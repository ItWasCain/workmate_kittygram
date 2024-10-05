from django.db.models import Avg
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.validators import UniqueTogetherValidator

from cats.models import Breed, Cat, Rating, User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    breed = PrimaryKeyRelatedField(queryset=Breed.objects.all(),
                                   many=False)
    rating = SerializerMethodField(read_only=False)
    owner = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Cat
        fields = (
            'id', 'name', 'color', 'age', 'breed',
            'owner', 'rating', 'description'
        )

    def get_rating(self, cat):
        if int(Rating.objects.filter(cat=cat).count()) == 0:
            return 'Этого котика еще никто не оценил'
        return round(
            Rating.objects.filter(
                cat=cat
            ).aggregate(Avg('rate'))['rate__avg'],
            2
        )

    def get_owner_name(self, cat):
        return cat.owner.username


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    cat = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        default=CatSerializer()
    )

    class Meta:
        model = Rating
        fields = (
            'user', 'cat', 'rate',
        )

    def validate(self, attrs):
        data = {}
        if self.instance is None:
            data['cat'] = self.context['view'].kwargs.get('cat_id')
            data['user'] = self.fields['user'].get_default()

        unique_title_author = UniqueTogetherValidator(
            queryset=Rating.objects.all(),
            fields=('user', 'cat'),
            message='Вы уже оценили этого кота.'
        )
        unique_title_author(data, self)
        return super().validate(attrs)

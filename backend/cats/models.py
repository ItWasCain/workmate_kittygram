from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=200)


class Cat(models.Model):
    name = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    description = models.TextField(null=False)
    breed = models.ForeignKey(
        Breed, related_name='cats',
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(
        User, related_name='rating',
        on_delete=models.CASCADE
    )
    cat = models.ForeignKey(
        Cat, related_name='rating',
        on_delete=models.CASCADE,
    )
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'cat'], name='unique_rate')
        ]

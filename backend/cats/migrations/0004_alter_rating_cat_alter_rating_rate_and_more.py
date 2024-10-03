# Generated by Django 4.2.16 on 2024-10-01 10:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='cat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='cats.cat'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'cat'), name='rating_once'),
        ),
    ]

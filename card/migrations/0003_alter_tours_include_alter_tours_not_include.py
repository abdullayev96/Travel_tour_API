# Generated by Django 4.2.8 on 2024-02-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_tourstranslation_name_alter_tours_not_include'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='include',
            field=models.ManyToManyField(related_name='include', to='card.include', verbose_name="o'z ichiga oladi:"),
        ),
        migrations.AlterField(
            model_name='tours',
            name='not_include',
            field=models.ManyToManyField(related_name='include1', to='card.include', verbose_name="o'z ichiga olmaydi:"),
        ),
    ]

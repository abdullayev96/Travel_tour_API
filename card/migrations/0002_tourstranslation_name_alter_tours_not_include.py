# Generated by Django 4.2.8 on 2024-02-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourstranslation',
            name='name',
            field=models.CharField(default=2, max_length=200, verbose_name='Joy nomi:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tours',
            name='not_include',
            field=models.ManyToManyField(related_name='include1', to='card.include', verbose_name='not include:'),
        ),
    ]

# Generated by Django 4.2.8 on 2024-02-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourtranslation',
            name='name',
            field=models.CharField(default=2, max_length=200, verbose_name='Joy nomi:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='include',
            field=models.ManyToManyField(related_name='include', to='opinion.includes', verbose_name="o'z ichiga oladi:"),
        ),
        migrations.AlterField(
            model_name='tour',
            name='not_include',
            field=models.ManyToManyField(related_name='include1', to='opinion.includes', verbose_name="o'z ichiga olmaydi:"),
        ),
    ]

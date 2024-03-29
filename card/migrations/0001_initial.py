# Generated by Django 4.2.8 on 2024-01-21 16:15

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Kategoriya_',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Shahar_',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Mehmonxona_',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='note/')),
            ],
            options={
                'verbose_name': 'Rasm_',
            },
        ),
        migrations.CreateModel(
            name='Include',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Xizmatlar_',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Nights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200, verbose_name='Dam olish soni:')),
            ],
            options={
                'verbose_name': 'Kechalar_',
            },
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=40, verbose_name='dam olish kunlari:')),
                ('image1', models.ImageField(upload_to='yes/', verbose_name='joy rasmi:')),
                ('price', models.FloatField()),
                ('people_price', models.IntegerField()),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('created_at', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='card.category')),
                ('city', models.ManyToManyField(related_name='city', to='card.city', verbose_name='Shahar:')),
                ('hotel', models.ManyToManyField(related_name='hotel', to='card.hotel', verbose_name='Mehmonxona:')),
                ('image', models.ManyToManyField(related_name='image', to='card.images', verbose_name='rasmlar')),
                ('include', models.ManyToManyField(related_name='include', to='card.include', verbose_name='xizmatlar:')),
                ('night', models.ManyToManyField(related_name='night', to='card.nights', verbose_name='Mehmonxonadagi  kechalar:')),
                ('not_include', models.ManyToManyField(related_name='include1', to='card.include', verbose_name='xizmatlar:')),
            ],
            options={
                'verbose_name': 'Sayohat_',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TourTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name="To'liq ism, familiyasi:")),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email:')),
                ('number', models.CharField(max_length=40, verbose_name='Raqamizgizni kiriting:')),
                ('ticket', models.CharField(choices=[('Tickets Type 1', 'Tickets Type 1'), ('Tickets Type 2', 'Tickets Type 2'), ('Tickets Type 3', 'Tickets Type 3')], default='Tickets Type 1', max_length=20, verbose_name='Chipta:')),
                ('adults', models.CharField(choices=[('Adult', 'Adult'), ('one', 1), ('two', 2), ('three', 3)], default=1, max_length=20, verbose_name='Kottalar:')),
                ('childs', models.CharField(choices=[('Child', 'Child'), ('one', 1), ('two', 2), ('three', 3)], default=1, max_length=20, verbose_name='Bolalar:')),
                ('message', models.CharField(max_length=500, verbose_name='Kelgan xabarlar:')),
                ('created_at', models.DateField()),
            ],
            options={
                'verbose_name': 'Mehmonxona_band_qilish_',
            },
        ),
        migrations.CreateModel(
            name='ToursTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('body', models.TextField(verbose_name='joy haqida malumot:')),
                ('tour_type', models.TextField(verbose_name=' Paket turi haqida:')),
                ('people', models.TextField(verbose_name='Odamlar soni:')),
                ('guide', models.TextField(verbose_name="Ko'rsatuvchilar soni:")),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='card.tours')),
            ],
            options={
                'verbose_name': 'Sayohat_ Translation',
                'db_table': 'card_tours_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='IncludeTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Xizmatlar nomi:')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='card.include')),
            ],
            options={
                'verbose_name': 'Xizmatlar_ Translation',
                'db_table': 'card_include_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HotelTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Mehmonxona')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='card.hotel')),
            ],
            options={
                'verbose_name': 'Mehmonxona_ Translation',
                'db_table': 'card_hotel_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CityTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Shahar nomi:')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='card.city')),
            ],
            options={
                'verbose_name': 'Shahar_ Translation',
                'db_table': 'card_city_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Kategoriya nomi:')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='card.category')),
            ],
            options={
                'verbose_name': 'Kategoriya_ Translation',
                'db_table': 'card_category_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]

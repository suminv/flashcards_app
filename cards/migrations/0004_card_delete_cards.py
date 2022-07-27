# Generated by Django 4.0.4 on 2022-07-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_rename_data_created_cards_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('box', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]

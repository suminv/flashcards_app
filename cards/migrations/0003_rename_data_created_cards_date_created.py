# Generated by Django 4.0.4 on 2022-07-26 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_cards_answer_alter_cards_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='data_created',
            new_name='date_created',
        ),
    ]

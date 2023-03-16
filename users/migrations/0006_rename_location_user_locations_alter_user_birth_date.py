# Generated by Django 4.1.7 on 2023-03-16 13:12

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='locations',
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, validators=[users.validators.check_birth_date]),
        ),
    ]
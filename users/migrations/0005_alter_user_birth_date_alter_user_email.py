# Generated by Django 4.1.7 on 2023-03-14 11:46

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(validators=[users.validators.check_birth_date]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, validators=[users.validators.check_email]),
        ),
    ]

# Generated by Django 4.2.7 on 2024-09-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BancoAGil', '0007_rename_email_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpf',
            name='email',
            field=models.CharField(default='no-reply@example.com', max_length=254),
        ),
    ]

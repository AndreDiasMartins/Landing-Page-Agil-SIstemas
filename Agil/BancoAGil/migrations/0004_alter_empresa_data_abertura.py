# Generated by Django 5.0.3 on 2024-09-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BancoAGil', '0003_alter_email_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='data_abertura',
            field=models.CharField(max_length=20),
        ),
    ]

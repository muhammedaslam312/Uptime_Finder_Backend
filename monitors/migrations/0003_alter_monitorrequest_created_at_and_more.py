# Generated by Django 4.1.4 on 2022-12-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0002_alter_monitorrequest_response_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='monitorrequest',
            name='response_time',
            field=models.IntegerField(null=True),
        ),
    ]

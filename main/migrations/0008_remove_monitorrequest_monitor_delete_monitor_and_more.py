# Generated by Django 4.1.4 on 2022-12-24 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_monitor_monitorrequest_delete_hello_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitorrequest',
            name='monitor',
        ),
        migrations.DeleteModel(
            name='Monitor',
        ),
        migrations.DeleteModel(
            name='MonitorRequest',
        ),
    ]

# Generated by Django 3.1 on 2020-08-16 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diamond_doc', '0014_auto_20200816_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diamond_doc.userinfo')),
            ],
        ),
    ]

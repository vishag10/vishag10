# Generated by Django 4.2.7 on 2024-01-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplications',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

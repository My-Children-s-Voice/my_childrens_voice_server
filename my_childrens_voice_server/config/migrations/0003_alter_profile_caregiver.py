# Generated by Django 4.2.4 on 2023-09-04 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_rename_inpatiant_children_inpatiantchildren_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='caregiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caregiver', to='config.caregiver'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_material_created_at_material_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='unit',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]

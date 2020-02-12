# Generated by Django 2.2 on 2019-04-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'ordering': ('diagnosis_code_type', 'full_code')},
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='full_code',
            field=models.CharField(default='Test', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis_code',
            field=models.CharField(max_length=15),
        ),
    ]
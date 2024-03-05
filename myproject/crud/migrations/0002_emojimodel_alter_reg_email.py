# Generated by Django 5.0.2 on 2024-03-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmojiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='reg',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
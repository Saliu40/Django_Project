# Generated by Django 5.0.2 on 2024-03-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000, null=True)),
                ('title', models.CharField(max_length=1000, null=True)),
                ('url', models.CharField(max_length=1000, null=True)),
                ('content', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
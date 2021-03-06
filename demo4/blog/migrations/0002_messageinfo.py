# Generated by Django 0002.0002.0001 on 2019-05-23 13:22

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(max_length=50)),
                ('info', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': '信息',
                'verbose_name_plural': '信息',
            },
        ),
    ]

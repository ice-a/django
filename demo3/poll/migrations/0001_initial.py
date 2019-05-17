# Generated by Django 2.2.1 on 2019-05-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='投票列表')),
                ('choseA', models.CharField(max_length=30, verbose_name='A选项')),
                ('choseB', models.CharField(max_length=30, verbose_name='B选项')),
                ('resualtA', models.IntegerField(null=True, verbose_name='A选项的结果')),
                ('resualtB', models.IntegerField(null=True, verbose_name='B选项的结果')),
            ],
        ),
    ]
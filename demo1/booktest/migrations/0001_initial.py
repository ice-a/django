# Generated by Django 2.2.1 on 2019-05-14 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.BooleanField(verbose_name=True)),
                ('skill', models.CharField(max_length=30, null=True)),
                ('wj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.book')),
            ],
        ),
    ]

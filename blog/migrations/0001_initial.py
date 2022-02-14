# Generated by Django 4.0.1 on 2022-02-14 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=10000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
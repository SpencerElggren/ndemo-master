# Generated by Django 2.1.7 on 2019-08-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='postimage')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'postimage',
            },
        ),
    ]
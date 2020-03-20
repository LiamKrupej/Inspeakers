# Generated by Django 2.1.5 on 2020-03-20 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspeakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AlterModelOptions(
            name='speakerprofile',
            options={'verbose_name_plural': 'speakerprofiles'},
        ),
        migrations.AddField(
            model_name='speakerprofile',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='speakerprofile',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='speakerprofile',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='speakerprofile',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='inspeakers.SpeakerProfile'),
        ),
    ]
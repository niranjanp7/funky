# Generated by Django 3.2.6 on 2021-08-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_css_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='js_file',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='css_file',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='html_file',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

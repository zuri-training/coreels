# Generated by Django 4.0.6 on 2022-07-29 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewer', to=settings.AUTH_USER_MODEL, verbose_name='viewed by'),
        ),
        migrations.AddField(
            model_name='reel',
            name='category',
            field=models.ManyToManyField(help_text='choose video category', to='reel.category', verbose_name='video category'),
        ),
        migrations.AddField(
            model_name='reel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by'),
        ),
        migrations.AddField(
            model_name='like',
            name='real',
            field=models.ForeignKey(help_text='reel liked', on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='reel.reel', verbose_name='liked reel'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL, verbose_name='liked by'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='real',
            field=models.ForeignKey(help_text='reel being favorited', on_delete=django.db.models.deletion.CASCADE, related_name='favoriited', to='reel.reel', verbose_name='favorite on'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoriter', to=settings.AUTH_USER_MODEL, verbose_name='favorited by'),
        ),
        migrations.AddField(
            model_name='dislike',
            name='real',
            field=models.ForeignKey(help_text='reel disliked', on_delete=django.db.models.deletion.CASCADE, related_name='disliked', to='reel.reel', verbose_name='disliked reel'),
        ),
        migrations.AddField(
            model_name='dislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disliker', to=settings.AUTH_USER_MODEL, verbose_name='disliked by'),
        ),
        migrations.AddField(
            model_name='comment',
            name='real',
            field=models.ForeignKey(help_text='reel commented on', on_delete=django.db.models.deletion.CASCADE, related_name='commented', to='reel.reel', verbose_name='comment on'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL, verbose_name='commented by'),
        ),
    ]
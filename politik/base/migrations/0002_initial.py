# Generated by Django 5.1.2 on 2024-10-09 12:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.categoryblog'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.blogpost'),
        ),
        migrations.AddField(
            model_name='commentforum',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentforum',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='base.commentforum'),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='base.forumthread'),
        ),
        migrations.AddField(
            model_name='commentforum',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.forumthread'),
        ),
        migrations.AddField(
            model_name='vote',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.candidate'),
        ),
        migrations.AddField(
            model_name='voteresult',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.candidate'),
        ),
        migrations.AddField(
            model_name='votesession',
            name='candidates',
            field=models.ManyToManyField(related_name='vote_sessions', to='base.candidate'),
        ),
        migrations.AddField(
            model_name='voteresult',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.votesession'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('candidate', 'user_ip')},
        ),
    ]

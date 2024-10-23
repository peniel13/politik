# Generated by Django 5.1.2 on 2024-10-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_votesession_candidates_delete_vote_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_debut_votes', models.DateTimeField(blank=True, null=True)),
                ('date_fin_votes', models.DateTimeField(blank=True, null=True)),
                ('candidats', models.ManyToManyField(to='base.candidat')),
            ],
        ),
    ]

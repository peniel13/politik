# Generated by Django 5.1.2 on 2024-10-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_uservote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('content', models.TextField(max_length=400)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('device', models.CharField(max_length=30)),
                ('transaction_id', models.CharField(max_length=30)),
                ('transaction_number', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Preinscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('description', models.TextField(max_length=400)),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
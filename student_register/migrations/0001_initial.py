# Generated by Django 4.0.4 on 2022-05-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=154, null=True, unique=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'), ('Prefer Not Say', 'Prefer Not Say')], max_length=50)),
                ('path', models.CharField(choices=[('Aws-Dewops', 'Aws-Dewops'), ('Data Science', 'Data Science'), ('Full Stack', 'Full Stack'), ('Cyber Security', 'Cyber Security')], max_length=50)),
            ],
        ),
    ]

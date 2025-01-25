# Generated by Django 5.1.5 on 2025-01-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]

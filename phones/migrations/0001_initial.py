# Generated by Django 4.2.2 on 2023-06-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('phone_type', models.CharField(choices=[('Для школоты', 'Для школоты'), ('Для студентов и взрослых', 'Для студентов и взрослых'), ('Для пенсионеров', 'Для пенсионеров')], max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('cost', models.PositiveIntegerField()),
                ('video', models.URLField()),
            ],
        ),
    ]
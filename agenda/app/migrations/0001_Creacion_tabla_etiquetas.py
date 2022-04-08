# Generated by Django 4.0.3 on 2022-04-06 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='create_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='update_at')),
            ],
            options={
                'db_table': 'tbl_etiquetas',
                'ordering': ['-nombre'],
            },
        ),
    ]

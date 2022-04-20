# Generated by Django 4.0.3 on 2022-04-19 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_Cambio_col_foto_a_Cloudinary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('precio_diario', models.FloatField()),
                ('platoId', models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='menu.plato')),
            ],
            options={
                'db_table': 'tbl_stock',
                'unique_together': {('fecha', 'platoId')},
            },
        ),
    ]

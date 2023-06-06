# Generated by Django 4.2.1 on 2023-06-03 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_status_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['slug'], 'verbose_name': 'Cars', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Status of the Car'},
        ),
        migrations.AlterField(
            model_name='cars',
            name='brand',
            field=models.CharField(max_length=100, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='model',
            field=models.CharField(max_length=100, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Status of the Car'),
        ),
    ]
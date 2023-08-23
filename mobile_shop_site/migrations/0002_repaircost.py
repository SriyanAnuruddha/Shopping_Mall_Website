# Generated by Django 4.1.7 on 2023-05-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_shop_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reapir_name', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-22 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_customer_store_custo_last_na_2e448d_idx_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='given_name',
            new_name='first_name',
        ),
    ]

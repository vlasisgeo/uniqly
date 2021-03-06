# Generated by Django 3.1.2 on 2020-10-10 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('display_type', models.CharField(choices=[('TEXT', 'Text'), ('HEX', 'HEX Color'), ('IMG', 'Image')], default='TEXT', max_length=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_value', models.CharField(max_length=20, null=True)),
                ('active', models.BooleanField(default=True)),
                ('attribute_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.attribute_group')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Product_variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_code', models.CharField(max_length=30, null=True)),
                ('barcode', models.CharField(max_length=30, null=True)),
                ('factory_code', models.CharField(max_length=20, null=True)),
                ('weight', models.IntegerField(blank=True, default=0)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('vat_percent', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.country')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, default=0)),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product_variant')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.warehouse')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.zone')),
            ],
        ),
        migrations.CreateModel(
            name='Product_variant_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.attribute_value')),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product_variant')),
            ],
        ),
        migrations.CreateModel(
            name='Product_route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('active', models.BooleanField(default=False)),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product_variant')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.route')),
                ('vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vat')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]

# Generated by Django 2.0 on 2018-10-24 10:54

from decimal import Decimal
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
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, unique=True)),
                ('cardholder_name', models.CharField(max_length=26)),
                ('cvv', models.CharField(max_length=3)),
                ('expires_at', models.DateField()),
                ('monthly_billing_day', models.PositiveIntegerField()),
                ('limit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('available', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
            ],
            options={
                'ordering': ['-monthly_billing_day', 'limit'],
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_limit', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('credit_available', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='creditcard',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='credit_cards', to='wallets.Wallet'),
        ),
    ]

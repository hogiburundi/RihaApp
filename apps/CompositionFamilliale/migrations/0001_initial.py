# Generated by Django 3.0 on 2020-06-27 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_auto_20200627_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('zone_price', models.IntegerField(default=0)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='composition_price_province', to='base.Zone')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_apps', models.CharField(default='Attestation de composition familliale', max_length=50)),
                ('fullname_lady', models.CharField(max_length=50)),
                ('date_delivrated', models.DateField(default=django.utils.timezone.now)),
                ('rejection_msg', models.TextField(blank=True, null=True)),
                ('secretary_validated', models.BooleanField(null=True)),
                ('ready', models.BooleanField(default=False)),
                ('residence_quarter', models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='composition_residence', to='base.Quarter')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='composition_user', to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='composition_zone', to='base.Zone')),
                ('zone_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='composition_province_payment', to='base.PaymentZone')),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname_child', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CompositionFamilliale.Document')),
            ],
        ),
    ]

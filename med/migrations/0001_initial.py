# Generated by Django 2.1.7 on 2019-04-05 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('demand', models.IntegerField(default=1)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicine_stock', to='med.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile_user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role', models.CharField(choices=[('retailer', 'retailer'), ('distributor', 'distributor'), ('supplier', 'supplier')], default=None, max_length=15)),
                ('is_supplier', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='supplier',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='med.UserProfile'),
        ),
        migrations.AddField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_supplier': False}, on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='med.UserProfile'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='retailer', to='med.UserProfile'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='user',
            field=models.ManyToManyField(through='med.stock', to='med.UserProfile'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='distributor', to='med.UserProfile'),
        ),
    ]
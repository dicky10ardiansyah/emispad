# Generated by Django 3.2 on 2022-05-25 06:27

import datetime
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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nama lengkap')),
                ('jk', models.CharField(choices=[('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], default='laki-laki', max_length=20, verbose_name='Jenis kelamin')),
                ('tgl_lahir', models.DateField(blank=True, null=True, verbose_name='Tanggal lahir / (yyyy-mm-dd)')),
                ('tempat_lahir', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tempat lahir')),
                ('alamat', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alamat asal')),
                ('nama_ortu', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nama orang tua')),
                ('no_hp', models.CharField(blank=True, max_length=100, null=True, verbose_name='No Telp. orang tua')),
                ('posisi', models.CharField(choices=[('dipondok', 'Di pondok'), ('pulang', 'Pulang')], default='dipondok', max_length=20, verbose_name='posisi')),
                ('kondisi', models.CharField(choices=[('lulus', 'Lulus'), ('mondok', 'Mondok')], default='lulus', max_length=20, verbose_name='Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('out', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('present', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

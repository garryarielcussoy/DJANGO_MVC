# Generated by Django 3.0 on 2019-12-09 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('jabatan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelajaran', models.CharField(max_length=200)),
                ('jadwal_mulai', models.DateTimeField(verbose_name='jadwal_mulai')),
                ('jadwal_akhir', models.DateTimeField(verbose_name='jadwal_akhir')),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('nomor_absen', models.IntegerField(default=0)),
                ('nilai_rata_rata', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ata.MataPelajaran')),
            ],
        ),
        migrations.CreateModel(
            name='LiveCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_live_code', models.CharField(max_length=200)),
                ('banyak_soal', models.IntegerField(default=0)),
                ('bobot_nilai', models.FloatField(default=0.0)),
                ('tanggal_pelaksanaan', models.DateField(verbose_name='tanggal_pelaksanaan')),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ata.MataPelajaran')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_challenge', models.CharField(max_length=200)),
                ('banyak_soal', models.IntegerField(default=0)),
                ('bobot_nilai', models.FloatField(default=0.0)),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ata.MataPelajaran')),
            ],
        ),
    ]

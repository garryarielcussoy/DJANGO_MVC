from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)
    bidang = models.CharField(max_length=200)
    jadwal_praktek = models.DateTimeField('jadwal_praktek')

    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)
    alamat = models.CharField(max_length=255)
    keluhan = models.TextField()

    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length=200)
    total_harga = models.BigIntegerField(default=0)
    kumpulan_obat = models.TextField() # Many-to-Many?

    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length=200)
    kandungan = models.TextField()
    khasiat = models.TextField()

    def __str__(self):
        return self.nama
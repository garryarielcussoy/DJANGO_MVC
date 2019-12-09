from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=200)
    spesies = models.CharField(max_length=200)
    berat = models.IntegerField(default=0)
    umur = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length=200)
    isi_kandang = models.TextField()
    luas_kandang = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)
    jadwal_jaga = models.DateTimeField('jadwal_jaga')

    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)
    hari_berkunjung = models.DateTimeField('hari_berkunjung')

    def __str__(self):
        return self.nama
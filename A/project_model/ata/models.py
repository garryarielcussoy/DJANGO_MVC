from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)
    nomor_absen = models.IntegerField(default=0)
    nilai_rata_rata = models.FloatField(default =0.0)

    def __str__(self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=200)
    jadwal_mulai = models.DateTimeField('jadwal_mulai')
    jadwal_akhir = models.DateTimeField('jadwal_akhir')

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=200)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.FloatField(default=0.0)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge
    
class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=200)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.FloatField(default=0.0)
    tanggal_pelaksanaan = models.DateField('tanggal_pelaksanaan')
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code
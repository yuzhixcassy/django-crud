from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Ruangan(models.Model):
    lab = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.lab

class Matakuliah(models.Model):
    kodematkul = models.CharField(max_length=5, null=True)
    matakuliah = models.CharField(max_length=50)
    sks = models.IntegerField(null=True) #konversi sks ke menit atau dijadiin menit langsung
    
    def __str__(self):
        return self.matkul

class Dosen(models.Model):
    nip = models.IntegerField(null=True, blank=True)
    nama = models.CharField(max_length=50)
    notelp = models.IntegerField(null=True, blank=True)
    mail = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nama

class Jadwal(models.Model):
    hari = models.CharField(max_length=10,null=True)
    waktu = models.TimeField(null=True)
    lab_id = models.ForeignKey(Ruangan, on_delete=models.CASCADE, null=True)
    matkul_id = models.ForeignKey(Matakuliah, on_delete=models.CASCADE, null=True, blank=True)
    dosen_id = models.ForeignKey(Dosen, on_delete=models.CASCADE, null=True)
    # class Meta:
    #     unique_together = ('hari', 'waktu')
    
    def __str__(self):
        return self.hari
    
    # def clean(self):
    #     exiting_jadwal = Jadwal.objects.filter(hari=self.hari, waktu=self.waktu)
    #     if exiting_jadwal.exists():
    #         raise ValidationError('Jadwal Bentrok!')
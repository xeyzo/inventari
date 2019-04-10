from django.db import models


class Pegawai (models.Model):  
    id_pegawai = models.CharField(max_length=10, primary_key='true')
    nama_pegawai = models.CharField(max_length=30)
    nip = models.CharField(max_length=10)
    alamat = models.CharField(max_length=100)


def __unicode__(self):
    return self.nama_pegawai

class Peminjaman (models.Model):
    STATUS_PEMINJAMAN_CHOICE = (
        ('Dikembalikan','Dikembalikan'),
        ('Belum_Dikembalikan','Belum_Dikembalikan'),
    )

    id_peminjaman = models.CharField(max_length=10, primary_key='true')
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()
    status_peminjaman = models.CharField(max_length=30, choices=STATUS_PEMINJAMAN_CHOICE)


class Pengembalian (models.Model):
    STATUS_PEMINJAMAN_CHOICE = (
        ('Dikembalikan','Dikembalikan'),
        ('Belum_Dikembalikan','Belum_Dikembalikan'),
    )
    id_pengembalian = models.CharField(max_length=4, primary_key='true')
    id_peminjaman = models.ForeignKey('Peminjaman', on_delete=models.CASCADE,)
    tanggal_kembali = models.DateField()
    status_peminjaman = models.CharField(max_length=30, choices=STATUS_PEMINJAMAN_CHOICE)



class Petugas (models.Model):
    id_petugas = models.CharField(max_length=10, primary_key='true')
    nama_petugas = models.CharField(max_length=30)

class Detail_pinjam (models.Model):
    id_detail_pinjam = models.CharField(max_length=10, primary_key='true')
    id_inventaris = models.ForeignKey('Inventaris', on_delete=models.CASCADE,)
    jumlah = models.IntegerField()

class Inventaris (models.Model):
    KONDISI_CHOICE = (
        ('BARU','BARU'),
        ('BEKAS','BEKAS'),
    )

    id_inventaris = models.CharField(max_length=10, primary_key='true')
    nama = models.CharField(max_length=30)
    kondisi = models.CharField(max_length=5, choices=KONDISI_CHOICE)
    keterangan = models.TextField()
    jumlah = models.IntegerField()
    id_jenis = models.ForeignKey('Jenis', on_delete=models.CASCADE,)
    tanggal_register = models.DateField()
    kode_inventaris = models.CharField(max_length=10)
    id_petugas= models.ForeignKey('Petugas', on_delete=models.CASCADE,)

class Jenis (models.Model):
    id_jenis = models.CharField(max_length=10, primary_key='true')
    nama_jenis = models.CharField(max_length=30)
    kode_jenis = models.CharField(max_length=10)
    keterangan = models.TextField()

class Ruang (models.Model):
    id_ruang = models.CharField(max_length=10, primary_key='true')
    nama_ruang = models.CharField(max_length=30)
    kode_ruang = models.CharField(max_length=10)
    keterangan = models.TextField()

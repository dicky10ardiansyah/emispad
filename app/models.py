# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _


class Person(models.Model):
    """
    Class that manages the person model fields
    """
    name=models.CharField(_("Nama lengkap"),max_length=100,null=True,blank=True)
    tahun=models.CharField(_("Tahun"),max_length=50,null=True,blank=True)
    nis=models.CharField(_("NIS"),max_length=100,null=True,blank=True)
    nik=models.CharField(_("NIK"),max_length=100,null=True,blank=True)
    pendidikan=models.CharField(_("Pendidikan terakhir"),max_length=100,null=True,blank=True)
    tgl_masuk=models.CharField(_("Tanggal Masuk"),max_length=50,null=True,blank=True)
    tgl_lulus=models.CharField(_("Tanggal Lulus"),max_length=50,null=True,blank=True)
    jk = (('L', 'Laki-laki'), ('P', 'Perempuan'))
    jk = models.CharField(_("Jenis kelamin"),max_length=20,choices=jk,default='L')
    tgl_lahir=models.DateField(_("Tanggal lahir / (yyyy-mm-dd)"),null=True,blank=True)
    tempat_lahir=models.CharField(_("Tempat lahir"),max_length=100,null=True,blank=True)
    alamat=models.CharField(_("Alamat asal"),max_length=200,null=True,blank=True)
    nama_ortu=models.CharField(_("Nama orang tua"),max_length=100,null=True,blank=True)
    no_hp=models.CharField(_("No Telp. orang tua"),max_length=100,null=True,blank=True)
    status = (('Mondok', 'Mondok'), ('Pulang', 'Pulang'), ('Lulus', 'Lulus'))
    status = models.CharField(_("posisi"),max_length=20,choices=status,default='Mondok')

    def __str__(self):
        return self.name

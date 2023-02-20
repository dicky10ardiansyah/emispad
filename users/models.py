from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

import datetime
# Create your models here.
	

class Present(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	present=models.BooleanField(default=False)
	
class Time(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	time=models.DateTimeField(null=True,blank=True)
	out=models.BooleanField(default=False)
	
class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	nama=models.CharField(_("Nama lengkap"),max_length=100,null=True,blank=True)
	jk = (('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan'))
	jk = models.CharField(_("Jenis kelamin"),max_length=20,choices=jk,default='laki-laki')
	tgl_lahir=models.DateField(_("Tanggal lahir / (yyyy-mm-dd)"),null=True,blank=True)
	tempat_lahir=models.CharField(_("Tempat lahir"),max_length=100,null=True,blank=True)
	alamat=models.CharField(_("Alamat asal"),max_length=200,null=True,blank=True)
	nama_ortu=models.CharField(_("Nama orang tua"),max_length=100,null=True,blank=True)
	no_hp=models.CharField(_("No Telp. orang tua"),max_length=100,null=True,blank=True)
	posisi = (('dipondok', 'Di pondok'), ('pulang', 'Pulang'))
	posisi = models.CharField(_("posisi"),max_length=20,choices=posisi,default='dipondok')
	kondisi = (('lulus', 'Lulus'), ('mondok', 'Mondok'))
	kondisi = models.CharField(_("Status"),max_length=20,choices=kondisi,default='lulus')
	
	def __str__(self):
		return self.user.username
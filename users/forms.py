from django import forms
from .models import UserProfile
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)

class UserProfileForm(forms.ModelForm):

    nama = forms.CharField(label="Nama lengkap",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    jk=[('laki-laki','Laki-laki'),
         ('perempuan','Perempuan')]
    jk = forms.ChoiceField(label="Gender",choices=jk, widget=forms.RadioSelect)
    tgl_lahir = forms.DateField(label="Tanggal lahir",widget=TextInput(attrs={
            'class':'form-control',
            'id':'timePicker',
        }), required = True)
    tempat_lahir = forms.CharField(label="Tempat lahir",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    alamat = forms.CharField(label="Alamat asal",widget=Textarea(attrs={
            'class':'form-control',
        }), required = True)
    nama_ortu = forms.CharField(label="Nama Orang tua",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    no_hp = forms.CharField(label="No telp. Orang tua",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    posisi=[('dipondok','Di pondok'),('pulang','Pulang')]
    posisi = forms.ChoiceField(label="Posisi",choices=posisi, widget=forms.Select)
    kondisi=[('mondok','Mondok'),('lulus','Lulus')]
    kondisi = forms.ChoiceField(label="Status",choices=kondisi, widget=forms.Select)

    class Meta:

        model = UserProfile

        fields = [
            'nama',
            'jk',
            'tgl_lahir',
            'tempat_lahir',
            'alamat',
            'nama_ortu',
            'no_hp',
            'posisi',
            'kondisi',
        ]

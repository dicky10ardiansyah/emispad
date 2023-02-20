# -*- coding: utf-8 -*-
from django import forms
from app.models import *
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)


class PersonForm(forms.ModelForm):
    """
    Form that manages the person model fields
    """
    name = forms.CharField(label="Nama lengkap",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    tahun = forms.CharField(label="Tahun",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    nis = forms.CharField(label="NIS",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    nik = forms.CharField(label="NIK",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    pendidikan = forms.CharField(label="Pendidikan terakhir",widget=TextInput(attrs={
            'class':'form-control',
        }), required = True)
    tgl_masuk = forms.DateField(label="Tanggal Masuk",widget=TextInput(attrs={
            'class':'form-control',
            'id':'timePicker',
        }), required = True)
    tgl_keluar = forms.DateField(label="Tanggal Keluar",widget=TextInput(attrs={
            'class':'form-control',
            'id':'timePicker2',
        }), required = False)
    jk=[('L','Laki-laki'),
         ('P','Perempuan')]
    jk = forms.ChoiceField(label="Gender",choices=jk, widget=forms.RadioSelect)
    tgl_lahir = forms.DateField(label="Tanggal lahir",widget=TextInput(attrs={
            'class':'form-control',
            'id':'timePicker3',
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
    status=[('Mondok','Mondok'),('Pulang','Pulang'),('Lulus','Lulus')]
    status = forms.ChoiceField(label="Status",choices=status, widget=forms.Select)

    class Meta:

        model = Person

        fields = [
            'name',
            'tahun',
            'nis',
            'nik',
            'pendidikan',
            'tgl_masuk',
            'tgl_keluar',
            'jk',
            'tgl_lahir',
            'tempat_lahir',
            'alamat',
            'nama_ortu',
            'no_hp',
            'status',
        ]

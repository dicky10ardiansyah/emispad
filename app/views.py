# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from app.models import Person
from app.forms import PersonForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

@login_required
def List(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    persons = Person.objects.all().order_by('name')
    return render(request, 'app/person_list.html', {'persons': persons})

@login_required
def Detail(request, pk):
    if request.user.username!='admin':
        return redirect('not-authorised')
    person = Person.objects.get(pk=pk)
    return render(request, 'app/person_detail.html', {'person': person})

@login_required
def Create(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('detail', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'app/person_form.html', {'form': form})

@login_required
def Update(request, pk):
    if request.user.username!='admin':
        return redirect('not-authorised')
    person = Person.objects.get(pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save()
            return redirect('detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    return render(request, 'app/person_form.html', {'form': form})

@login_required
def Delete(request, pk):
    if request.user.username!='admin':
        return redirect('not-authorised')
    person = Person.objects.get(pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('list')
    return render(request, 'app/person_confirm_delete.html', {'person': person})

@login_required
def Hitung(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    persons = Person.objects.all()
    persons_count = persons.count()
    persons_pulang = persons.filter(status='Pulang').count()
    persons_laki = persons.filter(jk='L').count()
    persons_perempuan = persons.filter(jk='P').count()
    persons_lulus = persons.filter(status='Lulus').count()
    persons_mondok = persons.filter(status='Mondok').count()
    context = {
        'persons': persons,
        'persons_count': persons_count,
        'persons_pulang': persons_pulang,
        'persons_laki': persons_laki,
        'persons_perempuan': persons_perempuan,
        'persons_lulus': persons_lulus,
        'persons_mondok': persons_mondok,
    }
    
    return render(request, 'app/person_count.html', context)

@login_required
def Cari(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    if request.method == 'POST':
        searched = request.POST['searched']
        persons = Person.objects.filter(name__icontains=searched)
        return render(request, 'app/person_search.html', {'searched': searched, 'persons': persons})
    else:
        return render(request, 'app/person_search.html')

@login_required
def Person_csv(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="santri.csv"'

    writer = csv.writer(response)
    persons = Person.objects.all()
    writer.writerow(['TAHUN', 'NAMA', 'L/P', 'NIK', 'TEMPAT LAHIR', 'TANGGAL LAHIR', 'STATUS MONDOK', 'PENDIDIKAN TERAKHIR', 'TGL MASUK', 'TGL LULUS', 'ALAMAT SANTRI', 'NO TELP', 'NAMA ORANG TUA'])
    for person in persons:
        writer.writerow([person.tahun, person.name, person.jk, person.nik, person.tempat_lahir, person.tgl_lahir, person.status, person.pendidikan, person.tgl_masuk, person.tgl_lulus, person.alamat, person.no_hp, person.nama_ortu])
    return response


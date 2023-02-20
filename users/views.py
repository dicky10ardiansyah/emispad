from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
# Create your views here.
from .models import UserProfile
from django.http import HttpResponse
import csv

@login_required
def register(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        profile_form=UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save() ###add user to database
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, f'siswa telah terdaftar!')
            return redirect('dashboard')

    else:
        form=UserCreationForm()
        profile_form=UserProfileForm()
    return render(request,'users/register.html', {'form' : form, 'profile_form' : profile_form})

@login_required
def AbsenList(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    userprofiles = UserProfile.objects.all().order_by('nama')
    return render(request, 'users/absen_list.html', {'userprofiles': userprofiles})

@login_required
def AbsenDetail(request, pk):
    if request.user.username!='admin':
        return redirect('not-authorised')
    userprofile = UserProfile.objects.get(pk=pk)
    return render(request, 'users/absen_detail.html', {'userprofile': userprofile})

@login_required
def AbsenDelete(request, pk):
    if request.user.username!='admin':
        return redirect('not-authorised')
    userprofile = UserProfile.objects.get(pk=pk)
    userprofile.delete()
    messages.success(request, f'Data berhasil dihapus.')
    return redirect('absen_list')

@login_required
def AbsenCari(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    if request.method == 'POST':
        searched = request.POST['searched']
        userprofiles = UserProfile.objects.filter(nama__icontains=searched)
        return render(request, 'users/absen_search.html', {'searched': searched, 'userprofiles': userprofiles})
    else:
        return render(request, 'users/absen_search.html')

@login_required
def AbsenUpdate(request, pk):
    if request.user.username!='admin':
        return redirect('not-authorised')
    userprofile = UserProfile.objects.get(pk=pk)
    form = UserProfileForm(instance=userprofile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Data berhasil diubah.')
            return redirect('absen_list')
    return render(request, 'users/absen_form.html', {'form': form})

@login_required
def Detail_csv(request):
    if request.user.username!='admin':
        return redirect('not-authorised')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="detailsantri.csv"'

    writer = csv.writer(response)
    userprofiles = UserProfile.objects.all()
    writer.writerow(['NAMA', 'L/P', 'TANGGAL LAHIR', 'ALAMAT', 'NAMA ORTU'])
    for userprofile in userprofiles:
        writer.writerow([userprofile.nama,userprofile.jk,userprofile.tgl_lahir,userprofile.alamat,userprofile.nama_ortu])
    return response

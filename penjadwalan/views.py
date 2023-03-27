from django.shortcuts import render, redirect
#from django.http import HttpResponse
from penjadwalan.models import *
from penjadwalan.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"User berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan saat membuat akun!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form,
        }
        return render(request, 'signup.html', konteks)


#                                   J A D W A L
@login_required(login_url=settings.LOGIN_URL)
def jadwal(request):
    jdwl = Jadwal.objects.all()
    paginator = Paginator(jdwl, 5)
    page = request.GET.get('page')
    jdwl = paginator.get_page(page)


    konteks = {
        'jdwl' : jdwl,
    }
    return render(request, 'jadwal.html', konteks) #konteks

def validation(value):
    bentrok = False

'''@login_required(login_url=settings.LOGIN_URL)
def tambah_jadwal(request):
    if request.POST:
        form = FormJadwal(request.POST)
        if form.is_valid:
            form.save()
            form = FormJadwal()
            pesan = "Jadwal berhasil disimpan!"
            
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-jadwal.html', konteks)
    else:
        form = FormJadwal()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah-jadwal.html', konteks)'''

def tambah_jadwal(request):
    if request.POST:
        form = FormJadwal(request.POST)
        if form.is_valid:
            form.save()
            return redirect('jadwal')
    else:
        form = FormJadwal()
        konteks = {
            'form' : form,
        }
    return render (request, 'tambah-jadwal.html', konteks)
    



@login_required(login_url=settings.LOGIN_URL)
def ubah_jadwal(request, id_jadwal):
    jadwal = Jadwal.objects.get(id=id_jadwal)
    template = 'ubah-jadwal.html'
    if request.POST:
        form = FormJadwal(request.POST, instance=jadwal)
        if form.is_valid:
            form.save()
            messages.success(request, "Jadwal berhasil diperbarui!")
            return redirect('ubah_jadwal', id_jadwal = id_jadwal)
    else:
        form = FormJadwal(instance=jadwal)
        konteks = {
            'form' : form,
            'jadwal' : jadwal,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_jadwal(request, id_jadwal):
    jadwal = Jadwal.objects.filter(id=id_jadwal)
    jadwal.delete()

    messages.success(request, "Data berhasil dihapus!")
    return redirect('jadwal')


#                                   D O S E N
@login_required(login_url=settings.LOGIN_URL)
def dosen(request):
    dsn = Dosen.objects.all()
    paginator = Paginator(dsn, 5)
    page = request.GET.get('page')
    dsn = paginator.get_page(page)
    konteks = {
        'dsn' : dsn,
    }
    return render(request, 'dosen.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid:
            form.save()
            form = FormDosen()
            pesan = "Data Dosen berhasil disimpan!"
            
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah-dosen.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbarui!")
            return redirect('ubah_dosen', id_dosen = id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form' : form,
            'dosen' : dosen,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()

    messages.success(request, "Data berhasil dihapus!")
    return redirect('dosen')


#                                   M A T K U L

@login_required(login_url=settings.LOGIN_URL)
def matakuliah(request):
    matkul = Matakuliah.objects.all()
    paginator = Paginator(matkul, 5)
    page = request.GET.get('page')
    matkul = paginator.get_page(page)
    konteks = {
        'matkul' : matkul,
    }
    return render(request, 'matkul.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_matkul(request):
    if request.POST:
        form = FormMatkul(request.POST)
        if form.is_valid:
            form.save()
            form = FormMatkul()
            pesan = "Matakuliah berhasil ditambah!"
            
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-matkul.html', konteks)
    else:
        form = FormMatkul()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah-matkul.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_matkul(request, id_matakuliah):
    matkul = Matakuliah.objects.get(id=id_matakuliah)
    template = 'ubah-matkul.html'
    if request.POST:
        form = FormMatkul(request.POST, instance=matkul)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbarui!")
            return redirect('ubah_matkul', id_matakuliah = id_matakuliah)
    else:
        form = FormMatkul(instance=matkul)
        konteks = {
            'form' : form,
            'matkul' : matkul,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_matkul(request, id_matkul):
    matkul = Matakuliah.objects.filter(id=id_matkul)
    matkul.delete()

    messages.success(request, "Data berhasil dihapus!")
    return redirect('matkul')


#                                   R U A N G A N
def ruangan(request):
    rngn = Ruangan.objects.all()
    paginator = Paginator(rngn, 5)
    page = request.GET.get('page')
    rngn = paginator.get_page(page)
    konteks = {
        'rngn' : rngn,
    }
    return render(request, 'ruangan.html', konteks)

def tambah_ruangan(request):
    if request.POST:
        form = FormRuangan(request.POST)
        if form.is_valid:
            form.save()
            form = FormRuangan()
            pesan = "Ruangan berhasil ditambah!"
            
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-ruangan.html', konteks)
    else:
        form = FormRuangan()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah-ruangan.html', konteks)

def ubah_ruangan(request, id_rngn):
    rngn = Ruangan.objects.get(id=id_rngn)
    template = 'ubah-ruangan.html'
    if request.POST:
        form = FormRuangan(request.POST, instance=rngn)
        if form.is_valid:
            form.save()
            messages.success(request, "Ruangan berhasil diperbarui!")
            return redirect('ubah_ruangan', id_rngn = id_rngn)
    else:
        form = FormRuangan(instance=ruangan)
        konteks = {
            'form' : form,
            'rngn' : rngn,
        }
    return render(request, template, konteks)

def hapus_ruangan(request, id_rngn):
    rngn = Ruangan.objects.filter(id=id_rngn)
    rngn.delete()

    messages.success(request, "Ruangan berhasil dihapus!")
    return redirect('ruangan')
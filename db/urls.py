"""kelompok4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from penjadwalan.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', signup, name='signup'),
    
    path('jadwal/', jadwal, name='jadwal'),
    path('tambah-jadwal/', tambah_jadwal, name='tambah_jadwal'),
    path('jadwal/ubah/<int:id_jadwal>', ubah_jadwal, name='ubah_jadwal'), 
    path('jadwal/hapus/<int:id_jadwal>', hapus_jadwal, name='hapus_jadwal'), 

    path('dosen/', dosen, name='dosen'),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'), 
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),

    path('matkul/', matakuliah, name='matkul'),
    path('tambah-matkul/', tambah_matkul, name='tambah_matkul'),
    path('matkul/ubah/<int:id_matkul>', ubah_matkul, name='ubah_matkul'),  
    path('matkul/hapus/<int:id_matkul>', hapus_matkul, name='hapus_matkul'),

    path('ruangan/', ruangan, name='ruangan'),
    path('tambah-ruangan/', tambah_ruangan, name='tambah_ruangan'),
    path('ruangan/ubah/<int:id_rngn>', ubah_ruangan, name='ubah_ruangan'),  
    path('ruangan/hapus/<int:id_rngn>', hapus_ruangan, name='hapus_ruangan'),
]

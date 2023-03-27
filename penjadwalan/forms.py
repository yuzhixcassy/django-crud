from django.forms import ModelForm
from penjadwalan.models import *
from django import forms
from django.forms.widgets import DateInput, TimeInput, Select
from django.utils import formats
from django.core.exceptions import ValidationError

'''class FormJadwal(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'

        widgets = {
            'hari' : forms.TextInput({'class':'form-control'}),
            #'tanggal' : forms.DateInput({'type': 'date'}),
            'waktu' : forms.TimeInput({'type': 'time'}),
            'matakuliah_id' : forms.Select({'class':'form-control'}),
            'dosen_id' : forms.Select({'class':'form-control'}),
            'lab_id' : forms.Select({'class':'form-control'}),
        }'''

class FormJadwal(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = ['hari', 'waktu', 'matkul_id', 'dosen_id', 'lab_id']

        widgets = {
            'hari' : forms.TextInput({'class':'form-control'}),
            'waktu' : forms.TimeInput({'type': 'time'}),
            'matkul_id' : forms.Select({'class':'form-control'}),
            'dosen_id' : forms.Select({'class':'form-control'}),
            'lab_id' : forms.Select({'class':'form-control'}),
        }
    # def clean(self):
    #     hari = self.cleaned_data['hari']
    #     waktu = self.cleaned_data['waktu']
    #     if hari and waktu:
    #         raise forms.ValidationError("Jadwal Bentrok!")
        # cleaned_data = super().clean()
        # hari = cleaned_data.get('hari')
        # waktu = cleaned_data.get('waktu')
        # lab_id = cleaned_data.get('lab_id')
        
        #if hari and waktu and lab_id:
         #   conflicting_schedules = Jadwal.objects.filter(
          #      hari__lt = waktu,
           #     waktu__lt = hari,
           #     lab_id = lab_id,
           # )
           # if self.instance:
           #     conflicting_schedules = conflicting_schedules.exclude(pk=self.instance.pk)
           # if conflicting_schedules.exists():
           #     raise forms.ValidationError("Jadwal Bentrok!")

class FormDosen(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'notelp' : forms.TextInput({'class':'form-control'}),
            'mail' : forms.TextInput({'class':'form-control'}),
        }

class FormMatkul(forms.ModelForm):
    class Meta:
        model = Matakuliah
        fields = '__all__'

        widgets = {
            'kode matkul' : forms.TextInput({'class':'form-control'}),
            'matkul' : forms.TextInput({'class':'form-control'}),
            'sks' : forms.TextInput({'class':'form-control'}),
        }

class FormRuangan(forms.ModelForm):
    class Meta:
        model = Ruangan
        fields = '__all__'

        widgets = {
            'lab' : forms.TextInput({'class':'form-control'}),
            'keterangan' : forms.TextInput({'class':'form-control'}),
        }
import streamlit as st
import pandas as pd
from datetime import date
from data import siswa
##definition
now = date.today()
##data
st.title("Absen Aplication")
st.header("X TKJ 3")
form = st.form(key="my_form")
tanggal = form.date_input("Tanggal", now)
namaSiswa = form.multiselect("Absensi",
                             options=siswa.nama,
                             help="tentukan untuk siapa")
keterangan = form.radio("keterangan",
                        ('Hadir', 'Sakit', 'Izin', 'Tanpa Keterangan'))
submitted = form.form_submit_button("Submit")
data = {"tanggal":{tanggal.strftime("%d %B, %Y"): {"Siswa": namaSiswa, "Ket": keterangan}}}
print(data)
if (submitted):
	data["tanggal"]:{tanggal:{"Siswa":namaSiswa,"Ket":keterangan}}}
for k,v in data["tanggal"].items():
	rekapAbsen = st.title('Rekap Absen')
	st.write("Absen Tanggal :", k)
	st.table(v)

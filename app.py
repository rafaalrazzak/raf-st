import streamlit as st
import pandas as pd
from datetime import date
from data import siswa
##definition
now = date.today()
logo="https://raw.githubusercontent.com/raf-ar/raf-st/a4c5cb39868a9a6d0953e95aa60264a9eb7cf908/public/img/ambigram-v4.png"
##data

st.set_page_config(page_title="<raf />", page_icon=logo, layout="centered", initial_sidebar_state="auto", menu_items=None)
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
rekapAbsen = st.title('Rekap Absen')

if (submitted):
	for i in namaSiswa:
		data = {"tanggal": {tanggal.strftime("%d %B, %Y"): {i:keterangan}}}

dataRekap = {
 "Nama": namaSiswa,
 "Keterangan": keterangan
}
st.table(dataRekap)

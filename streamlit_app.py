# -*- coding: utf-8 -*-

# -- Sheet --

import warnings
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

st.title('Test')

# import library pandas
# Import library numpy
# Import library matplotlib dan seaborn untuk visualisasi
plt.style.use('seaborn')
# me-non aktifkan peringatan pada python
warnings.filterwarnings("ignore")

# Panggil file (load file bernama Jumlah-kematian.csv) dan simpan dalam dataframe
st.header('Sample Data Jumlah Kematian Tahun 2017-2019')
dataset = "https://filedn.com/lePVfyAoiNxFBjMKNqcr2O7/MICROCREDENTIAL/ProjectTugasAkhir/Jumlah-kematian.csv"
data =  pd.read_csv(dataset))

st.header('Sample Data Jumlah Kematian')
# tampilkan 5 baris awal dataset dengan function head()
st.write(data.head(5))
data.corr()

# st.write(data.info())

st.write(data.describe().astype(int))

# melihat jumlah baris dan jumlah kolom (bentuk data) pada data df dengan fungsi .shape
# st.text('jumlah baris dan jumlah kolom')
# st.write(data.shape)

st.header('Mengecek Data yang Hilang')
# cek nilai yang hilang / missing values di dalam data
st.write(data.isnull().sum())

st.header('Table Jumlah Penyebab Kematian 1')
st.write(pd.pivot_table(data=data, index='kematian', columns=['penyebab'], values='jumlah', aggfunc='sum').fillna(0).astype(int))

st.header('Table Jumlah Penyebab Kematian 2')
df=pd.pivot_table(data=data, index='penyebab', values='jumlah', aggfunc='sum')
st.write(pd.pivot_table(data=data, index='penyebab', values='jumlah', aggfunc='sum'))

st.header('Bar Jumlah Kematian')
st.bar_chart(pd.pivot_table(data=data, index='penyebab', values='jumlah', aggfunc='sum'))

st.header('Pivot Tableaa')
pnyb = ['ASFIKSIA','BBLR','CAMPAK','DEMAM','DIARE','DIFTERI','GANGGUAN DARAH','GANGGUAN METABOLIK','HIPERTENSI','INFEKSI','KELAINAN','KELAINAN SARAF','LAIN-LAIN','MALARIA','PENDARAHAN','PNEUMONIA','SALURAN CERNA','SEPSIS','TETANUS']
fig = px.pie(df,values='jumlah', names=pnyb, title='my eyes cryin bruh')
st.plotly_chart(fig)

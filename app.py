# -*- coding: utf-8 -*-

# -- Sheet --

import warnings
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title('Test')

# import library pandas
# Import library numpy
# Import library matplotlib dan seaborn untuk visualisasi
plt.style.use('seaborn')
# me-non aktifkan peringatan pada python
warnings.filterwarnings("ignore")

# Panggil file (load file bernama Jumlah-kematian.xlsx) dan simpan dalam dataframe
st.header('Sample Data Jumlah Kematian Tahun 2017-2018')
dataset = "https://filedn.com/lePVfyAoiNxFBjMKNqcr2O7/MICROCREDENTIAL/ProjectTugasAkhir/Jumlah-kematian.xlsx"
data = pd.read_excel(dataset)

st.header('Sample Data Jumlah Kematian')
# tampilkan 5 baris awal dataset dengan function head()
data.head(5)
data.info()
data.describe()

# melihat jumlah baris dan jumlah kolom (bentuk data) pada data df dengan fungsi .shape
data.shape

st.header('Mengecek Data yang Hilang')
# cek nilai yang hilang / missing values di dalam data
data.isnull().sum()
data.corr()

st.header('Pivot Table')
pd.pivot_table(data=data, index='kematian', columns=[
               'penyebab'], values='jumlah', aggfunc='sum'). fillna(0)

st.header('Pivot Table')
pd.pivot_table(data=data, index='penyebab', values='jumlah', aggfunc='sum')

st.header('Pivot Table')
pd.pivot_table(data=data, index='penyebab', values='jumlah', aggfunc='sum')\
    .plot.bar(figsize=(20, 10), colormap='tab20c').legend(title=None)

st.header('Pivot Table')
data.groupby(['penyebab']).sum().plot(autopct='%1.0f%%', kind='pie',
                                      subplots=True, y='jumlah', figsize=(15, 14), title='Persentasi')
plt.tight_layout()

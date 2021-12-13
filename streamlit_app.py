import warnings
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

st.title('Jumlah Kematian Tahun 2017-2019 DI JAWA BARAT')
plt.style.use('seaborn')
# me-non aktifkan peringatan pada python
warnings.filterwarnings("ignore")

# Panggil file (load file bernama Jumlah-kematian.xlsx) dan simpan dalam dataframe
st.header('Sample Data Jumlah Kematian Tahun 2017 - 2019')
dataset = "https://filedn.com/lePVfyAoiNxFBjMKNqcr2O7/MICROCREDENTIAL/ProjectTugasAkhir/Jumlah-kematian.xlsx"
data = pd.read_excel(dataset)

df.drop(['id', 'kode_kota_kabupaten'], axis=1, inplace=True)

st.header('Sample Data Jumlah Kematian')
# tampilkan 5 baris awal dataset dengan function head()
st.write(data.head(5))
data.corr()

st.write(data.describe().astype(int))


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

st.header('Pie chart')
pnyb = ['ASFIKSIA','BBLR','CAMPAK','DEMAM','DIARE','DIFTERI','GANGGUAN DARAH','GANGGUAN METABOLIK','HIPERTENSI','INFEKSI','KELAINAN','KELAINAN SARAF','LAIN-LAIN','MALARIA','PENDARAHAN','PNEUMONIA','SALURAN CERNA','SEPSIS','TETANUS']
fig = px.pie(df,values='jumlah', names=pnyb, title='Pie chart Jumlah Penyebab Kematian ')
st.plotly_chart(fig)

#===START PLOT===
plt.figure(figsize=(24,10)) 
plt.plot(jumlah_pneu,c="red")
plt.title("PNEUMONIA",fontsize=16)
plt.xlabel("tahun 2017 - 2019",fontsize=16)
plt.ylabel("jumlah",fontsize=16)
plt.grid()
plt.show()
#===END PLOT===



#===START ILOC===
jpn=data.loc[(data.jumlah >= 0) & (data.penyebab == 'PNEUMONIA')]
jumlah_pneu=jpn.iloc[:,4:5].values
jumlah_pneu

jml=data.loc[(data.jumlah >= 0) & (data.penyebab == 'MALARIA')]
jumlah_mala=jml.iloc[:,4:5].values
jumlah_mala

jln=data.loc[(data.jumlah >= 0) & (data.penyebab == 'LAIN-LAIN')]
jumlah_lain=jln.iloc[:,4:5].values
jumlah_lain

jks=data.loc[(data.jumlah >= 0) & (data.penyebab == 'KELAINAN SARAF')]
jumlah_kelsaraf=jks.iloc[:,4:5].values
jumlah_kelsaraf

jke=data.loc[(data.jumlah >= 0) & (data.penyebab == 'KELAINAN')]
jumlah_kelainan=jke.iloc[:,4:5].values
jumlah_kelainan

jin=data.loc[(data.jumlah >= 0) & (data.penyebab == 'INFEKSI')]
jumlah_infek=jin.iloc[:,4:5].values
jumlah_infek

jht=data.loc[(data.jumlah >= 0) & (data.penyebab == 'HIPERTENSI')]
jumlah_hiper=jht.iloc[:,4:5].values
jumlah_hiper

jgm=data.loc[(data.jumlah >= 0) & (data.penyebab == 'GANGGUAN METABOLIK')]
jumlah_gmeta=jgm.iloc[:,4:5].values
jumlah_gmeta

jgd=data.loc[(data.jumlah >= 0) & (data.penyebab == 'GANGGUAN DARAH')]
jumlah_gdarah=jgd.iloc[:,4:5].values
jumlah_gdarah

jdf=data.loc[(data.jumlah >= 0) & (data.penyebab == 'DIFTERI')]
jumlah_difteri=jdf.iloc[:,4:5].values
jumlah_difteri

jdi=data.loc[(data.jumlah >= 0) & (data.penyebab == 'DIARE')]
jumlah_diare=jdi.iloc[:,4:5].values
jumlah_diare

jdm=data.loc[(data.jumlah >= 0) & (data.penyebab == 'DEMAM')]
jumlah_demam=jdm.iloc[:,4:5].values
jumlah_demam

jcm=data.loc[(data.jumlah >= 0) & (data.penyebab == 'CAMPAK')]
jumlah_campak=jcm.iloc[:,4:5].values
jumlah_campak

jbb=data.loc[(data.jumlah >= 0) & (data.penyebab == 'BBLR')]
jumlah_bblr=jbb.iloc[:,4:5].values
jumlah_bblr

jas=data.loc[(data.jumlah >= 0) & (data.penyebab == 'ASFIKSIA')]
jumlah_asfiksia=jas.iloc[:,4:5].values
jumlah_asfiksia

ja=data.loc[(data.jumlah >= 0) & (data.penyebab == 'PENDARAHAN')]
jumlah_pendarahan=ja.iloc[:,6:7].values
jumlah_pendarahan
#===END ILOC===
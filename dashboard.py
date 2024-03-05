# import libarary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sn
import plotly.express as px

px.defaults.template = "plotly_dark"
px.defaults.color_continous_scale = "reds"

#import dataset
days_df = pd.read_csv("https://raw.githubusercontent.com/Tasyanadila/Proyek-Analisis-Data/main/bike-sharing-datasets/day.csv")
hours_df = pd.read_csv("https://raw.githubusercontent.com/Tasyanadila/Proyek-Analisis-Data/main/bike-sharing-datasets/hour.csv")

# Sidebar with user information
st.sidebar.header("User Information")
st.sidebar.text(f"**Nama:** Tasya Nadila")
st.sidebar.text(f"**Email:** tasyanadila28012004@gmail.com")
st.sidebar.text(f"**ID Dicoding:** tasyanadila")

# Title
st.title("Bike-sharing dashboard")

### Conclution pertanyaan 1 
st.subheader("Apakah kondisi cuaca (weather situation) mempengaruhi tingkat kenaikan ataupun penurunan jumlah rata-rata sewa sepeda? dan bagaimana impactnya ditahun 2011 dan 2012, apakah ada perbedaan?")
st.markdown("Dari hasil visualisasi untuk pertanyaan 1 diatas aalah benar bahwa kondisi cuaca (weather situation) mempengaruhi tingkat kenaikan ataupun penurunan jumlah rata-rata sewa sepeda. Kemudian ada sedikit perbedaan impact di thaun 2011 dan 2012. Dari visualisasi diketahui bahwa pada cuaca cerah(clear) rata-rata sewa sepeda tinggi ditahun 2012 dan 2011, sedangkan di cuaca misty dan lightrain/snow rata-rata sewa sepeda turun, dan di cuaca heavy rain rata-rata sewa sepada sangatlah rendah di tahun 2011 dan 2012.")
  
### Conclution pertanyaan 2
st.subheader("Bagaimana tren penggunaan sepeda berubah setiap bulan dalam satu tahun tertentu?")
st.markdown("Trend penggunaan sepede relatif sama ditahun 2011 dan 2012, namun ditahun 2012 trend penggunaan sepeda lebih tinggi.")
  
### conclution pertanyaan 3
st.subheader("Pada musim (seasons) apa tingkat sewa sepeda (bike-riding) mendapat order terbanyak dalam tiap tahun (tahun 2011 dan 2012)?")
st.markdown("Musim panas (summer) merupakan musim dengan order sewa sepeda terbanyak di tahun 2011 dan 2012. Cuaca yang cerah, hangat, dan indah menjadi faktor utama yang mendorong tingginya order pada musim ini.")

### Conclusion pertanyaan 4
st.subheader("Bagaimana korelasi antara weekdays terhadap total order bike-riding berdasarkan kondisi cuaca?")
st.markdown("Cuaca cerah dan weekdays (Senin - Jum'at) merupakan kondisi yang paling ideal untuk bike-riding, sehingga menghasilkan total order tertinggi. Hujan lebat, baik weekdays (senin-jum'at) maupun weekend (sabtu-minggu), merupakan kondisi yang paling tidak ideal untuk bike-riding, sehingga menghasilkan total order terendah. Diketahui bahwa korelasi antara weekdays dan total order bike-riding dipengaruhi oleh kondisi cuaca.")

### Conclusion pertanyaan 5
st.subheader("Bagaimana korelasi antara suhu (temperature) terhadp total order bike-riding berdasarkan musim?")
st.markwodn("order bike-sharing memiliki nilai maksimum di summer dan nilai minimum di winter. Visualisasi yang ditampilkan sejalan dengan visualisasi yang ada di pertanyaan nomor 3. Dari hasil korelasi pertanyaan nomor 5 disimpulkan bahwa seiring dengan meningkatnya temperature orderan bike-sharing juga akan meningkat, puncaknya ada di musim summer.")

st.caption('Copyright © Tasya Nadila')
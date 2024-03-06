import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import seaborn as sn
import plotly.express as px
import os

# Set Plotly defaults
px.defaults.template = "plotly_dark"
px.defaults.color_continuous_scale = "reds"

# Import datasets
days_df = pd.read_csv("https://raw.githubusercontent.com/Tasyanadila/Proyek-Analisis-Data/main/Datasets/day.csv")
hours_df = pd.read_csv("https://raw.githubusercontent.com/Tasyanadila/Proyek-Analisis-Data/main/Datasets/hour.csv")

# Rename columns for days_df
column_mapping_days = {'dteday': 'date', 'yr': 'year', 'mnth': 'month', 'temp': 'temperature', 'hum': 'humidity', 'cnt': 'total'}
days_df.rename(columns=column_mapping_days, inplace=True)

# Rename columns for hours_df
column_mapping_hours = {'dteday': 'date', 'yr': 'year', 'hr': 'hour', 'mnth': 'month', 'temp': 'temperature', 'hum': 'humidity', 'cnt': 'total'}
hours_df.rename(columns=column_mapping_hours, inplace=True)

# Sidebar with user information
img = Image.open('bikes.jpg')
st.sidebar.image(img)

#visualization selection for the user
st.sidebar.header("Informasi")
selected_analysis = st.sidebar.selectbox("Pilih Salah Satu", ["Dataset Overview", "Visualization", "Conclusion"])

# Dataset overview
if selected_analysis == "Dataset Overview":
    # Title
    st.title("Overview dari dataset")
    
    # general information
    st.subheader("Tentang Dataset")
    st.markdown("Dataset ini terdiri dari dua data frame yang berasal di tahun 2011 dan 2012, yaitu hour.csv dan day.csv. Data hours memiliki 17379 baris dan 17 kolom, sedangkan data days memiliki 731 baris dan 16 kolom. Data ini berasal dari [kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset?resource=download) ")
    st.markdown("Bike-sharing rental(proses persewaan sepeda) sangat dipengaruhi oleh kondisi cuaca, musim, hari, dan jam. Oleh karenanya analisis data ini bertujuan untuk mengetahui faktor-faktor apa saja yang mempengaruhi jumlah sewa sepada di kota washington DC (tempat data ini bearasal).")
   
    # Dataframes
    st.subheader("Dataset Day")
    st.write(days_df)
    
    st.subheader("Dataset Hour")
    st.write(hours_df)
    
    # Statistik Deskriptif
    st.subheader("Statistik Deskriptif Dataset Day")
    st.write(days_df.describe())

    st.subheader("Statistik Deskriptif Dataset Hour")
    st.write(hours_df.describe())
    
    st.caption('Copyright © Tasya Nadila')

# Visualizations
elif selected_analysis == "Visualization":
    # Title
    st.title("Bike-Sharing Dashboard") 
    
    ### Plot 1
    st.subheader("Plot 1: Barchart Jumlah rata-rata sewa sepeda berdasarkan weather situation dan impactnya ditahun 2011 dan 2012")
    # Set the figure size
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    # Create a bar plot using the sn.barplot() function
    sn.barplot(
        x="weathersit",  # Kolom kondisi cuaca sebagai x
        y="total",  # Kolom jumlah total sewa sepeda sebagai y
        data=hours_df,
        hue="year",
        ax=ax1
    )

    # Add labels and a title to the plot
    ax1.set_xlabel("Weather Situation")
    ax1.set_ylabel("Average Total Rides")
    ax1.set_title("Impact of Weather on Average Bike Rentals")

    # Show the plot
    st.pyplot(fig1)

    ### Plot 2
    st.subheader("Plot 2: Trend penggunaan sepeda berdasarkan bulan")
    # Setting figsize
    fig2, ax2 = plt.subplots(figsize=(12, 6))

    # membuat linechart dengan fungsi sn.lineplot
    sn.lineplot(
        x="month",    # Kolom bulan
        y="total",    # Kolom jumlah total pesanan sepeda
        data=hours_df,
        hue="year",   # Pisahkan garis berdasarkan tahun
        marker='o',   # Menambahkan marker di setiap titik
        ax=ax2
    )

    # menambahkan label
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Average Total Rides")
    ax2.set_title("Monthly Bike Usage Trend Over Years")

    # menampilkan plot
    plt.xticks(rotation=45)  
    st.pyplot(fig2)

    ### Plot 3
    st.subheader("Plot 3: Bar chart total orders of bikeshare rides per Seasons")
    fig3, ax3 = plt.subplots(figsize=(10,6))

    sn.barplot(x='season', y='total', data=hours_df, hue='year', ax=ax3)

    ax3.set_xlabel("Season")
    ax3.set_ylabel("Total Rides")
    ax3.set_title("Total orders of bikeshare rides per Seasons")

    st.pyplot(fig3)

    ### Plot 4
    st.subheader("Plot 4: Heatmap korelasi antara weekdays dan total order bike-riding berdasarkan kondisi cuaca")
    fig4, ax4 = plt.subplots(figsize=(10,6))

    sn.scatterplot(x='weekday', y='total', data=days_df, hue='weathersit', ax=ax4)

    ax4.set_xlabel("Day of the Week")
    ax4.set_ylabel("Total Bike Rides")
    ax4.set_title("Bikeshare Rides Clustered by Weather Condition")

    # Show the plot
    st.pyplot(fig4)

    ### Plot 5
    st.subheader("Plot 5: Heatmap korelasi antara suhu (temperature) terhadap total order bike-riding berdasarkan musim")
    fig5, ax5 = plt.subplots(figsize=(10,6))

    sn.scatterplot(x='temperature', y='total', data=days_df, hue='season', ax=ax5)

    ax5.set_xlabel("Temperature (Celcius)")
    ax5.set_ylabel("Total Bike Rides")
    ax5.set_title("Clusters of bikeshare rides by season and temperature (2011-2012)")

    # Show the plot
    st.pyplot(fig5)

    st.caption('Copyright © Tasya Nadila')
    
# Conclusion
elif selected_analysis == "Conclusion":
    # Title
    st.title("Kesimpulan")

    ### Conclusion pertanyaan 1 
    st.subheader("Plot1: Barchart Jumlah rata-rata sewa sepeda berdasarkan weather situation dan impactnya ditahun 2011 dan 2012")
    st.markdown("adalah benar bahwa kondisi cuaca (weather situation) mempengaruhi tingkat kenaikan ataupun penurunan jumlah rata-rata sewa sepeda. Kemudian ada sedikit perbedaan impact di tahun 2011 dan 2012. Dari visualisasi diketahui bahwa pada cuaca cerah (clear) rata-rata sewa sepeda tinggi di tahun 2012 dan 2011, sedangkan di cuaca misty dan light rain/snow rata-rata sewa sepeda turun, dan di cuaca heavy rain rata-rata sewa sepeda sangat rendah di tahun 2011 dan 2012.")

    ### Conclution pertanyaan 2
    st.subheader("Plot2: Trend penggunaan sepeda berdasarkan bulan")
    st.markdown("Trend penggunaan sepede relatif sama ditahun 2011 dan 2012, namun ditahun 2012 trend penggunaan sepeda lebih tinggi.")
  
    ### conclution pertanyaan 3
    st.subheader("Plot3: Bar chart total orders of bikeshare rides per Seasons")
    st.markdown("Musim panas (summer) merupakan musim dengan order sewa sepeda terbanyak di tahun 2011 dan 2012. Cuaca yang cerah, hangat, dan indah menjadi faktor utama yang mendorong tingginya order pada musim ini.")

    ### Conclusion pertanyaan 4
    st.subheader("Plot4: Heatmap korelasi antara weekdays dan total order bike-riding berdasarkan kondisi cuaca")
    st.markdown("Cuaca cerah dan weekdays (Senin - Jum'at) merupakan kondisi yang paling ideal untuk bike-riding, sehingga menghasilkan total order tertinggi. Hujan lebat, baik weekdays (senin-jum'at) maupun weekend (sabtu-minggu), merupakan kondisi yang paling tidak ideal untuk bike-riding, sehingga menghasilkan total order terendah. Diketahui bahwa korelasi antara weekdays dan total order bike-riding dipengaruhi oleh kondisi cuaca.")

    ### Conclusion pertanyaan 5
    st.subheader("Plot5: Heatmap korelasi antara suhu (temperature) terhadap total order bike-riding berdasarkan musim")
    st.markdown("order bike-sharing memiliki nilai maksimum di summer dan nilai minimum di winter. Visualisasi yang ditampilkan sejalan dengan visualisasi yang ada di pertanyaan nomor 3. Dari hasil korelasi pertanyaan nomor 5 disimpulkan bahwa seiring dengan meningkatnya temperature orderan bike-sharing juga akan meningkat, puncaknya ada di musim summer.")

    st.caption('Copyright © Tasya Nadila')

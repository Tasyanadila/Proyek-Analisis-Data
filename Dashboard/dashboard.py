import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import seaborn as sn
import plotly.express as px

import os

# Set the page configuration
st.set_page_config(
    page_title="Bike-Sharing Dashboard",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set Plotly defaults
px.defaults.template = "plotly_dark"
px.defaults.color_continuous_scale = "reds"

# Load data
current_directory = os.path.dirname(os.path.abspath(__file__))
bike_path = os.path.join(current_directory, "bike_hour_df.csv")

bike_hour_df = pd.read_csv(bike_path)

# Sidebar with user information
img = Image.open('Dashboard/bikes.jpg')
st.sidebar.image(img)

#visualization selection for the user
st.sidebar.header("Informasi")
selected_analysis = st.sidebar.selectbox("Pilih Salah Satu", ["Dataset Overview", "Visualization", "Conclusion"])

if selected_analysis == "Dataset Overview":
    # Title
    st.title("Overview dari dataset")
    
    # general information
    st.subheader("Tentang Dataset")
    st.markdown("Dataframe ini memiliki 17379 baris dan 17 kolom. Data ini berasal dari [kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset?resource=download) ")
    st.markdown("Bike-sharing rental(proses persewaan sepeda) sangat dipengaruhi oleh kondisi cuaca, musim, hari, dan jam. Oleh karenanya analisis data ini bertujuan untuk mengetahui faktor-faktor apa saja yang mempengaruhi jumlah sewa sepada di kota washington DC (tempat data ini bearasal).")
   
    st.subheader("Dataset bike_hour_df.csv")
    st.write(bike_hour_df)
    
    st.subheader("Statistik Deskriptif Dataset bike_hour_df.csv")
    st.write(bike_hour_df.describe())
    
    st.caption('Copyright © Tasya Nadila')

# Visualizations
elif selected_analysis == "Visualization":
    # Title
    st.title("Bike-Sharing Dashboard") 

    # Total Bike User Section
    total_users = bike_hour_df["total_count"].sum()
    casual_users = bike_hour_df["casual_count"].sum()
    registered_users = bike_hour_df["registered_count"].sum()

    # Custom CSS to increase font size
    st.markdown(
        """
        <style>
             .big-blue-text {
                font-size: 24px;
                font-weight: bold;
                color: blue;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display Total Users
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Total Users")
        st.write(f'<p class="big-blue-text">{total_users}</p>', unsafe_allow_html=True)

    # Display Casual Users
    with col2:
        st.subheader("Casual Users")
        st.write(f'<p class="big-blue-text">{casual_users}</p>', unsafe_allow_html=True)

    # Display Registered Users
    with col3:
        st.subheader("Registered Users")
        st.write(f'<p class="big-blue-text"">{registered_users}</p>', unsafe_allow_html=True)


    
    ### Plot 1
    st.subheader("Plot 1: Barchart Jumlah rata-rata sewa sepeda berdasarkan weather situation dan impactnya ditahun 2011 dan 2012")
    
    # Konversi tipe data, memastikan bahwa tipe datanya berupa string atau object
    bike_hour_df['weathersit'] = bike_hour_df['weathersit'].astype(str)
    bike_hour_df['year'] = bike_hour_df['year'].astype(str)

    # Membuat figure menggunakan st.pyplot
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    chart1 = sn.barplot(
    x="weathersit",  # Kolom kondisi cuaca (weather sutuation) sebagai x
    y="total_count",  # Kolom jumlah total_count_count sewa sepeda sebagai y
    data=bike_hour_df,
    hue="year",
    ax=ax1
    )

    # Menambahkan labels dan title
    ax1.set_xlabel("Weather Situation")
    ax1.set_ylabel("Average total Rides")
    ax1.set_title("Impact of Weather on Average Bike Rentals")

    # Menampilkan plot menggunakan st.pyplot
    st.pyplot(fig1)
    
    st.subheader("Boxplot jumlah rata-rata sewa sepeda berdasarkan weather situation (kondisi cuaca)")
    # Boxplot
    fig, ax = plt.subplots(figsize=(10, 6))
    box_plot = sn.boxplot(x="weathersit", y="total_count", data=bike_hour_df, ax=ax)
    plt.title("Pengaruh Cuaca Terhadap Jumlah Sewa Sepeda")
    plt.xlabel("Weathersit")
    plt.ylabel("Jumlah Sewa Sepeda")

    # Display the boxplot using Streamlit
    st.pyplot(fig)

    ### Plot 2
    st.subheader("Plot 2: Trend penggunaan sepeda berdasarkan bulan")
    # Setting figsize
    fig, ax = plt.subplots(figsize=(12, 6))

    # membuat linechart dengan fungsi sn.lineplot
    sn.lineplot(
        x="month",    # Kolom bulan
        y="total_count",    # Kolom jumlah total pesanan sepeda
        data=bike_hour_df,
        hue="year",   # Pisahkan garis berdasarkan tahun
        marker='o',   # Menambahkan marker di setiap titik
        ax=ax  # Gunakan subplot yang sudah dibuat
        )

    # menambahkan label
    plt.xlabel("Month")
    plt.ylabel("Average Total Rides")
    plt.title("Monthly Bike Usage Trend Over Years")

    # menampilkan plot
    plt.xticks(rotation=45)
    st.pyplot(fig)  # Menggunakan st.pyplot untuk menampilkan plot di Streamlit
    
    # Plot 3: Bar chart dan pie chart total orders of bikeshare rides per Seasons
    st.subheader("Plot 3: Bar chart total orders of bikeshare rides per Seasons")

    # Set the figure size
    plt.figure(figsize=(10, 6))

    # Create a bar plot using the sn.barplot() function
    sn.barplot(
        x="season",        # Kolom musim
        y="total_count",   # Kolom jumlah total sewa sepeda
        data=bike_hour_df,
        hue="year"         # Beri warna berdasarkan tahun
        )

    # Add labels and a title to the plot
    plt.xlabel("Season")
    plt.ylabel("Total Rides")
    plt.title("Total orders of bikeshare rides per Seasons")

    # Show the plot
    st.pyplot(plt)
    
    st.subheader("pie chart total orders of bikeshare rides per seasons")
    
    # Set the figure size
    plt.figure(figsize=(6, 6))
    
    # Menghitung total rides per season
    season_total_rides = bike_hour_df.groupby('season')['total_count'].sum().reset_index()

    # Show pie chart using Streamlit
    plt.pie(season_total_rides['total_count'], labels=season_total_rides['season'], autopct='%1.1f%%', startangle=90, colors=sn.color_palette('pastel'))
    plt.title('Distribution of Total Rides by Season')

    # Display the pie chart using Streamlit
    st.pyplot(plt)

    ### Plot 4
    st.subheader("Plot 4: Scatter plot untuk melihat hubungan antara temperature dan total bike rental")
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter_plot = sn.scatterplot(x='temperature', y='total_count', hue='season', data=bike_hour_df, ax=ax)
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title('Correlation Between Temperature and Total Bike Rentals')

    # Display the plot using Streamlit
    st.pyplot(fig)

    st.caption('Copyright © Tasya Nadila')
    
# Conclusion
elif selected_analysis == "Conclusion":
    # Title
    st.title("Kesimpulan")

    ### Conclusion pertanyaan 1 
    st.subheader("Plot1: Barchart dan boxplot Jumlah rata-rata sewa sepeda berdasarkan weather situation dan impactnya ditahun 2011 dan 2012")
    st.markdown("Dari barchart dapat diketahui bahwa benar kondisi cuaca (weather situation) mempengaruhi tingkat kenaikan ataupun penurunan jumlah rata-rata sewa sepeda. Kemudian ada sedikit perbedaan impact di tahun 2011 dan 2012. Dari visualisasi diketahui bahwa pada cuaca cerah (clear) rata-rata sewa sepeda tinggi di tahun 2012 dan 2011, sedangkan di cuaca misty dan light rain/snow rata-rata sewa sepeda turun, dan di cuaca heavy rain rata-rata sewa sepeda sangat rendah di tahun 2011 dan 2012.")
    st.markdown("Dari boxplot dapat diketahui bahwa cuaca cerah (clear) memiliki jumlah sewa sepeda yang paling tinggi, sedangkan heavy rain memiliki jumlah sewa sepeda yang paling rendah ")

    ### Conclution pertanyaan 2
    st.subheader("Plot2: Trend penggunaan sepeda berdasarkan bulan")
    st.markdown("Trend penggunaan sepeda relatif sama ditahun 2011 dan 2012, namun ditahun 2012 trend penggunaan sepeda lebih tinggi.")
  
    ### conclution pertanyaan 3
    st.subheader("Plot3: Bar chart dan pie chart total orders of bikeshare rides per Seasons")
    st.markdown("Berdasarkan bar chart, musim panas (summer) merupakan musim dengan order sewa sepeda terbanyak di tahun 2011 dan 2012. Cuaca yang cerah, hangat, dan indah menjadi faktor utama yang mendorong tingginya order pada musim ini.")
    st.markdown("Dari visualisasi pie chart dapat dilihat juga dengan jelas persebaran total sewa sepeda berdasarkan musim. Musim panas(summer) memiliki persentase yang paling tinggi dibandingkan musim lainnya.")
    
    ### Conclusion pertanyaan 4
    st.subheader("Plot4: scatterplot untuk melihat korelasi antara temperature dengan jumlah bike rental.")
    st.markdown("Berdasarkan scatter-plot, order bike-sharing memiliki nilai maksimum di summer dan nilai minimum di winter. Visualisasi yang ditampilkan sejalan dengan visualisasi yang ada di pertanyaan nomor 3. Dari hasil korelasi pertanyaan nomor 4 disimpulkan bahwa seiring dengan meningkatnya temperature orderan bike-sharing juga akan meningkat, puncaknya ada di musim summer. Dengan kata lain dapat dikatakan bahwa suhu yang lebih tinggi umumnya terkait dengan jumlah persewaan sepeda yang lebih tinggi. Peningkatan suhu dapat mendorong lebih banyak orang untuk menyewa sepeda.")
    
    st.caption('Copyright © Tasya Nadila')

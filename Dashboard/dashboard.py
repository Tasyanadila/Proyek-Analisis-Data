import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import seaborn as sn
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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
    
    # Plot 3: Bar chart total orders of bikeshare rides per Seasons
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

    ### Plot 4
    # Scatter plot untuk melihat hubungan antara temperature dan total bike rental

    # Sidebar untuk pengaturan jumlah cluster
    num_clusters = st.sidebar.slider("Jumlah Cluster", 2, 3, 4)

    # Scatter plot untuk melihat hubungan antara temperature dan total bike rental
    st.subheader(f"Scatter plot - Hubungan antara suhu dan total sewa sepeda (Jumlah Cluster: {num_clusters})")

    # Set the figure size
    plt.figure(figsize=(10, 6))

    # Create a scatter plot using the sn.scatterplot() function
    sn.scatterplot(x='temperature', y='total_count', hue='season', data=bike_hour_df)

    # Add labels and a title to the plot
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title('Correlation Between Temperature and Total Bike Rentals')

    # Show the plot
    st.pyplot(plt)

    # Feature selection
    features = ['temperature']

    # Feature scaling
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(bike_hour_df[features])

    # KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    bike_hour_df['cluster'] = kmeans.fit_predict(scaled_data)

    # Scatter plot dengan warna berdasarkan cluster
    st.subheader(f'K-Means Clustering - {num_clusters} Clusters')

    # Set the figure size
    plt.figure(figsize=(10, 6))

    # Create a scatter plot using the sn.scatterplot() function
    sn.scatterplot(x='temperature', y='total_count', hue='cluster', data=bike_hour_df)

    # Add labels and a title to the plot
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title(f'K-Means Clustering - {num_clusters} Clusters')

    # Show the plot
    st.pyplot(plt)

    # Menampilkan karakteristik setiap cluster
    cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
    st.write("Cluster Centers:")
    st.write(cluster_centers)


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
    st.subheader("Plot4: Clustering Analisis untuk melihat korelasi antara temperature dengan jumlah bike rental dengan menggunakan K-means")
    st.markdown("order bike-sharing memiliki nilai maksimum di summer dan nilai minimum di winter. Visualisasi yang ditampilkan sejalan dengan visualisasi yang ada di pertanyaan nomor 3. Dari hasil korelasi pertanyaan nomor 4 disimpulkan bahwa seiring dengan meningkatnya temperature orderan bike-sharing juga akan meningkat, puncaknya ada di musim summer. Dengan kata lain dapat dikatakan bahwa suhu yang lebih tinggi umumnya terkait dengan jumlah persewaan sepeda yang lebih tinggi. Peningkatan suhu dapat mendorong lebih banyak orang untuk menyewa sepeda.")

    st.subheader("Hasil analisa teknik clustering")
    st.markdown("Scatter plot ini menunjukkan titik data yang sama seperti plot (plot4) diatas tetapi diwarnai dengan label cluster yang ditetapkan setelah pengelompokan dengan menggunakan K-Means. Terdapat juga cluster center yang akan memahami untuk melihar nilai rata-rata fitur (temperature) untuk setiap cluster.")
    st.subheader("1. untuk n=2")
    st.markdown("Terdapat dua cluster yang berbeda dalam data.")
    st.markdown("- Cluster 0  memiliki temperature rendah dan total sewa rendah, yang mana dapat mewakilkan musim dingin dan musim semi.")
    st.markdown("- Cluster 1  memiliki temperature tinggi dan total sewa tinggi, yang mana dapat mewakilkan musim panas dan musim gugur.")
    st.markdown("- Semakin tinggi nilai temperature (suhu) semakin tinggi pula total sewa bike-sharingnya.")

    st.subheader("2. untuk n=3")
    st.markdown("Terdapat 3 cluster yang berbeda dalam data.")
    st.markdown("- cluster 0 memiliki temperature sedang dengan total sewa sedang")
    st.markdown("- cluster 1 memiliki temperature tinggi dengan sewa tertinggi")
    st.markdown("- cluster 2 memiliki temperature rendah dengan sewa terendah")

    st.subheader("3. untuk n=4")
    st.markdown("Terdapat 4 cluster yang berbeda dalam data")
    st.markdown("- cluster 0 memiliki suhu agak rendah dengan sewa agak rendah, cluster ini mewakili musim semi")
    st.markdown("- cluster 1 memiliki suhu tinggi dengan jumlah sewa yang tertinggi, cluster ini mewakili musim panas (summer)")
    st.markdown("- cluster 2 memiliki suhu rendah dengan sewa terendah, cluster ini mewakili musim dingin")
    st.markdown("- cluster 3 memiliki suhu sedang dengan jumlah sewa sedang, cluster ini mewakili musim gugur")
    
    st.caption('Copyright © Tasya Nadila')

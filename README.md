# Proyek-Analisis-Data
Proyek Analisis Data Dicoding Academy

### cara menjalankan dashboard
```
conda create --name main-ds python=3.9 
conda activate main-ds 
pip install -r requirements.txt 
```

```
cd Proyek-Analisis-Data
streamlit run Dashboard/dashboard.py
```

### Run streamlit
```
streamlit run dashboard.py 
```

### Data overview
link dataset: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/code <br/>
Bike-sharing system adalah generasi baru dari persewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan kembali lagi ke posisi lain

### Ringkasan Dataset
Kedua data `day.csv` dan `hour.csv` memiliki attribut seperti dibawah ini, kecuali attribut `hr (hour)` yang hanya ada di data `hour.csv` dan tidak ada di data `day.csv`. Dibawah ini merupakan attribut dari data bike_hour_df.csv (dataframe dari hour.csv) yang telah di proses:
	
- `instant`: record index
- `date`: date
- `season` : season (1:springer, 2:summer, 3:fall, 4:winter)
- `year`: year (0: 2011, 1:2012)
- `month`: month ( 1 to 12)
- `hour`: hour (0 to 23)
- `holiday`: whether the day is a holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
- `weekday`: day of the week
- `workingday`: if the day is neither weekend nor holiday is 1, otherwise is 0.
+ `weathersit` : 
- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- `temperature`: Normalized temperature in Celsius. The values are divided into 41 (max)
	- `atemp`: Normalized feeling temperature in Celsius. The values are divided into 50 (max)
	- `humidity`: Normalized humidity. The values are divided into 100 (max)
	- `windspeed`: Normalized wind speed. The values are divided into 67 (max)
	- `casual_count`: count of casual users
	- `registered_count`: count of registered users
	- `Total_count`: count of total rental bikes including both casual and registered



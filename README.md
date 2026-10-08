# Traffic Congestion Prediction - Web Application

## Deskripsi Proyek
Aplikasi web interaktif untuk memprediksi tingkat kemacetan lalu lintas secara real-time. Proyek ini mengintegrasikan model Machine Learning Random Forest yang telah dilatih di [repo model](https://github.com/ShintaRaudita/model-prediksi-lalu-lintas) ke dalam antarmuka berbasis web menggunakan kerangka kerja Flask, memudahkan pengguna atau pihak terkait dalam menganalisis kondisi kepadatan jalan berdasarkan parameter input tertentu.

## Fitur Utama
- **Antarmuka Web Responsif:** Halaman input data yang intuitif dan mudah digunakan dengan tema visual lalu lintas yang modern.
- **Prediksi Real-Time:** Integrasi langsung dengan backend Flask untuk inferensi model seketika setelah formulir dikirim.
- **Pipeline Data Input Otomatis:** Input dari formulir diproses secara otomatis melalui `scaler.joblib` sebelum dilakukan prediksi oleh `best_rf_model.joblib`.
- **Tampilan Hasil Prediksi:** Menampilkan kategori tingkat kemacetan yang jelas dan mudah dipahami oleh pengguna.

## Teknologi yang Digunakan
- **Backend:** Python, Flask
- **Machine Learning Integration:** Scikit-Learn, Joblib, NumPy
- **Frontend:** HTML5, CSS3, Jinja2 Template Engine
- **Assets:** Custom styling (`style.css`), dynamic background (`bg.jpg`)

## Struktur Berkas
```text
├── app.py                # Server backend Flask & routing endpoint prediksi
├── best_rf_model.joblib  # Model Random Forest yang digunakan untuk inferensi
├── scaler.joblib         # File scaler untuk standarisasi input fitur
├── templates/
│   └── index.html        # Template antarmuka web (formulir & hasil)
├── static/
│   ├── style.css         # Styling halaman web
│   └── bg.jpg            # Aset visual latar belakang
└── README.md             # Dokumentasi repositori

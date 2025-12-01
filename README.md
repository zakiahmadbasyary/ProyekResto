# 🍽️ Proyek Resto — Aplikasi Pemesanan Restoran Berbasis Web (Flask)

Proyek Resto adalah aplikasi pemesanan restoran sederhana berbasis web menggunakan **Python Flask** dan **MySQL**.  
Aplikasi ini menyediakan fitur pemesanan oleh pengguna, serta dashboard bagi admin untuk mengelola meja, pesanan, dan memonitor aktivitas restoran.

---

## 🚀 Fitur Aplikasi

### 👤 **Admin**
- Login & Logout dengan session
- Dashboard admin
- Melihat daftar seluruh pemesanan
- Mengubah status meja (Kosong / Terisi)
- Melihat detail pemesanan + cetak struk
- Menghapus pemesanan
- Mengosongkan meja setelah pemesanan dihapus

### 🧑‍🍳 **Pengguna**
- Melakukan pemesanan (input nama, nomor HP, meja, menu)
- Mengirim data pemesanan ke database

### 🗄️ **Database MySQL**
- Tabel `admin`  
- Tabel `meja`  
- Tabel `produk`  
- Tabel `pemesanan`  

Struktur database mengikuti relasi dasar restoran.

---

## 🛠️ Teknologi yang Digunakan

- **Python 3**
- **Flask** (Blueprint, session, template engine)
- **MySQL / MariaDB**
- **Jinja2 Template**
- **Bootstrap / HTML / CSS** (UI)
- **pdoc** (opsional dokumentasi)

---

## 📁 Struktur Folder
```bash
ProyekResto/
│
├── app/
│ ├── database.py # Koneksi database
│ ├── init.py # Factory app & konfigurasi
│ │
│ ├── models/
│ │ ├── admin_model.py
│ │ ├── meja_model.py
│ │ └── pemesanan_model.py
│ │
│ ├── routes/
│ │  ├── admin_routes.py
│ │  ├── main_routes.py
│ │
│ └── templates/ # File HTML
│
├── docs/  # documentation pdocs
│ ├── models
│ ├── routes
│ └── search.js
│
├── run.py 
├── venv/ (opsional)
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalasi & Setup

### 1️⃣ Clone repository
```bash
git clone https://github.com/zakiahmadbasyary/ProyekResto
cd ProyekResto
```

### 2️⃣ Buat environment Python (opsional tapi disarankan)
```bash
python -m venv venv
source venv/bin/activate       # Mac / Linux
venv\Scripts\activate          # Windows
```

### 3️⃣ Instal semua dependency
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Database MySQL
```bash
CREATE DATABASE resto;
```

jika menggunakan local database
```bash
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DATABASE'] = 'resto'
```

### ▶️ Cara Menjalankan Aplikasi
```bash
python run.py
akses : http://localhost:5000
```

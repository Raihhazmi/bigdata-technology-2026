# 🚀 Bigdata Project

**Praktikum Big Data Technology**  
Prodi Teknologi Informasi – UIN Antasari  
Lecturer: Muhayat, M.IT

---

## 📋 Deskripsi

Project ini merupakan implementasi praktikum pertama mata kuliah **Big Data Technology**, yang membangun fondasi lingkungan kerja Data Engineer modern menggunakan stack industri.

---

## 🛠️ Technology Stack

| Teknologi | Versi | Fungsi |
|-----------|-------|--------|
| Python | 3.10 | Bahasa pemrograman utama |
| PySpark | 3.5.3 | Distributed data processing |
| MongoDB Atlas | M0 Free | Cloud NoSQL database |
| Git & GitHub | - | Version control |
| Java (Temurin) | 17 | Runtime untuk Spark |
| VS Code | - | Code editor |

---

## 📁 Struktur Project

```
bigdata-project/
│
├── data/               # Dataset lokal
├── cloud_storage/      # Simulasi cloud storage
├── scripts/            # Python scripts
│   ├── simple_job.py   # Spark job sederhana
│   └── test_mongo.py   # Test koneksi MongoDB
├── notebooks/          # Jupyter notebooks
├── reports/            # Laporan dan output
├── requirements.txt    # Dependency Python
└── README.md           # Dokumentasi project
```

---

## ⚙️ Setup Environment

### 1. Clone Repository
```bash
git clone https://github.com/username/bigdata-project.git
cd bigdata-project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables (Windows PowerShell)
```powershell
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.18.8-hotspot"
$env:PYSPARK_PYTHON = "C:\Users\...\Python310\python.exe"
$env:PYSPARK_DRIVER_PYTHON = "C:\Users\...\Python310\python.exe"
```

---

## ▶️ Menjalankan Spark Job

```bash
python scripts/simple_job.py
```

**Output yang diharapkan:**
```
+--------+----------+
|category|sum(value)|
+--------+----------+
|       A|        40|
|       B|        20|
+--------+----------+
```

---

## 🍃 Koneksi MongoDB Atlas

1. Buat cluster gratis di [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Salin connection string
3. Paste ke `scripts/test_mongo.py`
4. Jalankan:
```bash
python scripts/test_mongo.py
```

---

## 📦 Requirements

```
pyspark==3.5.3
pymongo
```

---

## 👤 Author

| Nama | NIM |
|Muhammad Raihan Azmi|230104040079|


---

## 📄 License

MIT License – bebas digunakan untuk keperluan akademik.

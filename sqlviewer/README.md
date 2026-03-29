# SQL Viewer (Django + MySQL)

Aplikasi Django sederhana untuk dijalankan di localhost dan menampilkan data dari MySQL.

## 1) Persiapan

```bash
cd sqlviewer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## 2) Setup database MySQL

Buat database:

```sql
CREATE DATABASE django_sqlviewer CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 3) Jalankan migrasi dan buat admin

```bash
export $(cat .env | xargs)
python manage.py migrate
python manage.py createsuperuser
```

## 4) Menjalankan aplikasi localhost

```bash
python manage.py runserver 127.0.0.1:8000
```

Buka:
- Halaman data: http://127.0.0.1:8000/
- Admin Django: http://127.0.0.1:8000/admin/

## 5) Tambah data contoh

Masuk ke admin, lalu tambahkan beberapa data `Product`. Data akan tampil di halaman utama.

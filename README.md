# Clinic Management System

Clinic Management System adalah aplikasi web berbasis Flask yang dirancang untuk membantu proses operasional klinik, mulai dari pendaftaran pasien, pengelolaan antrian, pemeriksaan dokter, resep obat, inventori obat, rekam medis, audit log, hingga pengelolaan user dan role.

## 1. Main Features

### Authentication and Role Access
- Login multi-role.
- Role user terdiri dari:
  - Admin
  - Doctor
  - Receptionist
- Setiap role memiliki hak akses berbeda.
- Admin dapat mengelola user.
- User yang sedang login tidak dapat menghapus akunnya sendiri atau mengubah role sendiri.

### Patient Management
- Menambahkan data pasien.
- Mencari data pasien.
- Nomor rekam medis otomatis.
- Tombol pembuatan antrian dari data pasien.
- Tombol rekam medis untuk admin dan dokter.

### Queue Management
- Jenis antrian:
  - Emergency
  - Appointment
  - Walk-in
- Prioritas antrian:
  1. Emergency
  2. Appointment
  3. Walk-in
- Monitor antrian untuk layar klinik.
- Auto refresh monitor antrian.
- Status antrian:
  - Waiting
  - Serving
  - Done

### Doctor Examination
- Dokter dapat melihat daftar pasien menunggu.
- Dokter dapat memanggil pasien.
- Dokter dapat mengisi diagnosis dan catatan pemeriksaan.
- Dokter dapat membuat resep obat.

### Prescription and Stock Reduction
- Dokter dapat memilih obat dan jumlah resep.
- Stok obat otomatis berkurang setelah pemeriksaan disimpan.
- Sistem menolak resep jika stok tidak mencukupi.

### Inventory and Stock Opname
- Menambahkan data obat.
- Mengubah data obat.
- Mencari dan memfilter obat.
- Stock opname untuk stok masuk dan stok keluar.
- Badge status stok:
  - Aman
  - Stok Rendah
  - Habis

### Medical Record History
- Admin dan dokter dapat melihat riwayat rekam medis pasien.
- Riwayat menampilkan:
  - Diagnosis
  - Catatan pemeriksaan
  - Dokter pemeriksa
  - Resep obat
  - Waktu kunjungan

### Audit Log
- Sistem mencatat aktivitas POST, PUT, PATCH, dan DELETE.
- Audit log menampilkan:
  - User
  - Role
  - Action
  - Module
  - IP Address
  - User Agent
  - Timestamp

### Security Features
- Password hashing.
- Role-based access control.
- Session timeout.
- Security headers.
- Simple rate limiting.
- IP restriction configuration.
- Anti-copy script.
- Custom error page 403, 404, dan 500.

## 2. Technology Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Bootstrap 5
- Jinja2
- Pytest

## 3. Project Structure

```text
clinic-management-system/
├── clinic_app/
│   ├── blueprints/
│   │   ├── auth/
│   │   ├── patients/
│   │   ├── queue/
│   │   ├── doctor/
│   │   ├── inventory/
│   │   ├── audit/
│   │   └── users/
│   ├── models/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── security.py
├── tests/
├── config.py
├── run.py
├── wsgi.py
├── requirements.txt
└── README.md
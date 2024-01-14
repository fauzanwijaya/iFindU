![ifindu](https://github.com/fauzanwijaya/iFindU/assets/139438257/83b1c7bb-4e67-493d-8cfb-9938a251cafb)

# iFindU (Instagram Follower Insight & Discovery Utility)

## Deskripsi
iFindU adalah skrip Python yang memanfaatkan API Instagram untuk mengidentifikasi non-followers - pengguna yang Anda ikuti namun tidak mengikuti Anda kembali. Alat ini menggunakan session cookie dari akun Instagram Anda untuk akses, memungkinkan pemindaian akurat dan efisien.

## Fitur
- **Identifikasi Non-Followers**: Mengetahui siapa saja yang tidak mengikuti Anda kembali.
- **Daftar Terorganisir**: Menampilkan non-followers dalam format yang mudah dibaca.
- **Penggunaan Session Cookie**: Akses menggunakan session cookie untuk keamanan dan privasi.

## Persyaratan
- Python 3
- Modul Python: `requests`, `json`, `time`, `sys`, `colorama`

## Instalasi
Clone repositori ini menggunakan git:
```
git clone https://github.com/fauzanwijaya/ifindu.git
cd ifindu
```

## Cara Penggunaan
### Langkah 1: Ambil Session Cookie dan User ID
Session cookie diperlukan untuk akses ke akun Instagram Anda. Anda bisa mendapatkan cookie ini dari browser saat login ke Instagram. Cookie yang diperlukan adalah sessionid.

Cara Mendapatkan Session Cookie dan User ID:
1. Buka Instagram di browser Anda dan login ke akun Anda.
2. Buka DevTools (biasanya dengan menekan F12 atau Ctrl+Shift+I).
3. Pergi ke tab 'Application', lalu pilih 'Cookies' pada sidebar.
4. Cari cookie dengan nama 'sessionid', dan salin nilainya.
5. User ID Anda adalah angka di awal session cookie. Misalnya, jika cookie Anda adalah 123456789:AbCdEfGhIjKlMnOpQrStUvWxYz:5:..., maka User ID Anda adalah 123456789.

### Langkah 2: Siapkan Skrip
Buka file ifindu.py. Isi variabel session_cookie dengan session cookie yang telah Anda salin, dan user_id dengan ID pengguna Instagram Anda.
![image](https://github.com/fauzanwijaya/iFindU/assets/139438257/fa9c7ee5-ea91-4c61-bfc4-4083010ee033)

### Langkah 3: Jalankan Skrip
Jalankan skrip Anda menggunakan Python. Pastikan Anda berada di direktori yang sama dengan file skrip.
```
python ifindu.py
```
Skrip akan menampilkan daftar pengguna yang tidak mengikuti Anda kembali.


Gesture Tangan Menggunakan MediaPipe
Program ini digunakan untuk mengenali gesture tangan dan menampilkan huruf berdasarkan posisi tangan di depan kamera. Dibangun menggunakan MediaPipe dan OpenCV, program ini dapat mendeteksi gesture secara real-time.

Fitur
Mengenali huruf A-Z dari gesture tangan.
Menampilkan huruf yang dikenali di layar.
Mendukung deteksi hingga dua tangan sekaligus.
Cara Instalasi dan Penggunaan
Clone Repository
Clone repository ini ke komputer kamu:

bash
Copy code
https://github.com/Dodikz/Gesture-Recognition.git
cd gesture-recognition
Instalasi Dependensi
Pastikan kamu sudah menginstal Python. Setelah itu, instal dependensi yang diperlukan:

bash
Copy code
pip install -r requirements.txt
Jika file requirements.txt belum ada, tambahkan secara manual dengan isi berikut:

Copy code
opencv-python
mediapipe
Jalankan Program
Eksekusi script untuk memulai pengenalan gesture:

bash
Copy code
python hand_gesture_recognition.py
Cara Menggunakan

Pastikan kamera terhubung dan aktif.
Arahkan tanganmu ke kamera dan buat gesture sesuai huruf.
Huruf yang dikenali akan muncul di layar.
Tekan q untuk keluar dari program.
Catatan
Pastikan pencahayaan cukup untuk hasil deteksi yang optimal.
Program ini dirancang untuk mengenali gesture tertentu, jadi pastikan gesture sesuai dengan yang telah didefinisikan.
Lisensi
Project ini bebas digunakan untuk keperluan pribadi atau edukasi. Jangan lupa mencantumkan credit jika ingin memodifikasi atau menyebarkannya.

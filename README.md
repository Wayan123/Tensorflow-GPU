Ini untuk versi Windows 10

Cara menginstall tensorflow GPU pada laptop atau komputer yang memiliki GPU Nvidia tidak begitu susah.

Ada beberapa tahap untuk menjalankan tensorflow GPU di komputer atau laptop yang ada GPU-nya.
1. Install anaconda
2. Dari conda prompt sheel kita buat environment "conda create --name 'yourenv' python=3.6"
   Dalam perintah pembuatan environment tersebut kita menambahkan beberapa kode install, yaitu nama env (misalnya tf2-gpu) dan python versi 3.6 atau versi atas lainnya.
3. Setelah proses 2 selesai, lanjut install tensorflow-nya dengan mengetik kode pakai pip "pip install tensorflow-gpu==2.3.0", 
   Note: tensorflow-gpu versi 2.0.0, 2.1.0, 2.2.0, dan 2.3.0 menggunakan CUDA 10 dan cuDNN 7.6, sedangkan versi tensorflow-gpu==2.4.0 menggunakan CUDA 11 dan cuDNN          8. Selengkapnya dapat dibaca di web tensorflow-nya langsung https://www.tensorflow.org/install/source_windows#gpu
   Cek tensorflow release di https://github.com/tensorflow/tensorflow/releases dan di https://github.com/tensorflow/tensorflow/releases
4. Reboot terdahulu laptop/komputer anda.
5. Buka python melalui Anaconda promptshell lalu ketik "import tensorflow as tf", lalu enter
6. Jika ada error open dynamic cudart64_101.dll, download dahulu di link berikut https://www.dll-files.com/cudart64_101.dll.html, lalu extract dan simpan di C:// ->    User -> NameUser -> Anaconda3 -> envs -> yourenv -> Libarry -> bin (paste disini)
7. Jika tidak ada error lagi dan dynamic open berhasil, tinggal tes code GPU test di repo ini.
8. Link install lebih lengkap dapat dibaca di https://warstek.com/tensorflowgpu/

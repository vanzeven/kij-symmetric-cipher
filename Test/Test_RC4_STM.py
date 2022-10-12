import sys 
import time
import os
import inspect

from Writer import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir) 
sys.path.insert(0, parentdir)

from Algo_Operations.RC4_STM import RC4_STM
# Runtime loop dan avearge per iteration
# Loop 100 kali
# plaintext size = 64 char
# key 8 byte
# IV 8 byte

writer = Writer()
writer.insert_to_array(0, "encrypt")
counter = 1

ciphertext=None
total_time = 0
for i in range(10):
    start_time = time.time()
    for loop in range(1000):
        encryptor = RC4_STM(key = b'sapisapi',iv = b'47433474')
        ciphertext = encryptor.encrypt(b'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 256)
    interval_time = (time.time() - start_time)
    print("Waktu interval ke-%d adalah %s detik" % (i,interval_time))
    writer.insert_to_array(counter, interval_time)
    counter += 1
    total_time += interval_time

average_time = total_time/10

print("Waktu rata-rata enkripsi adalah %s detik" % average_time )

writer.insert_to_array(counter, average_time)
writer.write_csv("RC4_STM.csv")
writer.insert_to_array(0, "decrypt")
counter = 1

plaintext=None
total_time = 0
for i in range(10):
    start_time = time.time()
    for loop in range(1000):
        encryptor = RC4_STM(key = b'sapisapi',iv = b'47433474')
        plaintext = encryptor.decrypt(ciphertext)
        #print(encryptor.encrypt(b'aaaa'))
    interval_time = (time.time() - start_time)
    print("Waktu interval ke-%d adalah %s detik" % (i,interval_time))
    writer.insert_to_array(counter, interval_time)
    counter += 1
    total_time += interval_time

average_time = total_time/10

print("Waktu rata-rata dekripsi adalah %s detik" % average_time )

writer.insert_to_array(counter, average_time)
writer.write_csv("RC4_STM.csv")
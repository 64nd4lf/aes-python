# aes-pythpn
This project implements AES encryption and evaluates encryption and decryption performance.
Language used: Python
Packages installed: PyCrypto version 2.6.1
OS used: Kali Linux

File descriptions:

plaintext.txt - contains the default plaintext, "Welcome to data security and privacy." in it
result.txt - Contains the decrypted message (human-readable)
ciphertext.txt - Contains the encrypted message in hex
iv.txt - contains the randomly generated IV in hex
key.txt - Contains the key in hex
aes.py - Simulates AES encryption in CBC mode
comparison.py - performs encryption in both CBC and ECB modes, twice each and prints the ciphertext
enc_time_measure.py - contains only encryption block from the original aes.py program with timers surrounding the encryption statements that measure time taken to encrypt
dec_time_measure.py - contains only decryption block from the original aes.py program with timers surrounding the decryption statements that measure time taken to decrypt


How to use:

1. Encryption
python aes.py enc /path/to/key.txt /path/to/plaintext.txt /path/to/ciphertext.txt
2. Decryption
python aes.py dec /path/to/key.txt /path/to/ciphertext.txt /path/to/result.txt
3. KeyGen
python aes.py keygen /path/to/key.txt

Example runs:

To encrypt
root@kali:~/Documents/aes_12499347/src# python aes.py enc ../data/key.txt ../data/plaintext.txt ../data/ciphertext.txt
f19e6f43c500e40a28d4279a9585aeaa4b501e1097698b79473a72f8e84a45b56337d5670a2038f0658ed729af0622fb022bdc1a03e6a4f7db418fac3a6bf1d7
root@kali:~/Documents/aes_12499347/src#

To decrypt
root@kali:~/Documents/aes_12499347/src# python aes.py dec ../data/key.txt ../data/ciphertext.txt ../data/result.txt
Welcome to data security and privacy.

root@kali:~/Documents/aes_12499347/src#

KeyGen
root@kali:~/Documents/aes_12499347/src# python aes.py keygen ../data/key.txt
5fde2521cc500a039c4bcf0f2d05182a5a4b5400ba214b85351d775dc02bd614
root@kali:~/Documents/aes_12499347/src#

Encryption modes comparison and time measuring exercises:

To compare the ciphertexts in both modes, run
python comparison.py ../data/key.txt ../data/plaintext.txt ../data/result.txt

To measure the encryption time, run
python enc_time_measure.py ../data/key.txt ../data/plaintext.txt ../data/ciphertext.txt

To measure the encryption time, run
python dec_time_measure.py dec ../data/key.txt ../data/ciphertext.txt ../data/result.txt

Example runs:

Comparison:

root@kali:~/Documents/aes_12499347/src# python comparison.py ../data/key.txt ../data/plaintext.txt ../data/result.txt
CBC encryption:
cd2b1db0c2a12d4326449bd97e98e27ca92a9a24208b8fb55e5a5f3f56d642417ad0c3e49cdaff92d68472eee86aec3dcfab69f8ec64c56a66c74988ea8aa6b3
ef15779ad9295315effe207cb42a548519e376e060cfe1ac5c9f5b5658ac0ae444306a3b8cf589e2ede44fc8e474893653be5eb2142c9dbcae5383fa17e6aec2
ECB encryption:
4f55c51225c2f456b5a8fdf9a2dedd186341aa9a86197fecd52e4c38a2d641c7642682b4a5ebf93fa013d213968898c9
4f55c51225c2f456b5a8fdf9a2dedd186341aa9a86197fecd52e4c38a2d641c7642682b4a5ebf93fa013d213968898c9
root@kali:~/Documents/aes_12499347/src#

Run time measurement:

1. Encryption run 3 times:
root@kali:~/Documents/aes_12499347/src# python enc_time_measure.py ../data/key.txt ../data/plaintext.txt ../data/ciphertext.txt
0.00134897232056
root@kali:~/Documents/aes_12499347/src# python enc_time_measure.py ../data/key.txt ../data/plaintext.txt ../data/ciphertext.txt
0.000990152359009
root@kali:~/Documents/aes_12499347/src# python enc_time_measure.py ../data/key.txt ../data/plaintext.txt ../data/ciphertext.txt
0.00173902511597
root@kali:~/Documents/aes_12499347/src#

2. Decryption run 3 times:
root@kali:~/Documents/aes_12499347/src# python dec_time_measure.py ../data/key.txt ../data/ciphertext.txt ../data/result.txt
0.000586986541748
root@kali:~/Documents/aes_12499347/src# python dec_time_measure.py ../data/key.txt ../data/ciphertext.txt ../data/result.txt
0.000380992889404
root@kali:~/Documents/aes_12499347/src# python dec_time_measure.py ../data/key.txt ../data/ciphertext.txt ../data/result.txt
0.000341176986694
root@kali:~/Documents/aes_12499347/src#

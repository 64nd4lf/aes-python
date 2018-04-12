import os
import binascii
import hashlib
import sys
import timeit

from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def main(argv):
	start = timeit.default_timer()

	# load the key file
	f = open(argv[1], 'r')
	key = f.read()
	key = binascii.unhexlify(key)
	f.close()
	# load the plaintext file
	f = open(argv[2], 'r')
	message = f.read()
	f.close()

	padded_message = pad(message)
	iv = Random.new().read(AES.block_size)
	f = open('../data/iv.txt', 'w')
	f.write(binascii.hexlify(iv))
	f.close()
	cipher = AES.new(key, AES.MODE_CBC, iv)
	ciphered_message = binascii.hexlify(iv + cipher.encrypt(padded_message))

	f = open(argv[3], 'w')
	f.write(ciphered_message)
	f.close()

	stop = timeit.default_timer()
	print(stop - start)

# validates minimum number of arguments
if(len(sys.argv)<3):
	print("Error: Invalid arguments")
main(sys.argv)
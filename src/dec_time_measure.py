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
	# load the ciphertext file
	f = open(argv[2], 'r')
	ciph = f.read()
	f.close()
	# load the iv file
	f = open('../data/iv.txt', 'r')
	iv = f.read()
	iv = binascii.unhexlify(iv)
	f.close()

	decoded_ciph = binascii.unhexlify(ciph)
	message = AES.new(key, AES.MODE_CBC, iv )
	unpadded_message = unpad(message.decrypt( decoded_ciph[16:] )).decode('utf-8')
	
	#print(unpadded_message)
	f = open(argv[3], 'w')
	f.write(unpadded_message)
	f.close()
	stop = timeit.default_timer()
	print(stop - start)

# validates minimum number of arguments
if(len(sys.argv)<3):
	print("Error: Invalid arguments")
main(sys.argv)
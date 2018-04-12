import os
import binascii
import hashlib
import sys

from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# fixed key for both modes of encryption
key = binascii.unhexlify('fdd0a98d53f60d9d85ab8d71d8437dfd80283de2f98ccbd11f5656ad896252af')

def main(argv):
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
	
	#running encryption in CBC mode twice
	print("CBC encryption:")
	for i in range(2):
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		ciphered_message = binascii.hexlify(iv + cipher.encrypt(padded_message))
		print (ciphered_message)

	# running encryption in ECB twice
	print ("ECB encryption:")
	for i in range(2):
		cipher = AES.new(key, AES.MODE_ECB)
		ciphered_message = binascii.hexlify(cipher.encrypt(padded_message))
		print(ciphered_message)


# validates minimum number of arguments
if(len(sys.argv)<2):
	print("Error: Invalid arguments")
main(sys.argv)
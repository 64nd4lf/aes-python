import os
import binascii
import hashlib
import sys

#PyCrypto package libraries
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16

# Padding for encryption and decryption. The value we encrypt must be a multiple of BLOCK_SIZE.
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def main(argv):
	# program enters the following segment if the enc command is used.
	if(argv[1] == "enc"):
		# load the key file
		f = open(argv[2], 'r')
		key = f.read()
		key = binascii.unhexlify(key)
		f.close()
		# load the plaintext file
		f = open(argv[3], 'r')
		message = f.read()
		f.close()

		padded_message = pad(message) #padding plaintext
		iv = Random.new().read(AES.block_size) # generating IV randomly
		f = open('../data/iv.txt', 'w') # saving IV to a file
		f.write(binascii.hexlify(iv))
		f.close()
		cipher = AES.new(key, AES.MODE_CBC, iv)
		ciphered_message = binascii.hexlify(iv + cipher.encrypt(padded_message)) # getting encrypted message in hex
		print (ciphered_message)

		f = open(argv[4], 'w') # saving the ciphered text in hex to a file
		f.write(ciphered_message)
		f.close()

	# program enters the following segement if dec command is used
	elif(argv[1] == "dec"):
		# load the key file
		f = open(argv[2], 'r')
		key = f.read()
		key = binascii.unhexlify(key)
		f.close()
		# load the ciphertext file
		f = open(argv[3], 'r')
		ciph = f.read()
		f.close()
		# load the iv file
		f = open('../data/iv.txt', 'r')
		iv = f.read()
		iv = binascii.unhexlify(iv)
		f.close()

		decoded_ciph = binascii.unhexlify(ciph) # decoding from hex
		message = AES.new(key, AES.MODE_CBC, iv )
		unpadded_message = unpad(message.decrypt( decoded_ciph[16:] )).decode('utf-8') #unpadding the deciphered messaged (the first 16 bytes contain IV so the data after first 16 is to be decrypted)
		
		print(unpadded_message)
		f = open(argv[4], 'w') # saving the decrypted message to a file
		f.write(unpadded_message)
		f.close()

	# program enters the following segment if keygen is used
	elif(argv[1] == "keygen"):
		r_key = binascii.hexlify(os.urandom(32)) # geberating a random 32 bytes or 256 bit key
		key = hashlib.sha256(r_key.encode('utf-8')).hexdigest() #saving it in hex
		print(key)
		# write the generated key into a file
		f = open(argv[2], 'w')
		f.write(key)
		f.close()

	else:
		print ("Error: Use enc or dec or keygen")

# validates minimum number of arguments
if(len(sys.argv)<2):
	print("Error: Invalid arguments")
main(sys.argv)

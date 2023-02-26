import hashlib

with open("dictionary.txt", "r") as my_file:
	numbr = my_file.read().split()
	
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
    
    
for x in numbr:
	if (correct_pw_hash == hash_pw(x)):
		print(x)



import hashlib

correct_pw_hash = open('level3.hash.bin', 'rb').read()

pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


for x in pos_pw_list:
	if (correct_pw_hash == hash_pw(x)):
		print(x)

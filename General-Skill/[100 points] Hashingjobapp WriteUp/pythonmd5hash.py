import hashlib

a = input('Nhap chuoi: ')
result = hashlib.md5(a.encode())


print("Chuoi hash md5: " + result.hexdigest())

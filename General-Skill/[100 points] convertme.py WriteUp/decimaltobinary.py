def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
# Driver code
if __name__ == '__main__':
	a = input("Nhap so vao: ")
	print(decimalToBinary(int(a)))

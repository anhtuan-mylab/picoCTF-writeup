import binascii

with open("whitepages.txt", "rb") as bin_file:
    data = bin_file.read()
    data = data.replace(b'\xe2\x80\x83', b'0')
    data = data.replace(b'\x20', b'1')
    data = data.decode("ascii")
    print("Noi dung binary : \n" + data)
    
    binary_int = int(data, 2)
    byte_number = binary_int.bit_length() + 7 // 8    
    binary_array = binary_int.to_bytes(byte_number, "big")   
    ascii_text = binary_array.decode()
    
    
    print("\nNoi dung ascii : " + ascii_text)
    
    
    

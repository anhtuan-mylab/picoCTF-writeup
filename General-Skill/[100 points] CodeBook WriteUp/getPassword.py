codebook = open('codebook.txt', 'r').read()

password = codebook[4] + codebook[14] + codebook[13] + codebook[14] + codebook[23]+ codebook[25] + codebook[16] + codebook[0] + codebook[25]

print(password);

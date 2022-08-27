
UnEncodeedMesage = input("Text: ")
CipherShift = input("Ciper Shift: ")

ASCII_values = []
for character in UnEncodeedMesage:
    ASCII_values.append(ord(character))

for i in range(len(ASCII_values)):
    ASCII_values[i] += int(CipherShift)

fin = ''.join(chr(i) for i in ASCII_values)
print(fin)
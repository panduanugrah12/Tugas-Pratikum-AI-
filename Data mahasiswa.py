nama = input('masukkan nama : ')
nim = int(input('masukkan nim : '))
prodi = input('masukkan prodi : ')
ipk = float(input('masukkan ipk : '))

print("====DATA MAHASISWA====")
print("NAMA : ", nama.upper()) #membuat huruf output dari kecil menjadi huruf besar
print("NIM : ", nim)
print("PRODI : ", prodi.lower())
print("Nilai Ipk : ", ipk)

if ipk >= 4.0:
    grade = 'A'
elif ipk >= 3.0:
    grade = 'B'
elif ipk >= 2.0:
    grade = 'C'
elif ipk >= 1.0:
    grade = 'D'
else:
    grade = 'E'
    
print('Grade : ', grade)









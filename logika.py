# function
def tampilan():
    print('Pilih Angka Untuk Melakukan Operasi Logika')
    print('1. And ')
    print('2. Or ')
    print('3. Not ')
    print('(selesai = apabila operasi sudah selesai)')

def logicAnd(p,q):
    nilaiAnd = p and q
    return nilaiAnd

def logicOr(p,q):
    nilaiOr = p or q
    return nilaiOr

def logicNot(p):
    nilaiNot = not p
    return nilaiNot

def operasiLogika(input_validasi):

    if input_validasi not in ['1', '2', '3']:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 'selesai'.")
        return

    if input_validasi == '3':
        p = input('Masukkan nilai [True / False]: ').lower()
        if p not in ['true', 'false']:
            print("Masukan tidak valid. Harap masukkan 'True' atau 'False'.")
            return
        p = p == 'true'
        print(f'Hasil Logika NOT {p} Adalah = ', logicNot(p))
        
    else:
        p = input('Masukkan nilai P [True / False]: ').lower()
        q = input('Masukkan nilai Q [True / False]: ').lower()
        if p not in ['true', 'false'] or q not in ['true', 'false']:
            print("Masukan tidak valid. Harap masukkan 'True' atau 'False'.")
            return
        p = p == 'true'
        q = q == 'true'
        if input_validasi == '1':
            print(f'Hasil Logika P AND Q Adalah = ', logicAnd(p,q))
        else:
            print(f'Hasil Logika P OR Q Adalah = ', logicOr(p,q))



print('-------Logika Dasar-------')
while True:
    tampilan()
    input_validasi = str(input('Masukan Nilai Operasi [ 1 | 2 | 3 | selesai ]: '))
    if input_validasi == 'selesai':
        print('Terimakasi Sudah Mencoba')
        break
    operasiLogika(input_validasi)
    validasi = str(input('Apakah Anda Ingin Melanjutkan ? [Y/N] : '))
    if validasi.upper() == 'Y':
        continue
    else:
        print('Terimakasih Telah mencoba')
        exit()
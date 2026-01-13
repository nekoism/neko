import random

welcome_message = ' Welcome bro '
lokasi_air = random.randint(1,4)

print ('*****************')
print (f'**{welcome_message}**')
print ('*****************')

nama = input('masukkan nama anda : ')

print (f'''
       
hallo {nama} selamat datang di mini game!!! 
lihat ke empat gelas berikut!!! 

       |   | |   | |   | |   |
       |_1_| |_2_| |_3_| |_4_|
       
       ''')

while True:
    pilihan_user = int(input('''silahkan pilih di gelas nomer berapa yang berisi air? 1/2/3/4 : '''))
    print()
    konfirmasi = input('Apakah kamu yakin dengan pilihanmu? Yes/No : ')
    
    if konfirmasi == 'Yes':
        break
    elif konfirmasi == 'No':
        continue
    else:
        print ('''
Pilih jawaban antara Yes/No dan lihat huruf besar dan kecilnya!!!
''')
        
print()
if pilihan_user == lokasi_air :
    print (f'SELAMAT KAMU MENANG!!! gelas yang berisi air berada di no : {lokasi_air} sedangkan pilihanmu adalah gelas no : {pilihan_user}')
        
elif pilihan_user > 4 :
    print (f'KOCAK!!! Cuman sampe 4 BOSSS!!! Jawaban yang benar ialah di gelas no : {lokasi_air}')
        
    
else :
    print (f'Kamu kalah!!! gelas yang berisi air beradaada di no : {lokasi_air} sedangkan pilihanmu adalah gelas no : {pilihan_user}')
        

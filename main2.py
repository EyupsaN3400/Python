

#print(dir(sys))
#komut yardım

#-sys.stderr.write("Bu Bir Uyarı")
#hata mesajı

#-sys.stderr.flush()

#sys.stdout.write("bu bir çıktı mesajıdır")
#çıktı mesajı

#toplam = 0
#while True:
#    sayi = input("bir sayı giriniz : ")
#    if(sayi.isnumeric()==False):
#        print("sayı dışında karekter girdiniz sistemden çıklıyor...")
#        sys.exit()
#    else:
#        toplam+=int(sayi)
#        print("girilen sayıların toplamı: ",toplam)

#dir(sys)
#print(dir)
#modülün içinde hangi nitelik ve fonksiyonların olduğunu görmek için

#sys.platform
#print(sys.platform)

#sys.version
#print(sys.version)
#versiyon gorme py

#print(sys.copyright)
#telif hakkı .x

#ver = sys.getwindowsversion()
#dir(ver)


import sys

#sayı = input('0 Dan Büyük Sayı gir: ')

#if int(sayı) > 0:
#    print('çıkılıyor..')
#    sys.exit
#else:
#    print(sayı)


#print(sys.argv)
#program çalıştırılırken kullanılan parametreleri bir liste halinde tutar

def çık():
    print('çıkılıyor...')
    sys.exit()
if len(sys.argv) < 2:
    print('gerekli parametreleri girmediniz!')
    çık()
elif len(sys.argv) > 2:
    print('çok fazla parametre girdiniz!')
    çık()
elif sys.argv[1] in ['-v', '-v']:
    print('program sürümü: 0.8')
else:
    mesaj = 'girdiğiniz parametre ({}) anlaşılmadı!'
    print(mesaj.format(sys.argv[1]))
    çık()
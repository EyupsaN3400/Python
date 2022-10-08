

from random import choice, choice, choices
import time
sayilar=([1,2,3,4,5,6,7,8,9,])   

sifre=str(input("bulunacak şifreyi gir:"))
sifres=""
adım=0
baslangıczamanı=time.time()
while True : 
    print(sifres,"sifresi deneniyor...")
    
    if sifre==sifres:
        
        break
    
    else:
        sifres=""
        for i in range(5):
            sifres+=str(choice(sayilar))
            adım+=1
            
            
bitiszamani=time.time() 
gecenzaman=bitiszamani-baslangıczamanı          
print("  \n \n  \n \n           Şifreniz başarıyla bulunmuştur!!! \n       sifeniz :",sifres,"/  ",adım,"adımda","\n  ",bitiszamani," sürede bulunmuştur...\n \n  \n \n")
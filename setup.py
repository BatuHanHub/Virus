#Gerekli Kütüphaneler eklendi.
import os
import time
import shutil # Windows'un erişime izin verme sorununu çözmek için

def yukleniyor():
    sayac = 0
    while sayac < 20:
        print("YÜKLENİYOR LÜTFEN BEKLEYİNİZ.")
        time.sleep(0.1)
        os.system("cls")
        print("YÜKLENİYOR LÜTFEN BEKLEYİNİZ..")
        time.sleep(0.1)
        os.system("cls")
        print("YÜKLENİYOR LÜTFEN BEKLEYİNİZ...")
        time.sleep(0.1)
        os.system("cls")
        sayac =sayac+1

print("\t\tHOŞGELDİNİZ\nProgram dosyaları hazırlanıyor birazdan yüklenmeye başlar.")

time.sleep(5)

yukleniyor()

kullaniciAdi = os.environ["USERPROFILE"] # Windows kullanıcı adı değişkene aktarıldı.

shutil.move("program.exe",f"{kullaniciAdi}\OneDrive\Masaüstü") # program masaüstüne taşındı

print("Program yüklendi.\n\n\a") # /a ses çıkarır 

input("Çıkmak için bir tuşa basınız...")

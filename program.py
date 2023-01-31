import os

sayac = 0
sayi = 1

kullaniciAdi = os.environ["USERPROFILE"] # Windows kullanıcı adı değişkene aktarıldı.
os.chdir(f'{kullaniciAdi}\OneDrive\Masaüstü\\') # Program dosya yolunu masaüstüne değiştirdi  

while True:
    dosya = open(f"Silemezsin {sayi}.txt", "w")
    dosya.write("Sil bakalım silebilirsen :)")
    dosya.close()
    
    sayi = sayi+1 

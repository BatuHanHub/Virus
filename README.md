# İndirmeden Önce Oku!
# Programın amacı 
Program kullanıcıdan habersiz (aynı virüsler gibi)
dosya oluşturması sonucu bilgisayarının donmasını sağlamak. Şaka amaçlı program. 

# Programın çalışma mantığı
## "Kurulum"
Programın klasöründe birsürü boş dosya bulunmakta. Bu da şüphe çekmemek için yapılmış işlevsiz klasörler.
Program "setup" dosyası gibi gözükerek kullanıcı kendini uygulama kurduğunu zannetmesi sağlanıyor. Virüs gereksiz klasörlerin birinden program.exe olarak masaüstüne getirir.

## Program
Kullanıcı programı çalıştırdığında birsürü .txt dosyası oluşturur. Bu da bilgisayarının donmasına kasmasına sebep olur (yani en azından benim bilgisayarımda öyle oldu 😄).

# Gelebilecek Sorunlar Ve Çözümleri
## Masaüstüm boş ve hiçbirşey yapamıyorum?
- Win+R yaparak çalıştırı açınız.
- Çıkan pencereye `explorer.exe` yazınız.
- Masaüstü klasörüne geliniz.
- Tüm '.txt' dosyalarını siliniz.
## Programı nasıl kapatırım?
- Bilgisayarınız donmadıysa Programı görev yöneticisinden (task manager)dan kapatın.
- Bilgisayarınız donduysa Win+R yaparak çalıştırı açın
- Çıkan pencere `taskmgr.exe` yazınız.
- Programın bulun ve sağ tık yaparak görevini sonlandırın.
- Bilgisayarınızı yeniden başlatın.
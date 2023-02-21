from tkinter import *
from tkinter import messagebox

# GUİ programlama konusunda yeniyim ve çok az tecrubem var bu yüzden baya kötü olabilir :) ama geliştireceğim

soz = 'Benim naçiz vücudum elbet bir gün toprak olacaktır, ancak Türkiye Cumhuriyeti ilelebet payidar kalacaktır.'

def evet():
    pencere.destroy() # Pencere yok edildi
  
def hayir():
    sayac = 1
    hazir = messagebox.askyesno('Soru','Programı kapatayim mi?')
    if hazir == True:    
        messagebox.showerror('Mesaj', soz)
        pencere.destroy()
        while True:
            dosya = open(f"Atatürk {sayac}.txt", "w", encoding='utf8')
            dosya.write("Ne Mutlu Türk'üm Diyene -Atatürk \n\nYerinde olsam Atatürk'ü severdim :) ama bu yolu sen istedin...")
            dosya.close()
            sayac += 1
    else:
        HaHaHa = messagebox.showinfo(':(','Tamam.')
        if HaHaHa == 'ok':
            pencere.destroy()
            while True:
                dosya = open(f"Atatürk {sayac}.txt", "w", encoding='utf8')
                dosya.write("Ne Mutlu Türk'üm Diyene -Atatürk \n\nYerinde olsam Atatürk'ü severdim :) ama bu yolu sen istedin...")
                dosya.close()
                sayac += 1

pencere = Tk() # Pencere değişkeninde pencere oluşturuyorum 
pencere.title('Atatürk') # Pencere başlığı

pencere.attributes('-fullscreen', True) # Pencere tam ekranda açılacak

# Yazı yazıyorum ve pencerede göstertiyorum
Label (pencere, font=('arial 70 bold'),text="Atatürk'ü seviyor musun?").pack()

# Çerçeve oluşturuyorum (Çerçeveye çokta gerek yok ama ben yaptım) - Çerçevenin içine butonlarımı yerleştireceğim
butonCerceve1 = Frame(pencere,bg='red',width=200,height=70)
butonCerceve1.place(relx=0.6,rely=0.8)

butonCerceve2 = Frame(pencere,bg='red',width=200,height=70)
butonCerceve2.place(relx=0.1,rely=0.8)

# Butonlarımı oluşturuyorum ve kişiselleştiriyorum
butonEvet = Button(butonCerceve1,text='Seviyorum',font=('arial 50 bold italic'),bg='red',fg='white',command=evet,
                    activebackground='white',activeforeground='red').pack()

butonHayir = Button(butonCerceve2,text='Sevmiyorum',font=('arial 50 bold italic'),bg='white',fg='red',command=hayir,
                    activebackground='red',activeforeground='white').pack()

pencere.mainloop() # Pencere değişkeni içerisindeki GUI hemen kapanmaması için döngüye sokuyorum

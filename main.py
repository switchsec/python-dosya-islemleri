import os 
import time
from os import system
#Uygulama Bilgileri
uygDev = "Developer : Switchsec"
uygİsim = "Dosya İşlemleri"
uygSürüm = "Astalavista"
uygKomutlar = (f'Uygulama Bilgileri \n\t{uygDev} \n\t Uygulama İsmi : {uygİsim} \n\t Sürüm : {uygSürüm} \n\n Komutlar : \n\t klasör aç = Klasör oluşturur \n\t dosya aç = Dosya oluşturur \n\t klasör degis = Klasör ismini değiştirme \n\t klasör kapat = Dosya kapatma \n\t klasör sil = Klasör siler \n\t dosya sil = Dosya siler')
#Uygulama Yazıları
class klasörler:
    print(uygKomutlar)
    time.sleep(2)
    system("cls")
    time.sleep(1)
    print(uygİsim)
    def giris(isim):
        if isim == "Görkem":
            print(f'Hoşgeldin {isim} ')
            time.sleep(1)
            deger = 1
            while (deger==1):
                komutGir = input("Ne yapmak istersin : ")
                if komutGir == "klasörac" or komutGir == "klasör aç":
                    os.mkdir(input("Klasör Adı Giriniz : ")) 
                    print("")
                    print("Klasör başarıyla oluşturuldu")
                elif komutGir == "dosyaac" or komutGir == "dosya aç":
                    print("Dosya isimlerini")
                    f = open(input("Dosya İsmi Giriniz "), "x")
                    print("")
                    print("Dosya başarıyla oluşturuldu")
                elif komutGir == "klasör degis" or komutGir == "klasördegis":
                    os.rename(input("Değiştirilecek olan klasörün ismini giriniz : "),input("Yeni klasör ismi giriniz : "))
                    os.listdir()
                    print("")
                    print("Klasör ismi başarıyla değiştirildi")
                elif komutGir == "klasörkapat" or komutGir == "klasör kapat":
                    dosya = open(input("Dosya konumunu giriniz : "))
                    dosya.close()
                    print("")
                    print("Dosya kapandı")
                elif komutGir == "dosyasil" or komutGir == "dosya sil":
                    if os.path.exists(input("Dosya konumunu giriniz : ")):
                        os.remove("demofile.txt")
                        print("")
                        print("Dosya başarıyla silindi")
                    else:
                        print("Dosya mevcut değil")
                elif komutGir == "klasörsil" or komutGir == "klasör sil":
                    os.rmdir(input("Klasör Konumunu Görünüz : "))
                    print("")
                    print("Klasör başarıyla silindi")
                else : 
                    print("Sistemimde böyle bir komut bulunmuyor ")
                    system("cls")

        else : 
            print("Sana verilen isim ile gir ! ")
            system("cls")
    giris(input("İsim Giriniz : "))
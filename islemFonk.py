import sqlite3
db = sqlite3.connect("servis.sqlite")
imlec =db.cursor()


def ogrenciEkle():
    ogrenciAdi =input("Öğrenci Adı: ")
    Soyadi= input("Öğrenci Soyadı:  ")
    Semt = input("Öğrenci Semti:  ")
    imlec.execute("insert into Ogrenciler(ogrenciAdi,Soyadi,Semt) Values(?,?,?)",(ogrenciAdi,Soyadi,Semt))
    db.commit()
    print("Öğrenci Ekleme Başarılı")
    print("Ana Menüye Dönmek için Enter'a Basın!")
    input()
def OgrenciListe():
    ogrenciAdi =input("Öğrenci Adı Giriniz: ")
    sorgu = "select * from Ogrenciler where ogrenciAdi='{}'".format(ogrenciAdi)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
            #print(i)
            print("Aradağınız Öğrenci {}".format(i))
            print("Ana Menüye Dönmek için Enter'a Basın!")
            input()


def OgrenciOdeme():
    ogrenciAdi = input("Öğrenci Adı: ")
    Soyadi = input("Öğrenci Soyadı: ")
    Semt = input("Öğrenci Semti: ")
    Fiyat =int(input("Güzergah Fiyatı:"))
    Taksitmi =input("Taksit Yapılsın mı?-E/H: ")
    if Taksitmi == "e" or "E":
        taksitsayisi = int(input("Taksit sayısı Girin: "))
        #Fiyat /= taksitsayisi
        Taksit = Fiyat / taksitsayisi
        print("Taksit Yapıldı.")
        TaksitD = input("Aylık Taksit Tutarı: {}".format(Taksit))
    else:
        print("Hepsi Ödendi Tutar. {}".format(Taksitmi))
    Durum = input("Öğrenci Aktif Kullanıcı mı?-E/H: ")
    if Durum == "e" or "E":
        print("Öğrencimiz {} Durumu Aktiftir.".format(ogrenciAdi))
    else:
        print("Öğrencimiz {} Durumu Aktiftir.".format(ogrenciAdi))
    imlec.execute("insert into Odeme(ogrenciAdi,Soyadi,Semt,Fiyat,Durum,Taksit) Values(?,?,?,?,?,?)", (ogrenciAdi,Soyadi,Semt,Fiyat,Durum,Taksit))
    db.commit()
    print("Öğrencimiz {} Ödeme Planı Hazırlama  Başarılı".format(ogrenciAdi))
    print("Ana Menüye Dönmek için Enter'a Basın!")
    input()
def OdemeList():
    ogrenciAdi =input("Öğrenci Adı Giriniz: ")
    sorgu = "select * from Odeme where ogrenciAdi='{}'".format(ogrenciAdi)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
            #print(i)
            print("Aradağınız Öğrenci {} ".format(i))
            print("Ana Menüye Dönmek için Enter'a Basın!")
            input()



def OgrenciSil():
    ogrenciAdi = input("Öğrenci Adı Giriniz: ")
    imlec.execute("Delete from Ogrenciler  where ogrenciAdi=? ",[ogrenciAdi])
    db.commit()
    print("Öğrenci {} başarıyla silindi.".format(ogrenciAdi))
    print("Ana Menüye Dönmek için Enter'a Basın!")
    input()
def OdemeGun():
    ogrenciAdi =input("Öğrenci Adı Giriniz:")
    Taksit = int(input("Taksit Ödemesi Giriniz"))
    imlec.execute("update odeme set Taksit=? where ogrenciAdi=?",(Taksit,ogrenciAdi))
    db.commit()
    print("Öğrenci {} taksit ödemesi güncellendi.".format(ogrenciAdi))
    print("Ana Menüye Dönmek için Enter'a Basın!")
    input()









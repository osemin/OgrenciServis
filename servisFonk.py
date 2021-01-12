import sqlite3
db = sqlite3.connect("servis.sqlite")
imlec =db.cursor()

imlec =db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS Ogrenciler (ogrenciAdi,Soyadi,Semt)")
imlec.execute("CREATE TABLE IF NOT EXISTS Odeme (ogrenciAdi,Soyadi,Semt,Fiyat,Durum,Taksit)")
db.commit()
db.close()


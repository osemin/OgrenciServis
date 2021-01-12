import os
import sqlite3
import servisFonk
import islemFonk
import time







def main():
    while True:
        os.system("cls")
        print("""
        [1] Öğrenci Ekle
        [2] Öğrenci Listele
        [3] Öğrenci Ödemesi Al
        [4] Öğrenci Sil
        [5] Öğrenci Ödeme Listele
        [6] Öğrenci Ödeme Güncelle
        [Q] Çıkış
        """)
        secim = input("İşleminizi Seçin : ")

        if secim == "1":
            islemFonk.ogrenciEkle()
        elif secim == "2":
            islemFonk.OgrenciListe()
        elif secim == "3":
            islemFonk.OgrenciOdeme()
        elif secim == "4":
            islemFonk.OgrenciSil()
        elif secim == "5":
            islemFonk.OdemeList()
        elif secim == "6":
            islemFonk.OdemeGun()








main()
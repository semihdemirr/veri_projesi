import sqlite3

# 1. BAGLANTI: 'sirket.db' adinda bir kasa (dosya) olustur veya varsa baglan
baglanti = sqlite3.connect("sirket.db")

# 2. IMLEC (CURSOR): Veritabaninda islem yapacak yetkili memur
imlec = baglanti.cursor()

# 3. TABLO OLUSTUR (SQL KOMUTU)
# Eger 'personel' adinda bir tablo yoksa olustur.
# Sutunlar: id (kimlik no), isim (yazi), departman (yazi), maas (sayi)
imlec.execute("""
    CREATE TABLE IF NOT EXISTS personel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT,
        departman TEXT,
        maas INTEGER
    )
""")

# 4. VERI EKLE (SQL KOMUTU: INSERT)
# Kasaya 3 tane eleman ekleyelim
imlec.execute("INSERT INTO personel (isim, departman, maas) VALUES ('Ahmet', 'IK', 30000)")
imlec.execute("INSERT INTO personel (isim, departman, maas) VALUES ('Mehmet', 'IT', 45000)")
imlec.execute("INSERT INTO personel (isim, departman, maas) VALUES ('Zeynep', 'IT', 42000)")
imlec.execute("INSERT INTO personel (isim, departman, maas) VALUES ('Semih', 'Yonetim', 75000)")

# 5. KAYDET VE KAPAT
baglanti.commit()  # Degisiklikleri onayla (Mühürle)
baglanti.close()   # Baglantiyi kes

print("Veritabani kuruldu ve veriler eklendi! 🚀")

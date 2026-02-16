import sqlite3
import pandas as pd

# 1. Kasanin Kapisini Cal (Baglan)
baglanti = sqlite3.connect("sirket.db")

# 2. SQL Emrini Ver ve Pandas'a Yukle
# read_sql_query: SQL sorgusunu calistir, gelen cevabi DataFrame yap.
df = pd.read_sql_query("SELECT * FROM personel", baglanti)

# 3. Kapiyi Kapat
baglanti.close()

# 4. Sonucu Goster
print("--- VERITABANINDAN GELEN TABLO ---")
print(df)

# BONUS: Sadece IT departmanini cekmek isteseydik?
# SQL: SELECT * FROM personel WHERE departman = 'IT'

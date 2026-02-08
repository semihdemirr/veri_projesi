import pandas as pd

# 1. Dosyayi Oku (Excel dosyasini acmak gibi)
df = pd.read_csv("calisanlar.csv")

# 2. Bilgileri Goster
print("--- DOSYA BASARIYLA OKUNDU ---")
print(df)

# 3. Yeni Bir Analiz Yapalim:
# Maas 40.000'den buyuk olanlari bulalim
zenginler = df[df['Maas'] > 40000]

print("\n--- MAASI 40.000 TL USTU OLANLAR ---")
print(zenginler)

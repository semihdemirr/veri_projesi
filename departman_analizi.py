import pandas as pd

# 1. Dosyayi Oku
df = pd.read_csv("calisanlar.csv")

# 2. Departmanlara Gore Grupla ve Maaslari Topla
# Mantik: Tabloyu al -> Departmana gore grupla -> Sadece Maas sutununa bak -> Topla (.sum)
bolum_ozeti = df.groupby('Departman')['Maas'].sum()

print("--- DEPARTMAN BAZLI TOPLAM MAASLAR ---")
print(bolum_ozeti)

# 3. BONUS: En cok maas odeyen departmani bulalim
en_pahali = bolum_ozeti.idxmax()  # idxmax: En buyuk sayinin ismini (etiketini) verir
en_yuksek_tutar = bolum_ozeti.max()

print("\n--- SAMPIYON DEPARTMAN ---")
print(f"En cok harcama yapan: {en_pahali} ({en_yuksek_tutar} TL)")

import pandas as pd
import matplotlib.pyplot as plt  # Ressami cagiriyoruz, adi 'plt' olsun

# 1. Veriyi Oku
df = pd.read_csv("calisanlar.csv")

# 2. Veriyi Hazirla (Grupla)
bolum_ozeti = df.groupby('Departman')['Maas'].sum()

# 3. Cizim Emrini Ver
# kind='bar' -> Cubuk grafik olsun (bar chart)
# color='skyblue' -> Rengi gokyuzu mavisi olsun
bolum_ozeti.plot(kind='bar', color='skyblue')

# 4. Grafigi Susle
plt.title("Departmanlara Gore Toplam Maaslar")  # Baslik
plt.xlabel("Departmanlar")                      # Alt yazi
plt.ylabel("Toplam Maas (TL)")                  # Yan yazi

# 5. Ekrana degil, DOSYAYA kaydet
plt.savefig("maas_grafigi.png")

print("Ressam isini bitirdi! 'maas_grafigi.png' dosyasi olusturuldu.")

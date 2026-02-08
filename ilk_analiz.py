import pandas as pd
# 1. Veriyi Sözlük Olarak Hazırla ( Excel satirlari gibi)
veri = {
    'Isim' : ['Ahmet' , 'Mehmet' , 'Zeynep' , 'Elif' , 'Semih' ],
    'Yas'  : [25, 30, 28, 22, 35],
    'Departman' : ['IK' , 'IT' , 'IT' , 'Pazarlama' , 'Yonetim'],
    'Maas' : [30000, 45000, 42000, 32000, 75000]
}

# 2. Pandas ile  Tabloyu Cevir (DataFrame)
df = pd.DataFrame(veri)

# 3. Ekrana Yazdir
print("--- SIRKET CALISAN LISTESI ---")
print(df)

print("\n-- IT DEPARTMANI ORTALAMA MAAS ---")
# Sadece IT departmani sec ve ortalamasini al
it_maas = df[df['Departman'] == 'IT' ]['Maas'].mean ()
print(it_maas)

# Veriyi dosya olarak kaydet
df.to_csv("calisanlar.csv", index=False)
print("\nDosya basariyla kaydedildi: calisanlar.csv")

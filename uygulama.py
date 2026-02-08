import streamlit as st
import pandas as pd

# 1. Baslik ve Aciklama
st.title("📊 Semih'in Veri Analiz Paneli")
st.write("Bu uygulama Python ve Streamlit kullanilarak hazirlandi.")

# 2. Veriyi Oku
df = pd.read_csv("calisanlar.csv")

# 3. Sol Tarafa Ayar Menusu Koyalim (Sidebar)
st.sidebar.header("Filtrele")
secilen_departman = st.sidebar.selectbox("Departman Seciniz:", df["Departman"].unique())

# 4. Filtreleme Yapalim
suzum_veri = df[df["Departman"] == secilen_departman]

# 5. Ekrana Yazdiralim
st.subheader(f"{secilen_departman} Departmani Calisanlari")
st.dataframe(suzum_veri)

# 6. Grafigi Canli Cizelim
st.subheader("Departman Maas Dagilimi")
# Butun departmanlarin toplam maasini hesaplayalim
genel_ozet = df.groupby("Departman")["Maas"].sum()
st.bar_chart(genel_ozet)

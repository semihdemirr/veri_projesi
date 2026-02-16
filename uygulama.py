import streamlit as st
import pandas as pd
import sqlite3

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Semih'in IK Paneli", layout="wide")

# --- FONKSIYON: VERILERI GETIR (SQL FILTRELI) ---
def verileri_getir(min_maas):
    conn = sqlite3.connect("sirket.db")
    # BURASI ONEMLI: SQL 'WHERE' komutu ile filtreleme yapiyoruz
    sorgu = f"SELECT * FROM personel WHERE maas >= {min_maas}"
    df = pd.read_sql_query(sorgu, conn)
    conn.close()
    return df

# --- FONKSIYON: YENI PERSONEL EKLE ---
def personel_ekle(isim, dept, maas):
    conn = sqlite3.connect("sirket.db")
    imlec = conn.cursor()
    imlec.execute("INSERT INTO personel (isim, departman, maas) VALUES (?, ?, ?)", (isim, dept, maas))
    conn.commit()
    conn.close()

# --- ANA BASLIK ---
st.title("📂 Şirket Veritabanı Yönetim Paneli")

# 1. SOL MENU (SIDEBAR)
st.sidebar.header("🔍 Filtreleme")
# Maas Filtresi (Slider)
secilen_min_maas = st.sidebar.slider("Minimum Maaş Limiti", 0, 100000, 0, step=1000)

st.sidebar.divider() # Cizgi

st.sidebar.header("➕ Yeni Personel Ekle")
yeni_isim = st.sidebar.text_input("Ad Soyad")
yeni_dept = st.sidebar.selectbox("Departman", ["IK", "IT", "Yonetim", "Pazarlama", "Satis"])
yeni_maas = st.sidebar.number_input("Maaş", min_value=17002, step=1000)

if st.sidebar.button("Kaydet"):
    personel_ekle(yeni_isim, yeni_dept, yeni_maas)
    st.sidebar.success(f"{yeni_isim} başarıyla eklendi!")
    st.rerun()

# 2. ANA EKRAN
# Verileri filtreye gore cekiyoruz
df = verileri_getir(secilen_min_maas)

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📋 Personel Listesi ({len(df)} Kişi)")
    st.dataframe(df)

with col2:
    st.subheader("💰 Departman Bütçeleri")
    if not df.empty:
        ozet = df.groupby("departman")["maas"].sum()
        st.bar_chart(ozet)
    else:
        st.warning("Bu kriterlere uygun veri bulunamadı.")

# 3. YEDEKLEME BUTONU (CSV INDIR)
st.divider()
st.subheader("📥 Veri Yedekleme")

# Veriyi CSV formatina cevir
csv_dosyasi = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📊 Güncel Listeyi İndir (CSV)",
    data=csv_dosyasi,
    file_name="personel_listesi.csv",
    mime="text/csv",
)

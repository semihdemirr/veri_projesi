import streamlit as st
import pandas as pd
import sqlite3

# --- AYARLAR ---
st.set_page_config(page_title="Semih'in IK Paneli", layout="wide")

# --- FONKSIYON: VERILERI GETIR ---
def verileri_getir():
    conn = sqlite3.connect("sirket.db")
    df = pd.read_sql_query("SELECT * FROM personel", conn)
    conn.close()
    return df

# --- FONKSIYON: YENI PERSONEL EKLE ---
def personel_ekle(isim, dept, maas):
    conn = sqlite3.connect("sirket.db")
    imlec = conn.cursor()
    imlec.execute("INSERT INTO personel (isim, departman, maas) VALUES (?, ?, ?)", (isim, dept, maas))
    conn.commit()
    conn.close()

# --- ANA SAYFA ---
st.title("📂 Şirket Veritabanı Yönetim Paneli")

# 1. SOL MENU: PERSONEL EKLEME FORMU
st.sidebar.header("➕ Yeni Personel Ekle")
yeni_isim = st.sidebar.text_input("Ad Soyad")
yeni_dept = st.sidebar.selectbox("Departman", ["IK", "IT", "Yonetim", "Pazarlama", "Satis"])
yeni_maas = st.sidebar.number_input("Maaş", min_value=17002, step=1000)

if st.sidebar.button("Kaydet"):
    personel_ekle(yeni_isim, yeni_dept, yeni_maas)
    st.sidebar.success(f"{yeni_isim} başarıyla eklendi!")
    # Sayfayi yenile ki tablo guncellensin (Bu onemli!)
    st.rerun()

# 2. ANA EKRAN: TABLO VE GRAFIK
df = verileri_getir()

col1, col2 = st.columns(2) # Ekrani ikiye bol

with col1:
    st.subheader("📋 Personel Listesi")
    st.dataframe(df)

with col2:
    st.subheader("💰 Departman Bütçeleri")
    ozet = df.groupby("departman")["maas"].sum()
    st.bar_chart(ozet)

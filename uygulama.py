import streamlit as st
import pandas as pd
import sqlite3

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Semih'in IK Paneli", layout="wide")

# --- 2. FONKSİYONLAR ---
def verileri_getir(min_maas):
    conn = sqlite3.connect("sirket.db")
    sorgu = f"SELECT * FROM personel WHERE maas >= {min_maas}"
    df = pd.read_sql_query(sorgu, conn)
    conn.close()
    return df

def personel_ekle(isim, dept, maas):
    conn = sqlite3.connect("sirket.db")
    imlec = conn.cursor()
    imlec.execute("INSERT INTO personel (isim, departman, maas) VALUES (?, ?, ?)", (isim, dept, maas))
    conn.commit()
    conn.close()

# --- 3. SOL MENÜ (SIDEBAR) ---
# Önce filtreyi oluşturuyoruz ki veriyi ona göre çekebilelim
st.sidebar.title("👮‍♂️ Semih'in Operasyon Merkezi")

st.sidebar.header("🔍 Filtreleme")
secilen_min_maas = st.sidebar.slider("Minimum Maaş Limiti", 0, 100000, 0, step=1000)

st.sidebar.divider()

st.sidebar.header("➕ Yeni Personel Ekle")
yeni_isim = st.sidebar.text_input("Ad Soyad")
yeni_dept = st.sidebar.selectbox("Departman", ["IK", "IT", "Yonetim", "Pazarlama", "Satis"])
yeni_maas = st.sidebar.number_input("Maaş", min_value=17002, step=1000)

if st.sidebar.button("Kaydet"):
    personel_ekle(yeni_isim, yeni_dept, yeni_maas)
    st.sidebar.success(f"{yeni_isim} başarıyla eklendi!")
    st.rerun()

# --- 4. ANA EKRAN VE HESAPLAMALAR ---
st.title("📂 Şirket Veritabanı Yönetim Paneli")

# KRİTİK NOKTA: Veriyi (df) BURADA çekiyoruz!
df = verileri_getir(secilen_min_maas)

# Veriyi çektikten SONRA istatistikleri hesaplıyoruz
st.markdown("---") 

col1, col2, col3 = st.columns(3)

# Hata vermemesi için boş veri kontrolü yapıyoruz
if not df.empty:
    toplam_personel = len(df)
    toplam_maas = df["maas"].sum()
    ortalama_maas = df["maas"].mean()
    
    col1.metric(label="Toplam Personel", value=f"{toplam_personel} Kişi")
    col2.metric(label="Toplam Maaş Yükü", value=f"{toplam_maas:,.0f} TL")
    col3.metric(label="Ortalama Maaş", value=f"{ortalama_maas:,.0f} TL")
else:
    col1.metric("Durum", "Veri Yok")

st.markdown("---")

# --- 5. TABLO VE GRAFİKLER ---
col_sol, col_sag = st.columns(2)

with col_sol:
    st.subheader(f"📋 Personel Listesi ({len(df)} Kişi)")
    st.dataframe(df)

with col_sag:
    st.subheader("💰 Departman Bütçeleri")
    if not df.empty:
        ozet = df.groupby("departman")["maas"].sum()
        st.bar_chart(ozet)
    else:
        st.warning("Kriterlere uygun veri yok.")

# --- 6. YEDEKLEME ---
st.divider()
csv_dosyasi = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📊 Güncel Listeyi İndir (CSV)",
    data=csv_dosyasi,
    file_name="personel_listesi.csv",
    mime="text/csv",
)

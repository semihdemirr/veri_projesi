import streamlit as st
import pandas as pd
import sqlite3

# --- PAGE CONFIGURATION (Sayfa Ayarlari) ---
st.set_page_config(page_title="Semih's HR Dashboard", layout="wide")

# --- FUNCTION: LOAD DATA (Veri Yukleme) ---
def load_data(min_salary):
    # Connect to database (Veritabanina baglan)
    conn = sqlite3.connect("sirket.db")
    
    # SQL Query (Sorgu Cumlesi)
    # "Select all columns from table where salary is greater than..."
    query = f"SELECT * FROM personel WHERE maas >= {min_salary}"
    
    # Read Query into DataFrame (Sorguyu tabloya dok)
    df = pd.read_sql_query(query, conn)
    
    conn.close()
    return df

# --- FUNCTION: ADD STAFF (Personel Ekleme) ---
def add_staff(name, department, salary):
    conn = sqlite3.connect("sirket.db")
    cursor = conn.cursor() # Cursor: Imlec (Islemi yapan)
    
    # Execute SQL Command (Komutu calistir)
    cursor.execute("INSERT INTO personel (isim, departman, maas) VALUES (?, ?, ?)", (name, department, salary))
    
    conn.commit() # Save changes (Kaydet)
    conn.close()

# --- SIDEBAR (Sol Menu) ---
st.sidebar.title("👨‍💻 Admin Panel")

# Section 1: Filter (Filtreleme)
st.sidebar.header("🔍 Filter Options")
selected_min_salary = st.sidebar.slider("Minimum Salary", 0, 100000, 0, step=1000)

st.sidebar.divider()

# Section 2: Add New Staff (Yeni Personel)
st.sidebar.header("➕ Add New Employee")
new_name = st.sidebar.text_input("Full Name")
new_dept = st.sidebar.selectbox("Department", ["IK", "IT", "Yonetim", "Pazarlama", "Satis"])
new_salary = st.sidebar.number_input("Salary", min_value=17002, step=1000)

if st.sidebar.button("Save Employee"):
    add_staff(new_name, new_dept, new_salary)
    st.sidebar.success(f"{new_name} added successfully!")
    st.rerun() # Refresh page (Sayfayi yenile)

# --- MAIN PAGE (Ana Sayfa) ---
st.title("📊 Company Data Dashboard")

# Load Data (Veriyi Cek)
# df = DataFrame (Tablo)
df = load_data(selected_min_salary)

st.markdown("---") 

# --- KPI METRICS (Anahtar Gostergeler) ---
col1, col2, col3 = st.columns(3)

if not df.empty:
    # Calculations (Hesaplamalar)
    total_staff = len(df)              # Kac satir var?
    total_salary = df["maas"].sum()    # Maas toplami
    avg_salary = df["maas"].mean()     # Maas ortalamasi
    
    # Display Metrics (Gostergeleri Bas)
    # label = Etiket (Baslik), value = Deger
    col1.metric(label="Total Staff", value=f"{total_staff} People")
    col2.metric(label="Total Salary Load", value=f"{total_salary:,.0f} TL")
    col3.metric(label="Average Salary", value=f"{avg_salary:,.0f} TL")
else:
    col1.metric("Status", "No Data Found")

st.markdown("---")

# --- DATA TABLE & CHARTS (Tablo ve Grafikler) ---
left_col, right_col = st.columns(2)

with left_col:
    st.subheader(f"📋 Employee List ({len(df)})")
    st.dataframe(df)

with right_col:
    st.subheader("💰 Budget by Department")
    if not df.empty:
        # Group data by department and sum salaries
        chart_data = df.groupby("departman")["maas"].sum()
        st.bar_chart(chart_data)
    else:
        st.warning("No data to display.")

# --- EXPORT SECTION (Yedekleme) ---
st.divider()
st.subheader("📥 Data Export")

# Convert to CSV
csv_file = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇️ Download Staff List (CSV)",
    data=csv_file,
    file_name="staff_list.csv",
    mime="text/csv",
)

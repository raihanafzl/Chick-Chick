import datetime
import urllib.parse
import streamlit as st

# 1. CONFIG HALAMAN BROWSER
st.set_page_config(
    page_title="Cafe & Mart Seblak Prasmanan",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- INJEKSI KODE CSS UNTUK TEMA MERAH & KUNING FRIED CHICKEN ---
st.markdown("""
<style>
    /* Background utama warna kuning pastel lembut */
    .stApp {
        background-color: #FFFDE7;
    }
    
    /* Background sidebar warna kuning cerah ala fried chicken (Golden Yellow) */
    [data-testid="stSidebar"] {
        background-color: #FFC107 !important;
    }
    
    /* Mengubah warna teks judul (Heading) menjadi merah */
    h1, h2, h3, h4, h5, h6 {
        color: #D32F2F !important;
    }
    
    /* Mengubah warna nilai metrik unggulan menjadi merah */
    [data-testid="stMetricValue"] {
        color: #D32F2F !important;
    }
    
    /* Modifikasi tombol biasa menjadi merah bergaris kuning */
    div.stButton > button {
        background-color: #D32F2F !important;
        color: #FFC107 !important;
        border-radius: 8px !important;
        border: 2px solid #FFC107 !important;
        font-weight: bold !important;
    }
    div.stButton > button:hover {
        background-color: #B71C1C !important;
        color: #FFE082 !important;
        border: 2px solid #FFD54F !important;
    }
    
    /* Modifikasi Link Button (tombol WhatsApp & Maps) jadi merah dengan teks kuning cerah */
    a[data-testid="baseLinkButton"] > div {
        background-color: #D32F2F !important;
        color: #FFECB3 !important;
        border: 2px solid #FFD54F !important;
        font-weight: bold !important;
    }
    a[data-testid="baseLinkButton"] > div:hover {
        background-color: #B71C1C !important;
        color: #FFFFFF !important;
    }
    
    /* Warna teks di sidebar agar kontras dan tetap jelas dibaca */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #212121 !important;
        font-weight: 500;
    }

    /* --- PERBAIKAN TOTAL WARNA KOTAK INPUT & DROPDOWN --- */
    
    /* 1. Mengubah seluruh kotak Dropdown (Selectbox) */
    div[data-baseweb="select"] > div {
        background-color: #D32F2F !important; 
        color: white !important;
        border: 2px solid #FFC107 !important;
    }
    div[data-baseweb="select"] span {
        color: white !important;
    }
    div[data-baseweb="select"] svg {
        fill: white !important;
    }
    
    /* 2. Mengubah SELURUH kotak Number Input (Background panjang + teks angka di dalamnya) */
    div[data-baseweb="spinbutton"] {
        background-color: #D32F2F !important;
        border-radius: 4px !important;
        border: 2px solid #FFC107 !important;
    }
    
    /* Memastikan elemen input angka di dalam kotak ikut berubah warna & teksnya putih */
    div[data-baseweb="spinbutton"] input {
        color: white !important;
        background-color: transparent !important;
        font-weight: bold !important;
    }

    /* 3. Mengubah Tombol Plus (+) dan Minus (-) pada Number Input */
    button[data-testid="stNumberInputStepDown"], 
    button[data-testid="stNumberInputStepUp"] {
        background-color: #B71C1C !important;
        color: white !important;
        border: none !important;
    }
    
    button[data-testid="stNumberInputStepDown"]:hover, 
    button[data-testid="stNumberInputStepUp"]:hover {
        background-color: #8E0000 !important;
        color: #FFC107 !important;
    }

    /* Menghilangkan border biru bawaan saat komponen diklik/fokus */
    div[data-baseweb="input"]:focus-within, 
    div[data-baseweb="spinbutton"]:focus-within {
        border-color: #FFC107 !important;
        box-shadow: 0 0 5px #FFC107 !important;
    }
    
</style>
""", unsafe_allow_html=True)

# --- FUNGSI CEK STATUS BUKA/TUTUP ---
now = datetime.datetime.now()
current_hour = now.hour
is_open = 8 <= current_hour < 21

# --- SIDEBAR INFORMASI CAFE ---
with st.sidebar:
    st.image(
        "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=500",
        caption="Warm & Cozy Cafe & Mart",
    )
    st.header("📍 Informasi Toko")

    # Status Toko
    if is_open:
        st.success("🟢 **TOKO BUKA** (08.00 - 21.00 WIB)")
    else:
        st.error("🔴 **TOKO TUTUP** (Buka Jam 08.00 WIB)")

    st.markdown(
        """
    **Alamat:**  
    📍 Jl. Contoh Raya No. 123 (Dekat Alun-alun)  

    **Layanan:**  
    🍽️ Makan di Tempat | 🛵 Takeaway / ShopeeFood | 📦 Belanja Mart  

    **Kontak Langsung:**  
    📞 WhatsApp: 0877-8266-0168  
    """
    )

    st.divider()
    st.markdown(
        "💡 *Tips: Pilih menu & barang belanjaanmu, hitung totalnya, lalu langsung pesan via WhatsApp!*"
    )

# --- HEADER / BANNER ---
col_logo, col_judul = st.columns([1, 5])  # Mengatur ukuran logo & teks judul

with col_logo:
    # Ganti 'logo.png' dengan nama file logomu / link URL gambar
    st.image("logo.png", width=90) 

with col_judul:
    st.title("Cafe & Mart - Seblak Prasmanan & Sembako")
    st.caption(
        "Nikmati Seblak Prasmanan, Ayam Kentucky/Geprek, Nasi Pecel, Es Coklat Segar & Belanja Kebutuhan Harian!"
    )

# --- METRIK UNGGULAN ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Menu Utama", "Seblak & Ayam")
m2.metric("Frozen Food", "Lengkap & Fresh")
m3.metric("Bumbu & Sembako", "Lengkap Dapur")
m4.metric("Layanan", "Dine-in / ShopeeFood / WA")

st.divider()

# Inisialisasi Session State Keranjang Belanja
if "cart" not in st.session_state:
    st.session_state.cart = {}

# --- KATALOG & KALKULATOR PESANAN ---
st.subheader("📋 Pilih Menu & Barang Belanjaan")

# Pilihan Tab Kategori
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🔥 Seblak Prasmanan & ShopeeFood",
        "🍗 Makanan Siap Saji",
        "🥤 Minuman Segar & Kopi",
        "🧊 Frozen Food",
        "🛒 Bumbu Masak & Sembako",
    ]
)

# TAB 1: SEBLAK PRASMANAN & PAKET SHOPEEFOOD
with tab1:
    st.write("### 🍲 Seblak Prasmanan & Paket Online")

    st.markdown("#### 🔴 Racik Seblak Prasmanan")
    st.info(
        "⚠️ **Syarat Seblak Prasmanan:** Minimal Pembelian **Rp 10.000** per porsi."
    )

    # Choice Level Pedas
    level_pedas = st.select_slider(
        "🌶️ PILIH LEVEL PEDAS SEBLAK",
        options=[
            "🤤 Level 0 - Ori",
            "🌶️ Level 1 - Sedang",
            "🌶️🌶️ Level 2 - Pedas",
            "🔥 Level 3 - Extra Pedas",
            "🔥🔥 Level 4 - Pedas Sekali",
            "🥵 Level 5 - Sangat Extra Pedas Sekali",
        ],
        value="🤤 Level 0 - Ori",
    )
    
    st.caption(
        "0️⃣ Ori  •  1️⃣ Sedang  •  2️⃣ Pedas  •  3️⃣ Extra Pedas  •  4️⃣ Pedas Sekali  •  5️⃣ Sangat Extra Pedas Sekali"
    )

    jenis_seblak = st.selectbox(
        "🍲 **Pilih Jenis Sajian:**",
        [
            "⚠️Pilih Dulu",
            "🍲 Kuah",
            "🥘 Nyemek",
        ],
    )

    tempat_validasi = st.empty()
    
    st.write("**Pilih Topping Seblak:**")
    container = st.container(height=450)
    with container:

        topping_seblak = {
            "Kerupuk Mawar": 1000,
            "Kerupuk Bunga": 1000,
            "Kerupuk Putih": 1000,
            "Kerupuk Kuning": 1000,
            "Kerupuk Bulat": 1000,
            "Kerupuk Churros": 1000,
            "Kerupuk Kerang": 1000,
            "Kerupuk Pelangi": 1000,
            "Kerupuk Petulo": 1000,
            "Kerupuk Siomay Mini": 1000,
            "Kerupuk Spiral": 1000,
            "Kerupuk Udang": 1000,
            "Kerupuk Udel": 1000,
            "Mie Kuning": 1000,
            "Toping Baso Ikan": 1000,
            "Toping Baso Sapi JJ": 1000,
            "Toping Baso Sapi Vita": 1000,
            "Toping Bentuk Ikan": 1000,
            "Toping Chikuwa": 1000,
            "Toping Cikur": 1000,
            "Toping Kaki Gurita": 1000,
            "Toping Kembang Cumi": 1000,
            "Toping SS Bambu": 1000,
            "Toping Flower Twister": 1500,
            "Toping Bola Udang": 1500,
            "Toping Naruto": 1500,
            "Toping Hati": 1500,
            "Crabstik": 2000,
            "Cuanki Lidah": 2000,
            "Kwetiau": 2000,
            "Toping Odeng": 2000,
            "Toping Cilok (isi 3)": 2000,
            "Toping Crabstik": 2000,
            "Toping Dimsum": 2000,
            "Toping Dumpling Ayam": 2000,
            "Toping Dumpling Bolognese": 2000,
            "Toping Dumpling Keju": 2000,
            "Toping Dumpling Matcha": 2000,
            "Toping Dumpling Rendang": 2000,
            "Toping Ekor Udang": 2000,
            "Toping Fish Cheese Ball": 2000,
            "Cuanki Tahu": 2500,
            "Toping Ceker Ayam": 2500,
            "Toping Baso Jumbo": 2500,
            "Telur Ayam": 3500,
        }

        total_seblak_prasmanan = 0
        topping_terpilih = []

        col1, col2, col3, col4 = st.columns(4)
        cols = [col1, col2, col3, col4]

        for i, (top, price) in enumerate(topping_seblak.items()):

            with cols[i % 4]:

                qty_top = st.number_input(
                    f"{top} (Rp {price:,})",
                    min_value=0,
                    max_value=10,
                    value=0,
                    key=f"top_{top}",
                )

                if qty_top > 0:
                    subtotal_top = qty_top * price
                    total_seblak_prasmanan += subtotal_top
                    topping_terpilih.append(f"{top} x{qty_top}")


       # --- VALIDASI KETAT & TOMBOL KONFIRMASI (DI ATAS TOPPING) ---
        if total_seblak_prasmanan > 0:
            
            # 1. Validasi Jenis Sajian Belum Dipilih (Merah)
            if jenis_seblak == "⚠️Pilih Dulu":
                tempat_validasi.error("⚠️ **Mohon pilih jenis sajian dulu** (Kuah atau Nyemek) di atas sebelum memesan!")
            
            # 2. Validasi Minimal Belanja Rp 10.000 (Kuning)
            elif total_seblak_prasmanan < 10000:
                tempat_validasi.warning(
                    f"Total Topping saat ini: **Rp {total_seblak_prasmanan:,}**. Kurang **Rp {10000 - total_seblak_prasmanan:,}** lagi untuk memenuhi syarat minimal Rp 10.000!"
                )
            
            # 3. Jika Syarat Terpenuhi: Munculkan Tombol Langsung di Atas Topping!
            else:
                with tempat_validasi.container():
                    st.success(f"✅ Total Racikan Seblak: **Rp {total_seblak_prasmanan:,}**")
                    if st.button("🛒 Masukkan Seblak Ini ke Keranjang", use_container_width=True):
                        nama_item_seblak = f"Seblak {jenis_seblak} ({level_pedas}) [{', '.join(topping_terpilih)}]"
                        
                        st.session_state.cart[nama_item_seblak] = {
                            "qty": 1,
                            "price": total_seblak_prasmanan,
                        }
                        st.success("🎉 Seblak berhasil dimasukkan ke keranjang pesanan!")
        
        else:
            tempat_validasi.info("💡 Silakan pilih minimal topping seblak senilai Rp 10.000.")

# TAB 2: MAKANAN SIAP SAJI
with tab2:
    st.write("### 🍗 Makanan Siap Saji & Olahan Ayam")
    with st.container(height=350):
        c_makan1, c_makan2 = st.columns(2)
        menu_makanan = {
            "Ayam Kentucky Crispy + Nasi": 12000,
            "Ayam Kentucky Crispy (Tanpa Nasi)": 9000,
            "Ayam Geprek Sambal Korek + Nasi": 13000,
            "Nasi Pecel Khas (Sayur + Bumbu Pecel)": 8000,
            "Nasi Pecel": 12000,
            "Ayam Ungkep C4C": 17000,
            "Kepala Ayam Ungkep C4C": 10000,
        }
        for i, (item, price) in enumerate(menu_makanan.items()):
            target_col = c_makan1 if i % 2 == 0 else c_makan2
            with target_col:
                key_name = f"input_{item}"
                # Inisialisasi awal jika belum ada
                if key_name not in st.session_state:
                    st.session_state[key_name] = 0
                
                qty = st.number_input(
                    f"{item} - Rp {price:,}", min_value=0, max_value=20, key=key_name
                )
                if qty > 0:
                    st.session_state.cart[item] = {"qty": qty, "price": price}
                elif item in st.session_state.cart and qty == 0:
                    del st.session_state.cart[item]

# TAB 3: MINUMAN SEGAR & KOPI
with tab3:
    st.write("### 🥤 Minuman Segar & Kopi")
    with st.container(height=350):
        c_minum1, c_minum2 = st.columns(2)
        menu_minuman = {
            "AQUVIVA AIR MINERAL 700ML": 3000,
            "Es Coklat Kuentel": 12000,
            "Teh Dingin/Panas": 3500,
            "Lemon Tea": 6500,
            "Black Cofee": 5000,
            "Cappucino": 10000,
            "Cappucino Aren": 12000,
            "Cappucino Caramel": 12000,
        }
        for i, (item, price) in enumerate(menu_minuman.items()):
            target_col = c_minum1 if i % 2 == 0 else c_minum2
            with target_col:
                key_name = f"input_{item}"
                if key_name not in st.session_state:
                    st.session_state[key_name] = 0
                
                qty = st.number_input(
                    f"{item} - Rp {price:,}", min_value=0, max_value=20, key=key_name
                )
                if qty > 0:
                    st.session_state.cart[item] = {"qty": qty, "price": price}
                elif item in st.session_state.cart and qty == 0:
                    del st.session_state.cart[item]

# TAB 4: FROZEN FOOD
with tab4:
    st.write("### 🧊 Stok Frozen Food Lengkap")
    with st.container(height=350):
        c_fz1, c_fz2 = st.columns(2)
        menu_frozen = {
            "888 Otak Otak": 6000,
            "AJ Siomay Putih": 12000,
            "AJ Tahu Bakso 24": 13000,
            "Bakso Sapi Premium (50 pcs)": 30000,
            "Kentang Goreng Frozen (1kg)": 28000,
            "Chikuwa & Crabstick Pouch": 18000,
            "Ayam Ungkep Frozen Pack": 35000,
        }
        for i, (item, price) in enumerate(menu_frozen.items()):
            target_col = c_fz1 if i % 2 == 0 else c_fz2
            with target_col:
                key_name = f"input_{item}"
                if key_name not in st.session_state:
                    st.session_state[key_name] = 0
                
                qty = st.number_input(
                    f"{item} - Rp {price:,}", min_value=0, max_value=10, key=key_name
                )
                if qty > 0:
                    st.session_state.cart[item] = {"qty": qty, "price": price}
                elif item in st.session_state.cart and qty == 0:
                    del st.session_state.cart[item]

# TAB 5: BUMBU MASAK & SEMBAKO
with tab5:
    st.write("### 🛒 Bumbu Dapur & Kebutuhan Rumah Tangga")
    with st.container(height=350):
        c_bumbu1, c_bumbu2 = st.columns(2)
        menu_sembako = {
            "58 Kecap Asin 135ml": 5000,
            "Ajinomoto 5000": 5000,
            "3 SAPI KRIMER 490g": 13000,
            "Delmonte Saus BBQ 250": 12500,
            "Delmonte Saus SPG 250": 12500,
            "Delmonte Saus Tomat 200": 8000,
            "Delmonte Saus Tomat 500": 12000,
            "FINNA Saus Ayam 340ml": 15000,
            "Gourmet Saus Keju 500gr": 22500,
            "INDOF Saus Tomat 135": 6000,
            "KIKKO Saus Bulgogi 300ml": 20000,
        }
        for i, (item, price) in enumerate(menu_sembako.items()):
            target_col = c_bumbu1 if i % 2 == 0 else c_bumbu2
            with target_col:
                key_name = f"input_{item}"
                if key_name not in st.session_state:
                    st.session_state[key_name] = 0
                
                qty = st.number_input(
                    f"{item} - Rp {price:,}", min_value=0, max_value=10, key=key_name
                )
                if qty > 0:
                    st.session_state.cart[item] = {"qty": qty, "price": price}
                elif item in st.session_state.cart and qty == 0:
                    del st.session_state.cart[item]

st.divider()

# --- RINGKASAN PESANAN & INTEGRASI WHATSAPP ---
st.subheader("🛒 Ringkasan Pesanan Anda")

if not st.session_state.cart:
    st.write("Belum ada item yang dipilih. Silakan pilih menu/barang di atas!")
else:
    total_bayar = 0
    pesanan_text = "Halo Kak, saya mau pesan:\n"
    
    # Kumpulkan item yang akan dihapus tanpa langsung mengubah session_state di tengah loop
    for idx, (item, detail) in enumerate(list(st.session_state.cart.items())):
        subtotal = detail["qty"] * detail["price"]
        total_bayar += subtotal
        
        col_item, col_del = st.columns([5, 1])
        
        with col_item:
            st.write(f"• **{item}** x {detail['qty']} = **Rp {subtotal:,}**")
            
        with col_del:
            if st.button("❌", key=f"btn_del_{idx}", help="Hapus menu ini"):
                # Hapus dari keranjang saja
                del st.session_state.cart[item]
                
                # Hapus key state agar widget mereset dirinya di rerun berikutnya
                key_input = f"input_{item}"
                if key_input in st.session_state:
                    del st.session_state[key_input]
                
                st.rerun()

        pesanan_text += f"- {item} ({detail['qty']}x) : Rp {subtotal:,}\n"

    pesanan_text += f"\n*Total Estimasi: Rp {total_bayar:,}*"
    st.markdown(f"### **Total Pembayaran: Rp {total_bayar:,}**")

    # Format URL WhatsApp
    encoded_text = urllib.parse.quote(pesanan_text)
    wa_url = f"https://wa.me/6287782660168?text={encoded_text}"

    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        st.link_button(
            "📲 Kirim Rincian Pesanan via WhatsApp", wa_url, type="primary", use_container_width=True
        )
        
    with col_btn2:
        if st.button("🗑️ Hapus Semua Pesanan", key="btn_clear_all", type="secondary", use_container_width=True):
            # Hapus semua input_ key dari session state
            for k in list(st.session_state.keys()):
                if k.startswith("input_"):
                    del st.session_state[k]
            
            st.session_state.cart.clear()
            st.rerun()

st.divider()
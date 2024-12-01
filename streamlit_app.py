import streamlit as st

def is_vokal(x):
    return x.lower() in ['a', 'i', 'u', 'e', 'o']

def hanacaraka(x):
    mapping = {
        "H": "R", "N": "K", "C": "D", "T": "L", "S": "M",
        "W": "G", "B": "J", "NG": "Y", "P": "NY", "R": "H",
        "K": "N", "D": "C", "L": "T", "M": "S", "G": "W",
        "J": "B", "Y": "NG", "NY": "P"
    }
    return mapping.get(x, x)

def enkripsi(x):
    cipherteks = ""
    i = 0

    while i < len(x):
        c = x[i].upper()
        s_input = c

        c_before = x[i - 1].upper() if i > 0 else ""
        c_after = x[i + 1].upper() if i < len(x) - 1 else ""

        if c.isalpha() and not is_vokal(c):
            if c_before == 'N' and c == 'Y':
                s_input = "NY"
            elif c_before == 'N' and c == 'G':
                s_input = "NG"
            elif c == 'N' and c_after == 'Y':
                s_input = "NY"
                i += 1
            elif c == 'N' and c_after == 'G':
                s_input = "NG"
                i += 1

        s_hasil = hanacaraka(s_input)
        cipherteks += s_hasil
        i += 1

    return cipherteks

# Streamlit App
st.title("Enkripsi Hanacaraka")
st.write("Masukkan pesan yang ingin dienkripsi menggunakan metode Hanacaraka.")

# Input teks dari pengguna
input_text = st.text_area("Ketikkan pesan:", "")

# Jika tombol diklik, lakukan enkripsi
if st.button("Enkripsi"):
    if input_text.strip():
        hasil = enkripsi(input_text)
        st.success("Hasil Enkripsi:")
        st.text_area("Teks Terenkripsi:", hasil, height=200)
    else:
        st.warning("Masukkan pesan terlebih dahulu!")

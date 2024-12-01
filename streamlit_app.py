import streamlit as st

def is_vokal(x):
    return x.lower() in ['a', 'i', 'u', 'e', 'o']

def hanacaraka(x):
    mapping = {
        "h": "r", "n": "k", "c": "d", "t": "l", "s": "m",
        "w": "g", "b": "j", "ng": "y", "p": "ny", "r": "h",
        "k": "n", "d": "c", "l": "t", "m": "s", "g": "w",
        "j": "b", "y": "ng", "ny": "p",
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
        c = x[i]
        s_input = c

        c_before = x[i - 1] if i > 0 else ""
        c_after = x[i + 1] if i < len(x) - 1 else ""

        if c.isalpha() and not is_vokal(c):
            if c_before.lower() == 'n' and c.lower() == 'y':
                s_input = c_before + c
            elif c_before.lower() == 'n' and c.lower() == 'g':
                s_input = c_before + c
            elif c.lower() == 'n' and c_after.lower() == 'y':
                s_input = c + c_after
                i += 1
            elif c.lower() == 'n' and c_after.lower() == 'g':
                s_input = c + c_after
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

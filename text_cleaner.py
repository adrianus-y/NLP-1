from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
from wordcloud import STOPWORDS  # Stopwords bawaan dari WordCloud


# Membuat stemmer Bahasa Indonesia
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Menggabungkan stopwords bawaan dan tambahan
def load_stopwords(custom_stopwords_path):
    # Stopwords bawaan
    default_stopwords = set(STOPWORDS)
    # Membaca stopwords tambahan dari file
    with open(custom_stopwords_path, "r", encoding="utf-8") as file:
        custom_stopwords = set(file.read().splitlines())
    # Menggabungkan stopwords
    combined_stopwords = default_stopwords.union(custom_stopwords)
    return combined_stopwords

# Fungsi untuk membersihkan teks
def clean_text(text, stopwords):
    # Menghapus angka, tanda baca, dan simbol
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Menghapus spasi ekstra
    text = re.sub(r'\s+', ' ', text).strip()
    # Mengubah teks menjadi huruf kecil
    text = text.lower()
    # Menghapus stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

# Path file stopwords tambahan
custom_stopwords_file = r"D:/stopwords-id.txt"  # Ganti dengan path file stopwords tambahan

# Path file input dan output
input_file = r"D:/JSS.txt"  # Ganti dengan path file input
output_file = r"D:/cleaned_and_stemmed_output.txt"  # Ganti dengan path file output

# Membaca daftar stopwords gabungan
stopwords = load_stopwords(custom_stopwords_file)

# Membaca file teks input
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Membersihkan teks
cleaned_text = clean_text(text, stopwords)

# Melakukan stemming
stemmed_text = stemmer.stem(cleaned_text)

# Menyimpan hasil ke file output
with open(output_file, "w", encoding="utf-8") as file:
    file.write(stemmed_text)

print(f"Proses selesai! Hasil disimpan ke '{output_file}'.")

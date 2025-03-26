from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import re

# Membaca file teks
with open(r"D:/yt-1.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Daftar stopwords bawaan WordCloud
stopwords = set(STOPWORDS)

# Stopwords tambahan, tambahkan ke set
with open(r"D:/stopwords-id.txt", "r", encoding="utf-8") as stop_file:
    custom_stopwords = set(stop_file.read().splitlines())
stopwords.update(custom_stopwords)

# Membersihkan teks dan menghapus stopwords
cleaned_text = re.findall(r'\b\w+\b', text.lower())  # Memisahkan kata-kata
filtered_words = [word for word in cleaned_text if word not in stopwords]

# Menghitung jumlah kemunculan kata
word_counts = Counter(filtered_words)

# Menampilkan 10 kata paling sering muncul
print("10 Kata Paling Sering Muncul:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")

# Membuat word cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=stopwords
).generate_from_frequencies(word_counts)

# Menampilkan word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

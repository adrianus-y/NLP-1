from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Membaca file teks
with open(r"D:/yt-1.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Daftar stopwords bawaan WordCloud
stopwords = set(STOPWORDS)

# Stopwords tambahan, tambahkan ke set
with open(r"D:/stopwords-id.txt", "r", encoding="utf-8") as stop_file:
    custom_stopwords = set(stop_file.read().splitlines())
stopwords.update(custom_stopwords)

# Membuat word cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=stopwords
).generate(text)

# Menampilkan word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

import stanza
from docx import Document
from heapq import nlargest

# Fungsi untuk membaca teks dari file Word
def extract_text_from_word(file_path):
    doc = Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()])
    return text

# Path ke file Word Anda
word_file = "<lokasi file docx>"

# Ekstrak teks dari file Word
text = extract_text_from_word(word_file)

# Memisahkan teks menjadi paragraf
paragraphs = [p.strip() for p in text.split("\n") if p.strip()]

# Memuat pipeline Stanza untuk Bahasa Indonesia
stanza.download('id')  # Unduh model Bahasa Indonesia
nlp = stanza.Pipeline('id')

# Analisis per paragraf
paragraph_analyses = []

for i, paragraph in enumerate(paragraphs, 1):
    doc = nlp(paragraph)
    sentences = [sentence.text for sentence in doc.sentences]
    
    # Algoritma sederhana untuk gagasan utama
    word_frequencies = {}
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.upos not in ['PUNCT', 'SYM']:  # Mengabaikan tanda baca dan simbol
                word_frequencies[word.text] = word_frequencies.get(word.text, 0) + 1

    if word_frequencies:
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / max_frequency)

        sentence_scores = {}
        for sentence in doc.sentences:
            sentence_text = sentence.text
            sentence_score = sum(word_frequencies.get(word.text, 0) for word in sentence.words)
            sentence_scores[sentence_text] = sentence_score

        # Ekstrak gagasan utama paragraf
        summary_sentences = nlargest(1, sentence_scores, key=sentence_scores.get)
        main_idea = " ".join(summary_sentences)
    else:
        main_idea = "Tidak ada gagasan utama yang ditemukan."

    paragraph_analyses.append((i, main_idea))

# Menampilkan hasil
for paragraph_id, main_idea in paragraph_analyses:
    print(f"Paragraf {paragraph_id}:")
    print(main_idea)
    print("-" * 50)

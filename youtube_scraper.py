import csv
from youtube_comment_downloader import YoutubeCommentDownloader

# Inisialisasi Downloader
downloader = YoutubeCommentDownloader()

# Ganti VIDEO_ID dengan ID video YouTube yang ingin Anda unduh komentarnya
video_url = 'https://www.youtube.com/watch?v=Wm-8nlEmby0'  # Masukkan URL video
comments = downloader.get_comments_from_url(video_url)

# Nama file output CSV
output_file = r'C:\Users\ivanovna\coding\Wm-8nlEmby0.csv'

# Menyimpan komentar ke file CSV
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # Header kolom
    writer.writerow(['Username', 'Comment', 'Likes', 'Time'])

    # Tulis komentar ke file CSV
    for comment in comments:
        writer.writerow([
            comment.get('author', 'Unknown'),  # Nama pengguna
            comment.get('text', ''),          # Komentar
            comment.get('likes', 0),          # Jumlah likes
            comment.get('time', '')           # Waktu komentar
        ])

print(f"Komentar berhasil disimpan ke file {output_file}")

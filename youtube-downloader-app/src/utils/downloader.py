import os
import yt_dlp

def download_video(video_url):
    try:
        # İndirme klasörü yolunu ayarla
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        download_folder = os.path.join(base_dir, "indirlen videolar")
        os.makedirs(download_folder, exist_ok=True)

        # yt-dlp seçeneklerini ayarla
        ydl_opts = {
            'format': 'best',  # En iyi kalitede video
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'progress': True
        }

        # Video bilgilerini al
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Video bilgileri alınıyor...")
            info = ydl.extract_info(video_url, download=False)
            title = info.get('title', None)
            
            print(f"Video bulundu: {title}")
            print("İndirme başlıyor...")
            
            # Videoyu indir
            ydl.download([video_url])
            
            return f"Video başarıyla indirildi: {title}"

    except Exception as e:
        error_message = str(e)
        print(f"Hata detayı: {error_message}")
        if "unavailable" in error_message.lower():
            return "Bu video kullanılamıyor veya özel bir video"
        elif "not found" in error_message.lower():
            return "Video bulunamadı"
        else:
            return f"Video indirme hatası: {error_message}"
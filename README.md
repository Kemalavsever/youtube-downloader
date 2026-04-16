# YouTube Downloader

YouTube videolarini ve ses dosyalarini indirmeye yarayan Flask tabanli web uygulamasi.

## Ozellikler

- YouTube video URL'si ile video indirme
- Basit ve kullanici dostu web arayuzu
- Flask backend ile hafif ve hizli

## Proje Yapisi

```
youtube-downloader-app/
├── src/
│   ├── app.py           # Flask uygulamasi (ana giris noktasi)
│   ├── templates/
│   │   └── index.html   # Web arayuzu
│   ├── static/
│   │   └── style.css    # Stiller
│   └── utils/
│       └── downloader.py  # Video indirme mantigi
└── requirements.txt     # Bagimliliklar
```

## Kurulum

```bash
git clone https://github.com/Kemalavsever/youtube-downloader
cd youtube-downloader/youtube-downloader-app
pip install -r requirements.txt
```

## Kullanim

```bash
python src/app.py
```

Tarayicida `http://127.0.0.1:5000` adresine gidin, YouTube linkini yapistirin ve indirin.

## Gereksinimler

```
Flask
pytube
```

## Teknolojiler

- Python 3
- Flask
- pytube

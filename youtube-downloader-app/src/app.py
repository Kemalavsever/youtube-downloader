from flask import Flask, render_template, request
from utils.downloader import download_video

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if video_url:
            message = download_video(video_url)
        else:
            message = "Lütfen bir YouTube video URL'si girin"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
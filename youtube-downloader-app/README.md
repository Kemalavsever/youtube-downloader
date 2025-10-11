# YouTube Downloader App

This project is a simple web application that allows users to download YouTube videos by providing a video link. It is built using Flask for the web framework and utilizes the `pytube` library for downloading videos.

## Project Structure

```
youtube-downloader-app
├── src
│   ├── app.py               # Main entry point of the application
│   ├── templates
│   │   └── index.html       # HTML structure for the web interface
│   ├── static
│   │   └── style.css        # CSS styles for the web interface
│   └── utils
│       └── downloader.py     # Logic for downloading videos from YouTube
├── requirements.txt          # List of dependencies for the project
└── README.md                 # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-downloader-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Enter the YouTube video link in the provided form and click the download button.

4. The video will be downloaded and saved in a folder named "indirlen videolar" within the application directory.

## Dependencies

- Flask
- pytube

## License

This project is open-source and available under the MIT License.
# World Spotify Playlists

A simple web app that allows users to search for Spotify playlists by country. It uses the **Spotify Web API** to fetch and display playlists related to the selected country.

## 🌍 Demo

[![Watch the video](https://img.youtube.com/vi/Q4kwGHZoA4Y/0.jpg)](https://youtu.be/Q4kwGHZoA4Y)


## 🎵 Features
- Search for Spotify playlists by country.
- Get a list of up to 5 relevant playlists.
- Click on the playlist links to open them in Spotify.

## 🛠️ Technologies used
- **Python** (Flask)
- **Spotify API** (Spotipy)
- **HTML/CSS** (Basic frontend)
- **Gunicorn** (for deployment)

## 🚀 How to Run locally
### 1. Clone the repository
```sh
git clone https://github.com/RominaSR/world-spotify-playlists.git
cd world-spotify-playlists
```

### 2. Create a Virtual Environment & install dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up your Spotify API credentials
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an app and get your `CLIENT_ID` and `CLIENT_SECRET`.
3. Replace the placeholders in `app.py`:
   ```python
   CLIENT_ID = "YOUR_CLIENT_ID"
   CLIENT_SECRET = "YOUR_CLIENT_SECRET"
   ```

### 4. Run the application
```sh
python app.py
```
Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## 📌 Deployment
This app is deployed on **Render**. If you want to deploy your own version:
1. Push your project to GitHub.
2. Sign up at [Render](https://render.com/).
3. Create a new **Web Service**, link your GitHub repo, and set up the build & start commands:
   ```sh
   pip install -r requirements.txt
   gunicorn app:app
   ```
4. Deploy and get your live URL!

## 📜 License
This project is open-source under the **MIT License**.


---
🚀 **Developed by [Romina Soledad Romay](https://github.com/RominaSR)**


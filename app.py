from flask import Flask, request, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# 🎵 Configuration API de Spotify
CLIENT_ID = "81cc0207023848b6904790f317bd3cff"  # Replace with your Client ID
CLIENT_SECRET = "81ddd16cbfbd4583afac0299fffa4fde"  # Replace with your  Client Secret

# 🔑 Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

app = Flask(__name__)

# 📌 Function to get playlists
def get_playlists_by_country(country_name):
    results = sp.search(q=country_name, type="playlist", limit=5)
    playlists = []

    if not results.get("playlists") or not results["playlists"].get("items"):
        return None

    for playlist in results["playlists"]["items"]:
        if playlist and "name" in playlist and "external_urls" in playlist:
            playlists.append({
                "name": playlist["name"],
                "url": playlist["external_urls"]["spotify"]
            })

    return playlists

# 🌍 Homepage
@app.route("/", methods=["GET", "POST"])
def home():
    playlists = None
    country = None

    if request.method == "POST":
        country = request.form.get("country")
        playlists = get_playlists_by_country(country)

    return render_template("index.html", country=country, playlists=playlists)

if __name__ == "__main__":
    app.run(debug=True)

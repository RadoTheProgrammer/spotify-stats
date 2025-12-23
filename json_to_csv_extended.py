import json
import pandas as pd
import matplotlib.pyplot as plt
import glob
import settings
import os

files = glob.glob(r"my_spotify_data (1)\Spotify Extended Streaming History\Streaming_History_Audio_*.json")
data={"endTime":[],"artistName":[],"trackName":[],"albumName":[],"msPlayed":[]}
for file in files:
    print(file)
    with open(file,"rb") as f:
        #text=f.read()
        input_data = json.load(f)

    
    for track in input_data:
        data["endTime"].append(track["ts"])
        data["artistName"].append(track["master_metadata_album_artist_name"])
        data["trackName"].append(track["master_metadata_track_name"])
        data["albumName"].append(track["master_metadata_album_album_name"])
        data["msPlayed"].append(track["ms_played"])

df = pd.DataFrame(data)
df.to_csv("StreamingHistory.csv", index=False)
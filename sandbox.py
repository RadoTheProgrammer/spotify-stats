"""
Identify what was trendy
date -> obj
"""


import json

with open(r"my_spotify_data\Spotify Account Data\StreamingHistory_music_0.json","rb") as f:
    #text=f.read()
    input_data = json.load(f)

data={"endTime":[],"artistName":[],"trackName":[],"timePlayed":[]}
for track in input_data:
    data["endTime"].append(track["endTime"])
    data["artistName"].append(track["artistName"])
    data["trackName"].append(track["trackName"])
    data["timePlayed"].append(track["msPlayed"])

import pandas as pd

df = pd.DataFrame(data)
df = df.astype({"endTime":"datetime64[s]"})#, "timePlayed":"timedelta64[ms]"})





df_artist = df.groupby("artistName")
df_artist_size = df_artist.size().sort_values(ascending=False)
df_artist_size.to_csv("artist_play_counts.csv")

df_track = df.groupby(["artistName", "trackName"])
df_track_size = df_track.size()
df_track_size = df_track_size.sort_values(ascending=False)
df_track_size.to_csv("track_play_counts.csv")

print(df_track_size)
for key,value in df_track:
    print(key)
    print(value)
    pass
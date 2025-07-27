import json
import pandas as pd
import matplotlib.pyplot as plt
import glob

files = glob.glob("my_spotify_data/Spotify Account Data/StreamingHistory_music_*.json")
data={"endTime":[],"artistName":[],"trackName":[],"timePlayed":[]}
for file in files:
    print(file)
    with open(file,"rb") as f:
        #text=f.read()
        input_data = json.load(f)

    
    for track in input_data:
        data["endTime"].append(track["endTime"])
        data["artistName"].append(track["artistName"])
        data["trackName"].append(track["trackName"])
        data["timePlayed"].append(track["msPlayed"])

df = pd.DataFrame(data)
df.to_csv("StreamingHistory.csv", index=False)
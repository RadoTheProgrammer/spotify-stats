"""
Identify when sth was trendy
obj -> date
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
with open(r"my_spotify_data\Spotify Account Data\StreamingHistory_music_0.json","rb") as f:
    #text=f.read()
    input_data = json.load(f)

data={"endTime":[],"artistName":[],"trackName":[],"timePlayed":[]}
for track in input_data:
    data["endTime"].append(track["endTime"])
    data["artistName"].append(track["artistName"])
    data["trackName"].append(track["trackName"])
    data["timePlayed"].append(track["msPlayed"])

df = pd.DataFrame(data)
df = df.astype({"endTime":"datetime64[s]"})#, "time




artist = "Haywyre"
track = "Tell Me - Ellis Remix"
df = df[(df["artistName"] == artist) & (df["trackName"] == track)]
#df = df[df["artistName"]=="Haywyre" and df["trackName"]=="Tell Me - Ellis Remix"]

#df_counts_date = df.groupby(df.endTime.dt.date).size()
df_groups_date = df.groupby(pd.Grouper(key='endTime', freq='1D'))
df_counts_date = df_groups_date.size()
df_counts_date.to_csv("df_counts_date.csv")

df_groups_5d = df.groupby(pd.Grouper(key='endTime', freq='5D'))
df_counts_5d = df_groups_5d.size()
df_counts_5d.to_csv("df_counts_5d.csv")
df_groups_month = df.groupby(pd.Grouper(key='endTime', freq='ME'))
df_counts_month = df_groups_month.size()

plt.plot(df_counts_date.index,df_counts_date, label="5D")
plt.gcf().autofmt_xdate()
plt.show()




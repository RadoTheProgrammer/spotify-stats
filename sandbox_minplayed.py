"""
Identify what was trendy
date -> obj
"""



import pandas as pd
import settings

df = pd.read_csv(settings.FILE_DATA, parse_dates=["endTime"])

df = df[(df["endTime"]>"2025-01-01") & (df["endTime"]<"2025-11-15")]
totalplayed = 0
for track in df.itertuples():
    minPlayed = track.msPlayed/60000  # type: float 
    if minPlayed < 0.5:
        continue
    totalplayed += minPlayed
    print(totalplayed,track.endTime)
    if totalplayed > 19000:
        break
print(df["msPlayed"].sum() / 60000)
# 18573, 17869
df_artist = df.groupby("artistName")
df_artist_size = df_artist.size().sort_values(ascending=False)
df_artist_size.to_csv(settings.DIR_TRG+"/artist_play_counts_minplayed.csv")

df_track = df.groupby(["artistName", "trackName"])
df_track_size = df_track.size()
df_track_size = df_track_size.sort_values(ascending=False)
df_track_size.to_csv(settings.DIR_TRG+"/track_play_counts_minplayed.csv")


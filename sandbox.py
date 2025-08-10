"""
Identify what was trendy
date -> obj
"""



import pandas as pd
import settings

df = pd.read_csv(settings.FILE_DATA, parse_dates=["endTime"])
df = df.astype({"endTime":"datetime64[s]"})#, "timePlayed":"timedelta64[ms]"})





df_artist = df.groupby("artistName")
df_artist_size = df_artist.size().sort_values(ascending=False)
df_artist_size.to_csv(settings.DIR_TRG+"/artist_play_counts.csv")

df_track = df.groupby(["artistName", "trackName"])
df_track_size = df_track.size()
df_track_size = df_track_size.sort_values(ascending=False)
df_track_size.to_csv(settings.DIR_TRG+"/track_play_counts.csv")


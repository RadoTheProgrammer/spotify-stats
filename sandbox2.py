"""
Identify when sth was trendy
obj -> date
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import settings
import rrstats

df = pd.read_csv(settings.FILE_DATA, parse_dates=["endTime"])

artist = "Duumu"#"Hallmore"
track = "Talk!"#"Piece of Me"
#track = "Tell Me - Ellis Remix"

freq = "1D"
if artist:
    if track:
        df = df[(df["artistName"] == artist) & (df["trackName"] == track)]
    else:
        df = df[df["artistName"] == artist]
#df = df[df["artistName"]=="Haywyre" and df["trackName"]=="Tell Me - Ellis Remix"]
print(df.iloc[38:40])
#df_counts_date = df.groupby(df.endTime.dt.date).size()
df_groups = df.groupby(pd.Grouper(key='endTime', freq=freq))
df_counts = df_groups.size()
df_counts5 = df_counts.rolling(5).mean()
df_counts5_trimmed = rrstats.StatsSeries(df_counts).myrolling(5).trimmed_mean(1)
df_counts12 = df_counts.rolling(12).mean()
df_counts12_trimmed = rrstats.StatsSeries(df_counts).myrolling(12).trimmed_mean_p(0.2)
#df_counts.to_csv(f"df_counts_{freq}.csv")
print(df_counts)

plt.bar(df_counts.index,df_counts,label="raw")
#plt.plot(df_counts5.index,df_counts5,label="rolling 5")
#plt.plot(df_counts5_trimmed.index,df_counts5_trimmed,label="rolling 5 trimmed")
#plt.bar(df_counts12.index,df_counts12,label="rolling 12")
#plt.bar(df_counts12_trimmed.index,df_counts12_trimmed,label="rolling 12 trimmed")
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()




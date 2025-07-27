"""
Identify when sth was trendy
obj -> date
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("StreamingHistory.csv", parse_dates=["endTime"])

artist = "Duumu"
track = ""
#track = "Tell Me - Ellis Remix"

freq = "1D"
if artist:
    if track:
        df = df[(df["artistName"] == artist) & (df["trackName"] == track)]
    else:
        df = df[df["artistName"] == artist]
#df = df[df["artistName"]=="Haywyre" and df["trackName"]=="Tell Me - Ellis Remix"]

#df_counts_date = df.groupby(df.endTime.dt.date).size()
df_groups = df.groupby(pd.Grouper(key='endTime', freq=freq))
df_counts = df_groups.size()
#df_counts.to_csv(f"df_counts_{freq}.csv")
print(df_counts)
plt.bar(df_counts.index,df_counts)
plt.gcf().autofmt_xdate()
plt.show()




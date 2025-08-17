import pandas as pd
import matplotlib.pyplot as plt
import settings
import rrstats
FREQ = "1D"
first_played_liked = pd.read_csv(r"data_output\first_played_liked.csv", parse_dates=["endTime"])
first_played = pd.read_csv(r"data_output\first_played.csv", parse_dates=["endTime"])

df_fpl = first_played_liked.groupby(pd.Grouper(key='endTime', freq=FREQ))
df_fpl = df_fpl.size()
df_fpl = df_fpl.rolling(5).mean()
#df_fpl = rrstats.StatsSeries(df_fpl).myrolling(12).trimmed_mean(1)
df_fp = first_played.groupby(pd.Grouper(key='endTime', freq=FREQ))
df_fp = df_fp.size()
df_fp = df_fp.rolling(12).mean()
#df_fp = rrstats.StatsSeries(df_fp).myrolling(12).trimmed_mean(1)
#df_counts.to_csv(f"df_counts_{freq}.csv")
print(df_fpl.mean())
print(df_fp.mean())
#plt.bar(df_fpl.index,df_fpl)
#plt.bar(df_fp.index,df_fp)

plt.plot(df_fp.index,df_fp,label="fp")
plt.plot(df_fpl.index,df_fpl,label="fpl")

print(df_fp)
print(df_fpl)
plt.gca().legend()
plt.gcf().autofmt_xdate()
plt.show()
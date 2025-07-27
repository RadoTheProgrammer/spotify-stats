import json
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StreamingHistory.csv", parse_dates=["endTime"])
df_groups_hour = df.groupby(pd.Grouper(key='endTime', freq='1h'))
df_counts_hour = df_groups_hour.size()
df_counts_hour = df_counts_hour[(df_counts_hour.index > "2024-07-01") & (df_counts_hour.index < "2024-07-02")]  # Filter out empty hours
plt.bar(df_counts_hour.index, df_counts_hour,width=0.03)
plt.gcf().autofmt_xdate()
plt.show()
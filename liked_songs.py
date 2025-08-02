import pandas as pd
import matplotlib.pyplot as plt
FREQ = "1W"
first_played_liked = pd.read_csv(r"data_output\first_played_liked.csv", parse_dates=["endTime"])


df_groups = first_played_liked.groupby(pd.Grouper(key='endTime', freq=FREQ))
df_counts = df_groups.size()
#df_counts.to_csv(f"df_counts_{freq}.csv")
print(df_counts.mean())
plt.bar(df_counts.index,df_counts)
plt.gcf().autofmt_xdate()
plt.show()
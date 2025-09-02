# %% [markdown]
# #assignment1

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %%
sns.set_style("darkgrid")

# %% [markdown]
# ##Load Dataset

# %%
df = pd.read_csv("spotify_data.csv")
df

# %%
df = pd.read_csv("spotify_data.csv")
df.drop("Unnamed: 0", axis=1,inplace=True)
df.head()

# %%
##Data Cleaning 

# %%
df.isna().sum()

# %%
df.info()

# %%
df.shape

# %%
df.columns

# %%
len(df.columns)

# %%
df.describe()

# %% [markdown]
# ##Data analysis 

# %% [markdown]
# ###Top 5 most popular artists

# %%
top_five_artists =df.groupby("artist").count().sort_values(by="song_title",ascending=False)["song_title"][:5]
top_five_artists

# %%
top_five_artists.plot.barh()
plt.show()

# %% [markdown]
# ###Top 5 loudest tracks

# %%
top_five_loudest_tracks = df[["loudness", "song_title","artist"]].sort_values(by="loudness", ascending = True)[:5]
top_five_loudest_tracks

# %%
plt.figure(figsize=(12,7))
sns.barplot(x="loudness",y="song_title",data=top_five_loudest_tracks)
plt.title("top 5 loudest tracks")
plt.show()

# %% [markdown]
# ###Top 10 instrumentalness tracks

# %%
top_ten_instrumental_tracks=df[["instrumentalness","song_title","artist"]].sort_values(by="instrumentalness",ascending=False)[:10]
top_ten_instrumental_tracks

# %%
plt.figure(figsize=(12,7))
plt.pie(x="instrumentalness",data=top_ten_instrumental_tracks,autopct='%1.2f%%',labels=top_ten_instrumental_tracks.song_title)
plt.title("top_ten_instrumental_tracks")
plt.show()

# %% [markdown]
# ###Multiple feature plots

# %%
interest_feature_cols=["tempo","loudness","acousticness","danceability","duration_ms","energy","instrumentalness","liveness","speechiness","valence"]

# %%
for feature_col in interest_feature_cols:
    pos_data=df[df["target"]==1][feature_col]
    neg_data=df[df["target"]==0][feature_col]
    
    plt.figure(figsize=(12,7))
    
    sns.distplot(pos_data, bins=30, label="positive", color="yellow")
    sns.distplot(neg_data, bins=30, label="negative", color="red")
    
    plt.legend(loc="upper right")
    plt.title(f"positive and negative histogram  plot for {feature_col}")
    plt.show()
    

# %%




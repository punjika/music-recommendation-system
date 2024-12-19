from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load cleaned data
from data_cleaning import load_and_clean_data

# Load and preprocess data
cleaned_data = load_and_clean_data('spotify_songs.xlsx')
features = ['tempo', 'danceability', 'energy', 'valence', 'acousticness']
X = cleaned_data[features]

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform clustering
kmeans = KMeans(n_clusters=5, random_state=42)
cleaned_data['cluster'] = kmeans.fit_predict(X_scaled)

# Recommendation function
def recommend_songs(song_name=None, speed_category=None, num_recommendations=5):
    if song_name:
        song_row = cleaned_data[cleaned_data['track_name'].str.contains(song_name, case=False)]
        if song_row.empty:
            return f"No song found with name '{song_name}'!"
        cluster_label = kmeans.predict(scaler.transform(song_row[features]))[0]
    elif speed_category:
        cluster_label = cleaned_data[cleaned_data['speed_category'] == speed_category]['cluster'].mode()[0]
    else:
        return "Provide either a song name or a speed category!"

    cluster_songs = cleaned_data[cleaned_data['cluster'] == cluster_label]
    return cluster_songs.sample(n=min(num_recommendations, len(cluster_songs)))[['track_name', 'tempo', 'speed_category']]

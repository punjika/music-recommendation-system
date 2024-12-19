import pandas as pd

# Load the dataset
def load_and_clean_data(filepath):
    data = pd.read_excel(filepath)

    # Drop irrelevant columns
    columns_to_drop = ['playlist_name', 'language', 'duration_ms', 'key', 'mode']
    data = data.drop(columns=columns_to_drop, errors='ignore')

    # Handle missing values and duplicates
    data = data.dropna().drop_duplicates()

    # Categorize songs by speed
    def categorize_speed(tempo):
        if tempo < 100:
            return 'Slow'
        elif 100 <= tempo <= 140:
            return 'Medium'
        else:
            return 'Fast'

    data['speed_category'] = data['tempo'].apply(categorize_speed)

    return data

if __name__ == "__main__":
    # Example usage
    cleaned_data = load_and_clean_data('spotify_songs.xlsx')
    print(cleaned_data.head())

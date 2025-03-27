from google_play_scraper import Sort, reviews_all
import pandas as pd
scrapreview= reviews_all(
'com.gojek.app', #ID aplikasi
lang='id', # defaults to 'en'
country='id', # defaults to 'us'
sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
filter_score_with=1 # defaults to None (means all score)
)
print(scrapreview)
app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.to_csv(r'C:\Users\ivanovna\coding/playstore-1.csv', index=None, header=True)

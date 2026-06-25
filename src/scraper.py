from google_play_scraper import reviews, Sort
import pandas as pd

APPS = {
    "WhatsApp": "com.whatsapp",
    "PayPal": "com.paypal.android.p2pmobile",
    "CashApp": "com.squareup.cash"
}

def scrape_reviews(app_name, app_id, num_reviews=300):
    print(f"Scraping {app_name} reviews...")
    result, _ = reviews(app_id, 
                      lang='en', 
                      country='us', 
                      sort=Sort.NEWEST, 
                      count=num_reviews)
    print(f"{app_name}: {len(result)} resultados")
    if len(result) == 0:
        return pd.DataFrame()
    df = pd.DataFrame(result)
    df["app"] = app_name
    return df

def main():
    import os
    os.makedirs("data", exist_ok=True)

    all_reviews = []
    for app_name, app_id in APPS.items():
        df = scrape_reviews(app_name, app_id)
        if not df.empty:
            all_reviews.append(df)


    combined = pd.concat(all_reviews, ignore_index=True)
    combined = combined[["app", "userName", "score", "content","at"]]
    combined.columns = ["app", "user", "rating","review","date"]
    combined.dropna(subset = ["review"], inplace=True)
    combined.to_csv("data/reviews_raw.csv", index = False)
    print(f"Done {len(combined)} reviews scraped.")



if __name__ == "__main__":
    main()
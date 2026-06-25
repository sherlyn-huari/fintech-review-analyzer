import pandas as pd 
df = pd.read_csv("data/reviews_raw.csv")

# Sentimiento por rating
def get_sentiment(rating):
    if rating >=4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:   
        return "negative"
    
#categoria por keywrods
def get_category(review):
    review = str(review).lower()
    if any(w in review for w in ["payment", "transfer", "send", "money", "transaction", "charge"]):
        return "payments"
    elif any(w in review for w in ["crash", "error", "bug", "slow", "freeze", "loading"]):
        return "performance"
    elif any(w in review for w in ["interface", "design", "ui", "button", "screen", "easy", "confusing"]):
        return "ux"
    elif any(w in review for w in ["support", "help", "customer", "service", "response"]):
        return "support"
    else:
        return "other"
    
df ["sentiment"] = df["rating"].apply(get_sentiment)
df ["category"] = df["review"].apply(get_category)
df["date"] = pd.to_datetime(df["date"]).dt.date

df.to_csv("data/reviews_classified.csv", index = False)
print(f"Done — {len(df)} reseñas clasificadas")
print(df["category"].value_counts())
print(df["sentiment"].value_counts())
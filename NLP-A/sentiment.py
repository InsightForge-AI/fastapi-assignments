# Install (only needed in Colab once)


# Import libraries
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Import dataset
df = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t')
df.head()

# Initialize analyzer (only once)
analyzer = SentimentIntensityAnalyzer()

# ✅ Generic function (DATA-INDEPENDENT)
def get_sentiment(text: str) -> str:
    if not isinstance(text, str):   # handle non-text safely
        return "neutral"
    
    score = analyzer.polarity_scores(text)
    compound = score['compound']

    if compound >= 0.05:
        return "positive"
    elif compound <= -0.05:
        return "negative"
    else:
        return "neutral"

print("START")
sent = get_sentiment("Crust is not good.")
print("RESULT:", sent)
print("END")
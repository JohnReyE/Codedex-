from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from textblob import TextBlob


# Label each review as either "positive" or "negative."
reviews = ['This movie was fantastic! A must-watch.',
           'I didn\'t enjoy this movie at all.',
           'Amazing storyline and great acting!',
           'The plot was dull and predictable.',
           'Loved the cinematography! Highly recommended.']

labels = ['positive', 'negative', 'positive', 'negative', 'positive']

# (Optional) Correct any spelling mistakes in the reviews using TextBlob
corrected_reviews = [str(TextBlob(review).correct()) for review in reviews]

# Vectorize the Text Data
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

# Split the Data into Training and Testing Sets

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(x_train, y_train)

# Test the model
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Interpret the Results
if accuracy > 0.5:
    print("Good vibes. Book a ticket!")
else:
    print("Need more work!")
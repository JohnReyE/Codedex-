from textblob import TextBlob

# Text variable with a spelling error.abs
text = "I havv a speling errror in this sentense."

# Create a TextBlob object
blob = TextBlob(text)

# Check for spelling errors and correct them

corrected_text = blob.correct()
print("Original Text:", text)
print("Corrected Text:", corrected_text)



from translate import Translator

# Create a translator object
translator = Translator(to_lang="es")

# Translate a text
text = "Hello, how are you?"

# Perform the translation
translated_text = translator.translate(text)

# Print the translated text
print("Translated Text:", translated_text)

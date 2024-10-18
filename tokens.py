import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def tokenize_text(text):
    return word_tokenize(text)

# Example usage
text = "Hello, how can I help you?"
tokens = tokenize_text(text)
print(tokens)

import gensim.downloader as api

def load_glove_model():
    glove = api.load("glove-wiki-gigaword-100")  # You can choose different dimensions
    return glove

glove_model = load_glove_model()

def get_word_embeddings(tokens):
    embeddings = [glove_model[word] for word in tokens if word in glove_model]
    return embeddings

# Example usage
embeddings = get_word_embeddings(tokens)
print(embeddings)

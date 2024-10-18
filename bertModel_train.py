from transformers import BertTokenizer, BertForSequenceClassification
import torch

def prepare_bert_model():
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)  # Adjust num_labels as needed
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    return model, tokenizer

model, tokenizer = prepare_bert_model()

def encode_texts(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
    return inputs

# Example usage
texts = ["Hello, how can I help you?", "What are your hours?"]
encoded_inputs = encode_texts(texts)

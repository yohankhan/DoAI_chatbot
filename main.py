from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        return self.texts[idx], self.labels[idx]

# texts = [...]  
# labels = [...]  

# dataset = CustomDataset(texts, labels)
# train_loader = DataLoader(dataset, batch_size=16, shuffle=True)

# Training loop (simplified)
# for epoch in range(num_epochs):
#     for batch in train_loader:
#         optimizer.zero_grad()
#         inputs = encode_texts(batch[0])
#         outputs = model(**inputs)
#         loss = loss_function(outputs, batch[1])
#         loss.backward()
#         optimizer.step()

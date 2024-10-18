import pandas as pd
import requests

def download_dataset(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

# Example usage
url = 'https://raw.githubusercontent.com/algolia/datasets/master/ecommerce-support.json'  # Replace with your dataset URL
filename = 'dataset.csv'
downloaded_file = download_dataset(url, filename)

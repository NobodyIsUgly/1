import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_data():
    url = 'https://example.com/tft/match_data'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    matches = []
    for match in soup.find_all('div', class_='comp-card'):
        outcome = int(match.find('div', class_='comp-outcome').text)
        feature1 = float(match.find('div', class_='feature1').text)
        feature2 = float(match.find('div', class_='feature2').text)
        feature3 = float(match.find('div', class_='feature3').text)
        matches.append([outcome, feature1, feature2, feature3])

    df = pd.DataFrame(matches, columns=['outcome', 'feature1', 'feature2', 'feature3'])
    df.to_csv('data/processed/match_data.csv', index=False)


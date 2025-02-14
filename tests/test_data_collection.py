import pytest
from src.data_collection import collect_data
from bs4 import BeautifulSoup

def parse_metatft(soup):
    matches = []
    for match in soup.find_all('div', class_='comp-card'):
        outcome = int(match.find('div', class_='comp-outcome').text)
        feature1 = float(match.find('div', class_='feature1').text)
        feature2 = float(match.find('div', class_='feature2').text)
        feature3 = float(match.find('div', class_='feature3').text)
        matches.append([outcome, feature1, feature2, feature3])
    return matches

def test_collect_data(mocker):
    mock_html = '''
    <div class='comp-card'>
        <div class='comp-outcome'>1</div>
        <div class='feature1'>2.0</div>
        <div class='feature2'>3.0</div>
        <div class='feature3'>4.0</div>
    </div>
    '''
    soup = BeautifulSoup(mock_html, 'html.parser')
    data = parse_metatft(soup)
    assert len(data) == 1
    assert data[0] == [1, 2.0, 3.0, 4.0]


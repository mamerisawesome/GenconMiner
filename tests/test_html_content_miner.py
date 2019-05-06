from html_content_miner import GenconMiner, __version__

def test_version():
    assert __version__ == '0.1.0'

def test_url_extract():
    miner = GenconMiner(url='http://google.com')
    data = miner.extract('title')
    assert data[-1].text == 'Google'

def test_text_extract():
    import requests
    html_data = requests.get('http://google.com')
    miner = GenconMiner(text=html_data.text)
    data = miner.extract('title')
    assert data[-1].text == 'Google'

def test_on_target_extract():
    miner = GenconMiner(url='http://google.com')
    data = miner.extract('html', 'title')
    assert data[-1].text == 'Google'

def test_on_get_all_text():
    import json
    miner = GenconMiner(url='http://jsonplaceholder.typicode.com/todos/1')
    data = miner.to_text()
    test_json = {"userId": 1,
                 "id": 1,
                 "title": "delectus aut autem",
                 "completed": False}
    assert json.loads(data) == test_json

def test_on_get_soup():
    from bs4 import BeautifulSoup
    miner = GenconMiner(url='http://google.com')
    assert isinstance(miner.to_soup(), BeautifulSoup)

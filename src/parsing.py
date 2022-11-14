import requests
from bs4 import BeautifulSoup


def parser(coin: str):
    try:
        coin = coin.lower().replace(" ", "-")
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        request = requests.get(url)
        html = request.text
        soup = BeautifulSoup(html, "html.parser")
        if "something went wrong" in soup.text:
            raise Exception("Check Name")
        else:
            price_value_class = soup.find("div", {'class': "priceValue"})
            span: str = price_value_class.find("span").string
            result = span.replace(",", "")
            return result
    except:
       return request.status_code


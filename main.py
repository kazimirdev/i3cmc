from requests import get
from bs4 import BeautifulSoup



def parcer(coin: str):
    try:
        coin = coin.lower().replace(" ", "-")
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        html = get(url).text
        soup = BeautifulSoup(html, "html.parser")
        if "something went wrong" in soup.text:
            return "Run install script one more time and check input."
        else:
            price_value_class = soup.find("div", {'class': "priceValue"})
            normal_output = price_value_class.find("span").string[1:]
            cutted_output = normal_output.split(".")[0]
    except:
        pass


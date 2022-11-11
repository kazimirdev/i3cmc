from requests import get
from bs4 import BeautifulSoup


def parser(coin: str):
    try:
        coin = coin.lower().replace(" ", "-")
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        html = get(url).text
        soup = BeautifulSoup(html, "html.parser")
        if "something went wrong" in soup.text:
            print("Run install script one more time and check input.")
            return "InputError"
        else:
            return soup.find(
                    "div", {'class': "priceValue"}
                    ).find("span").string
    except:
        return "ConnectionError"


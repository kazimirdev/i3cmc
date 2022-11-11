from json import dump
from os import remove


with open(".cache", "r") as cache:
    line: str = cache.read()
    names_of_coins: list[str] = [coin.strip() for coin in line.split(",")]
    names_and_prices: dict[str, int] = {name: -1 for name in names_of_coins}
    with open("data.json", "w") as datafile:
        dump(names_and_prices, datafile)
remove(".cache")

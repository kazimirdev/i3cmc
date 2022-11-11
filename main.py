from json import loads
from src import parser


def main():    
    output = dict()
    with open("data.json", "w") as data:
        output: dict = loads(data.read())

    for key in output.keys():
        output[key] = parser(coin=key)


if __name__ == "__main__":
    main()

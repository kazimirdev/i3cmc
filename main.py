from json import dump, loads

from src import parser


def main():
    data = open("data.json", "r+")
    output: dict = loads(data.read())
    data.close()
    for key in output.keys():
        try:
            output[key]['price'] = parser(coin=key)
        except:
            output[key]['error'] = True
        else:
            output[key]['error'] = False
    data = open("data.json", "w+")
    dump(output, data)
    data.close()
    print(' | '.join({f"{key}:{output[key]['price']}" if not output[key]['error'] else f"{key}:{output[key]['price']}[cache]" for key in tuple(output.keys())}))
        

if __name__ == "__main__":
    main()

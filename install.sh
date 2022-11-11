echo "Enter the names of cryptocurrencies separated by commas:"
read NAME

echo ${NAME} > .cache
python3 installer.py

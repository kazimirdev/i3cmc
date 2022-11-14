echo "Enter the names of cryptocurrencies separated by commas:"
read NAME

echo ${NAME} > .cache
pip install -r requirements.txt
python3 installer.py

echo "Enter the names of cryptocurrencies separated by commas:"
read cryptoarray
path=$(pwd)

echo "Enter the path to the i3 config file (with filename):"
read i3path

echo ${cryptoarray} > .cache

echo \ 
"

# i3cmc
bar {

        font pango:Days 9
        output eDP
        position bottom
        status_command i3blocks -c ${path}/config
        workspace_buttons no
        tray_output none

        }
" >> ${i3path}

echo \
"
[i3cmc]
command=python ${path}/main.py
interval=60
signal=1
" > ${path}/config 



pip install -r requirements.txt
python3 installer.py

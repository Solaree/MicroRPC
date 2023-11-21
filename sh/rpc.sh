sudo apt -y update && sudo apt -y upgrade
sudo apt -y install python3 python3-pip
pip install pypresence

sudo chmod +x ./micro.sh
sudo cp ./micro.sh /usr/local/bin/micro
sudo mkdir -p $HOME/.config/micro/plug/MicroRPC
sudo cp ../rpc/rpc.py $HOME/.config/micro/plug/MicroRPC/rpc.py

SCRIPT_PATH="/usr/local/bin/micro"
CONTENT="alias micro $SCRIPT_PATH"
CONFIG="$HOME/.config/fish/config.fish"

if [ -e "$CONFIG" ]; then
    echo "$CONTENT" >> "$CONFIG"
else
    echo "$CONTENT" > "$CONFIG"
fi

clear
echo "\033[0;102mMicroRPC: Script finished. Please restart your terminal or run 'source ~/.config/fish/config.fish' to apply the changes."

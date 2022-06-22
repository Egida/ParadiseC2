clear
echo "Installing required files for "ParadiseC2" 20% [==>-------]"
sudo apt install python3
clear
echo "Installing required files for "ParadiseC2" 50% [=====>----]"
sudo apt install pip3 colorama
clear
echo "Installing required files for "ParadiseC2" 100% [==========]"
sleep 2
clear
echo "Cleaning up"
sleep 2
rm -rf installation.sh
clear
python3 cnc.py

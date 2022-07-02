clear
echo "Installing required files for "ParadiseC2" 20% [==>-------]"
sudo apt install python3
sudo apt install python2
sudo apt install python
clear
echo "Installing required files for "ParadiseC2" 50% [=====>----]"
sudo apt install pip3
pip3 install colorama
clear
echo "Installing required files for "ParadiseC2" 100% [==========]"
sleep 2
clear
echo "Cleaning up"
sleep 2
rm -rf installation.sh
clear
python3 cnc.py
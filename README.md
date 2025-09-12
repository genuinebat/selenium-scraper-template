# Preparing Dependencies

### Execute the following commands to download and install all the necessary script dependencies

Updates all apps and installs Vulkan library
```
sudo apt-get update
sudo apt-get install -y wget unzip libvulkan1
```
Download and install latest stable version of Google Chrome
```
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f -y
sudo rm google-chrome-stable_current_amd64.deb
```
Setup local Python virtual environment
```
sudo apt install python3-venv
python3 -m venv env
```
Download and install required Python modules in the venv
```
source env/bin/activate
pip install -r requirements.txt
```

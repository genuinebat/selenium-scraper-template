# Install Dependencies

Execute the following commands in order within this folder

'''
sudo apt-get update
sudo apt-get install -y wget unzip libvulkan1

sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -f -y

source env/bin/activate
pip install -r requirements.txt
'''

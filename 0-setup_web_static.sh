#!/usr/bin/env bash
# script that sets up your web servers for the deployment
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html><head></head><body>Hello!</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
CF="/etc/nginx/sites-available/default"
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' "$CF"
sudo service nginx start

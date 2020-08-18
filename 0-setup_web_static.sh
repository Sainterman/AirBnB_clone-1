#!/usr/bin/env bash
# Install nginx and configure default pages and routes
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

sudo mkdir -p "/data/web_static/releases/test"
sudo mkdir -p "/data/web_static/shared/"
sudo touch "/data/web_static/releases/test/index.html"
echo "<html><head><title>test</title></head><body><p>just fior testing.</p></body></html>">/data/web_static/releases/test/index.html

sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu /data/
config="/etc/nginx/sites-enabled/default"
sudo sed -i "/server_name _;/ a \\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n" "$config"
sudo service nginx restart

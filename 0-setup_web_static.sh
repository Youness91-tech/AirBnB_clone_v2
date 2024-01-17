#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "ALX SE" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

configuration="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$configuration"; then
    sudo sed -i "/server_name _;/a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" "$configuration"
fi

sudo service nginx restart

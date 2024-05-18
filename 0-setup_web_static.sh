#!/bin/env bash
# script that configures an nginix server with some folders and files

sudo apt-get -y update
sudo apt-get -y install ngnix
service bginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
<head>
</head>
<body>
Hello World!
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -P ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
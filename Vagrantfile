Vagrant.configure("2") do |config|
  
config.vm.box = "hashicorp/bionic64"
# config.vm.box_check_update = false


config.vm.network "forwarded_port", guest: 80, host: 80
config.vm.network :forwarded_port, guest: 443, host: 443
# config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
# config.vm.network "private_network", ip: "192.168.33.10"
# config.vm.network "public_network"
# config.vm.synced_folder ".", "/var/www/html"

config.vm.provision "shell", inline: <<-SHELL
apt-get update
apt-get install -y apache2

sudo cp -r /vagrant/static/ /var/www/
sudo cp -r /vagrant/dynamic/ /var/www/
sudo cp -r /vagrant/SSL /etc/apache2/
sudo cp /vagrant/server.py /var/www/
cp -f /vagrant/000-default.conf /etc/apache2/sites-available/000-default.conf
cp -f /vagrant/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
a2enmod ssl headers proxy proxy_http
a2ensite 000-default.conf default-ssl.conf
service apache2 reload
echo "127.0.0.1 static.local" >> /etc/hosts
echo "127.0.0.1 dynamic.local" >> /etc/hosts

apt-get install -y python3-pip
pip3 install -U pip aiohttp
nohup python3 /var/www/server.py &

SHELL
end

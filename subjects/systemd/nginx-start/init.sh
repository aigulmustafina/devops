set -e

apt update
apt install -y nginx
service nginx stop

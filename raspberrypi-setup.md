sudo raspi-config #カメラ ON
sudo apt-get install vim
sudo vim /usr/share/alsa/alsa.conf
    19行目 #
    defaults.ctl.card 0 => 1
    defaults.pcm.card 0 => 1
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
./ngrok authtoken 4iDoXA1zoGrfLHv5w48pk_3sBJoNt7naWk4gm41KkCg
./ngrok http 8080
sudo pip3 install --upgrade google-cloud-vision
json セッティング
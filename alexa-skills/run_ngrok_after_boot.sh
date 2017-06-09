#Add a command to /etc/rc.local before exit
# or add to crontab 

/home/pi/FishTank/ngrok start --all \
  --config=/home/pi/FishTank/ngrok.yml \
  --log=stdout \
  > /dev/null

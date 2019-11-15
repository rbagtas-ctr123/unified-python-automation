#!/bin/bash

start_sauce_connect_service() {
DONE=0
SAUCE_USERNAME=${SAUCE_USERNAME}
SAUCE_API_KEY=${SAUCE_API_KEY}
SAUCE_TUNNEL_IDENTIFIER=${SAUCE_TUNNEL_IDENTIFIER}

echo "STARTING SAUCE CONNECT SERVICE"
cd sauce_connect || exit
bin/sc -u ${SAUCE_USERNAME} -k ${SAUCE_API_KEY} -i ${SAUCE_TUNNEL_IDENTIFIER} -v -l /tmp/sc-${SAUCE_TUNNEL_IDENTIFIER}.log &

counter=0
echo "CHECKING IF SAUCE LABS IS UP AND RUNNING"
while true;
do
  sleep 5
  STATUS=$(grep -Eo "Sauce Connect is up, you may start your tests" /tmp/sc-${SAUCE_TUNNEL_IDENTIFIER}.log)
  if [ "$STATUS" = "Sauce Connect is up, you may start your tests" ]
  then
       echo "DONE! SAUCE IS READY"
       break
  elif [ "$counter" -gt 10 ]
  then
       echo "COUNTER: $counter TIMES REACHED"
       echo "SAUCE LABS DID NOT START"
       exit 1
  else
       counter=$((counter+1))
       echo "STILL CHECKING CONNECTIONS"
  fi
done
}

# Executes the method defined at the top of the file script
start_sauce_connect_service

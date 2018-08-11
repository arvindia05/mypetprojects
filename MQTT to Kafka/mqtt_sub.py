
#!/usr/bin/python

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import ssl

ssl.match_hostname = lambda cert, hostname: True

auth = {
  'username':prop.username,
  'password':prop.password
}

tls = {
  'ca_certs':prop.cert_path,
  'tls_version':ssl.PROTOCOL_TLSv1
}

# msg = subscribe.simple("test-topic", retained=False, hostname="ec2-54-245-171-189.us-west-2.compute.amazonaws.com",
#     port=8883, client_id="testing1", keepalive=5, will=None, auth=auth, tls=tls,
#     protocol=mqtt.MQTTv311)
# 
# print msg.topic
# print msg.payload

def on_message_print(client, userdata, message):
    print message.payload

subscribe.callback(on_message_print, prop.topic, hostname=prop.host,port=prop.port,auth=auth, tls=tls,keepalive=60,protocol=mqtt.MQTTv311)
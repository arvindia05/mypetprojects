
#!/usr/bin/python

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ssl
import prop

ssl.match_hostname = lambda cert, hostname: True

auth = {
  'username':prop.username,
  'password':prop.password
}

tls = {
  'ca_certs':prop.cert_path,
  'tls_version':ssl.PROTOCOL_TLSv1
}

msgs = []

for i in range(479,599):

    msg = {'topic':prop.topic1, 'payload':i}
    msgs.append(msg)

    if len(msgs) == 10:
      publish.multiple(msgs,
      	hostname=prop.hostname,
      	client_id=prop.clientID,
      	auth=auth,
      	tls=tls,
      	port=prop.port,
      	protocol=mqtt.MQTTv311)
      msgs = []
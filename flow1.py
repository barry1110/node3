[{"id":"19fc168.6a52eea","type":"tab","label":"Flow 1","disabled":false,"info":""},{"id":"d4087468.a28938","type":"inject","z":"19fc168.6a52eea","name":"","topic":"","payload":",,25.5","payloadType":"str","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":110,"y":120,"wires":[["bbe042e2.6232b"]]},{"id":"e2f12300.de94f","type":"inject","z":"19fc168.6a52eea","name":"","topic":"","payload":",,20.3","payloadType":"str","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":110,"y":240,"wires":[["bbe042e2.6232b"]]},{"id":"bbe042e2.6232b","type":"mqtt out","z":"19fc168.6a52eea","name":"","topic":"mcs/DMQgbphJ/ww2feEtERPLAwwNQ/Temperature","qos":"2","retain":"","broker":"1936a805.a875e8","x":510,"y":200,"wires":[]},{"id":"1936a805.a875e8","type":"mqtt-broker","z":"","name":"MCS Cloud","broker":"mqtt.mcs.mediatek.com","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"birthTopic":"","birthQos":"0","birthPayload":"","closeTopic":"","closeQos":"0","closePayload":"","willTopic":"","willQos":"0","willPayload":""}]

[{"id":"18a8de6.ce87122","type":"tab","label":"Flow 2","disabled":false,"info":""},{"id":"2f1d56b2.a2626a","type":"mqtt in","z":"18a8de6.ce87122","name":"","topic":"mcs/DMQgbphJ/ww2feEtERPLAwwNQ/+","qos":"2","datatype":"auto","broker":"1936a805.a875e8","x":230,"y":240,"wires":[["c5c49b36.3fa198"]]},{"id":"c5c49b36.3fa198","type":"csv","z":"18a8de6.ce87122","name":"","sep":",","hdrin":"","hdrout":"","multi":"one","ret":"\\n","temp":",,Data","skip":"0","x":210,"y":340,"wires":[["180c3194.69a6ee"]]},{"id":"180c3194.69a6ee","type":"change","z":"18a8de6.ce87122","name":"Get Data","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.Data","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":200,"y":420,"wires":[["78693929.9cd988"]]},{"id":"78693929.9cd988","type":"ui_gauge","z":"18a8de6.ce87122","name":"","group":"bb29b737.4f2918","order":0,"width":0,"height":0,"gtype":"gage","title":"gauge","label":"units","format":"{{value}}","min":0,"max":"50","colors":["#00b500","#e6e600","#ca3838"],"seg1":"","seg2":"","x":360,"y":420,"wires":[]},{"id":"1936a805.a875e8","type":"mqtt-broker","z":"","name":"MCS Cloud","broker":"mqtt.mcs.mediatek.com","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"birthTopic":"","birthQos":"0","birthPayload":"","closeTopic":"","closeQos":"0","closePayload":"","willTopic":"","willQos":"0","willPayload":""},{"id":"bb29b737.4f2918","type":"ui_group","z":"","name":"Status","tab":"8a2ff257.08291","order":1,"disp":true,"width":"6","collapse":false},{"id":"8a2ff257.08291","type":"ui_tab","name":"Tab 1","icon":"dashboard","order":1}]

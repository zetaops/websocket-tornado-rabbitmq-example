##WebSocket - Tornado - RabbitMQ - Worker Process Example

This example demonstrates realtime bidirectional communication between multiple browser clients and background worker processes over Tornado / Pika / RabbitMQ.
 
 Inbound messages routed through a single channel via "topic" type exchange to multiple workers. Session ID's passed with "routing_key"s. 
 
 Outbound return messages transmitted via per websocket "direct" channels. 

### Testing

First run the `` worker.py `` as is or pass the number of worker sub-processes like this: `` worker.py manage=10 `` 

Then run the `` server.py `` and open http://127.0.0.1:9001 on your browser and press "Run" button. 



### Screenshot

  
  ![Screenshot](https://raw.githubusercontent.com/zetaops/websocket-tornado-rabbitmq-example/master/screenshot.png)


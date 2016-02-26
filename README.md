#WebSocket - Tornado - RabbitMQ - Worker Process Example

  
  ![Screenshot](https://raw.githubusercontent.com/zetaops/websocket-tornado-rabbitmq-example/master/screenshot.png)


This example demonstrates bidirectional communication between browser and background worker processes over Tornado / Pika / RabbitMQ.
 
 Inbound messages routed through a single channel via "topic" type exchange to multiple workers. Session ID's passed with "routing_key"s. 
 
 Outbound return messages transmitted via per socket "direct" channels. 

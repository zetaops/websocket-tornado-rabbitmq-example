**WebSocket - Tornado - RabbitMQ - Worker Process Example

  
  ![Screenshot](https://raw.githubusercontent.com/zetaops/websocket-tornado-rabbitmq-example/master/screenshot.png)


This example demonstrates bidirectional communication between browser and background worker processes over Tornado / Pika / RabbitMQ.
 
 Inbound messages routed through a single "topic" type exchange to multiple workers. Return messages transmitted via per socket direct connections with session IDs as queue names.

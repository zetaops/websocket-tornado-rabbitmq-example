# -*-  coding: utf-8 -*-
"""
tornado websocket proxy for WF worker daemons
"""


from queue import PikaClient
from uuid import uuid4

from tornado import websocket, web, ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def _get_sess_id(self):
        return self.sess_id;

    def open(self):
        self.sess_id = uuid4().hex
        self.application.pc.register_websocket(self._get_sess_id(), self)

    def on_message(self, message):
        self.application.pc.redirect_incoming_message(self._get_sess_id(), message)

    def on_close(self):
        """
        remove connection from pool on connection close.
        """
        self.application.pc.unregister_websocket(self._get_sess_id())


class Connect(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.render('connector.html')


class Index(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.render('index.html')

app = web.Application([
    (r'/ws', SocketHandler),
    (r'/connect', Connect),
    (r'/', Index),
])


def runserver():
    my_ioloop = ioloop.IOLoop.instance()

    # setup pika client
    pc = PikaClient(my_ioloop)
    app.pc = pc
    pc.connect()
    app.listen(9001)
    my_ioloop.start()

if __name__ == '__main__':
    runserver()


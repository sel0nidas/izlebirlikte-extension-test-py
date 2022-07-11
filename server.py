from websocket_server import WebsocketServer

class Websocket_Server():

    def __init__(self, host, port):
        self.server = WebsocketServer(host, port)

    def new_client(self, client, server):
        print("New client({}) connected.".format(client["id"]))

    def client_left(self, client, server):
        print("Client({}) disconnected.".format(client["id"]))

    def message_received(self, client, server, message):
        print("Client({}) said,{}".format(client["id"], message))

    def run(self):
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received) 
        self.server.run_forever()

ws_server = Websocket_Server("localhost" , 8080)
ws_server.run()
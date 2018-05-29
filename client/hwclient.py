#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
from proto_out import test_pb2

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    req = test_pb2.TestReq();
    req.id = 1
    req.name = "test_name"
    socket.send(req.SerializeToString())

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))

import zmq
context = zmq.Context()
receive = context.socket(zmq.PULL)
receive.connect("tcp://localhost:2222")

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:1111")

while 1:
     data = receive.recv_string()
     print(data)
     sender.send_string(data)
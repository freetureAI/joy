import zmq, sys, argparse

context = zmq.Context()


if __name__ == "__main__":
    # different args for different service
    parser = argparse.ArgumentParser()
    parser.add_argument('--type',  dest='type',  type=int, default=1,  help='0: req/rep, 1:pub/sub, 2:push/pull')
    args, more = parser.parse_known_args()

    
    if args.type == 0:
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")
        while 1:
            data = input("input your data: ")
            if data == "q":
                sys.exit()
            socket.send_string(data)
            response = socket.recv_string()
            print(response)
    elif args.type == 1:
        socket = context.socket(zmq.SUB)
        socket.connect("tcp://localhost:1234")
        socket.setsockopt_string(zmq.SUBSCRIBE, '')
        while 1:
            response = socket.recv_string()
            print(response)
    elif args.type == 2:
        socket = context.socket(zmq.PUSH)
        socket.bind("tcp://*:2222")
        while 1:
            data = input("input your data:")
            socket.send_string(data)

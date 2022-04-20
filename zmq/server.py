import zmq, argparse
context = zmq.Context()



if __name__ == "__main__":
    # different args for different service
    parser = argparse.ArgumentParser()
    parser.add_argument('--type',  dest='type',  type=int, default=1,  help='0: req/rep, 1:pub/sub, 2:push/pull')
    args, more = parser.parse_known_args()

    
    if args.type == 0:
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")
        while 1:
            message = socket.recv_string()
            print(message)
            socket.send_string("OK, 200")
    elif args.type == 1:
        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:1234")
        while 1:
            data = input("input your data:")
            print(data)
            socket.send_string(data)
    elif args.type == 2:
        socket = context.socket(zmq.PULL)
        socket.bind("tcp://*:1111")
        while 1:
            data = socket.recv_string()
            print(data)





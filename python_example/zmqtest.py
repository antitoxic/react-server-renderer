import zmq
import time
context = zmq.Context.instance()

with open('./largestate.json', 'r') as myfile:
    data=myfile.read()

sock = context.socket(zmq.REQ)
sock.bind('ipc:///tmp/zmqiscool')
# sock.bind('tcp://*:8080')
# sock.setsockopt(zmq.LINGER, 0) no effect?
sock.setsockopt(zmq.SNDTIMEO, 1000)
sock.setsockopt(zmq.RCVTIMEO, 1000)


while True:
    #  Wait for next request from client
    sock.send_string(data)
    # sock.send_json({"d":2})
    response = sock.recv()
    print("Received request: ", response)
    time.sleep(1)


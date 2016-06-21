import zmq
import ujson

channel = zmq.Context.instance().socket(zmq.REQ)
channel.bind('ipc:///tmp/myapp')
channel.setsockopt(zmq.SNDTIMEO, 1000)
channel.setsockopt(zmq.RCVTIMEO, 1000)


def render(state):
    channel.send(ujson.dumps(state))
    return channel.recv()

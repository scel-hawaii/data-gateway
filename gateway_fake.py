#!/usr/bin/env python

import pika
import time
import json
import datetime
import logging

class RMQ:

    def __init__(self):
        port = 8082
        host = 'localhost'

        connection = pika.BlockingConnection(pika.ConnectionParameters(
                           host, port))

        self.channel = connection.channel()
        self.channel.queue_declare(queue='hello')

    def publish(self, data):
        self.channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=data)



logging.basicConfig(filename='gateway_fake.log',level=logging.DEBUG)
queue = RMQ()

while True:
    string_now = datetime.datetime.now().isoformat()
    packet = {
        'data':'hello, world',
        'timestamp': string_now
    }
    packet_string = json.dumps(packet)
    queue.publish(packet_string);

    seconds = 0.25
    time.sleep(seconds)

    s = "[" + str(datetime.datetime.now()) + "] " + "Published data"
    print s
    logging.info(s)

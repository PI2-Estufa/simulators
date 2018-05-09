import time
import random
from nameko.standalone.rpc import ClusterRpcProxy

temperature = 20
config = {'AMQP_URI':'amqp://rabbit:5672'}

with ClusterRpcProxy(config) as cluster_rpc:


    while True:
        
        cluster_rpc.temperature_server.receive_temperature(temperature)
        time.sleep(2)
        temperature = random.randint(20, 30) + random.random()

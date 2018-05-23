import time
import random
from nameko.standalone.rpc import ClusterRpcProxy

temperature = 20
ph = 7.0
humidity = 95.00
config = {'AMQP_URI':'amqp://rabbit'}

with ClusterRpcProxy(config) as cluster_rpc:
    while True:
        cluster_rpc.temperature_server.receive_temperature(temperature)
        cluster_rpc.humidity_server.receive_humidity(humidity)
        cluster_rpc.ph_server.receive_ph(ph)
        time.sleep(2)
        temperature = round(random.uniform(23.0, 26.0), 2)
        ph = round(random.uniform(6.6, 7.4), 1)
        humidity = round(random.uniform(93.0, 97.9), 2)

import time
import random
from nameko.standalone.rpc import ClusterRpcProxy

temperature = 20
ph = 7.0
humidity = 95.00
ilumination = True
water_level = 1
water_temperature = 20
drawer_status = True

config = {'AMQP_URI':'amqp://rabbit'}

with ClusterRpcProxy(config) as cluster_rpc:
    while True:
        cluster_rpc.temperature_server.receive_temperature(temperature)
        cluster_rpc.humidity_server.receive_humidity(humidity)
        cluster_rpc.ph_server.receive_ph(ph)
        cluster_rpc.ilumination_server.receive_ilumination(ilumination)
        cluster_rpc.water_level_server.receive_water_level(water_level)
        cluster_rpc.water_temperature_server.receive_water_temperature(water_temperature)
        cluster_rpc.drawer_status_server.receive_drawer_status(drawer_status)
        time.sleep(2)
        temperature = random.uniform(23.0, 26.0)
        ph = random.uniform(6.6, 7.4)
        humidity = random.uniform(93.0, 97.9)
        ilumination = bool(random.getrandbits(1))
        water_level = random.randint(0,2)
        water_temperature = random.uniform(23.0, 26.0)
        drawer_status = bool(random.getrandbits(1))


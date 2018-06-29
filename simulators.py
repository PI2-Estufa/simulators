import time
import random
import os
from nameko.standalone.rpc import ClusterRpcProxy

temperature = 20
ph = 7.0
humidity = 95.00
ilumination = True
water_level = 1
drawer_status = 1
water_temperature = 20
# images.remove('.keep')

i = 0

config = {'AMQP_URI':'amqp://rabbit'}

with ClusterRpcProxy(config) as cluster_rpc:
    while True:
        images = os.listdir('./uploads')
        cluster_rpc.temperature_server.receive_temperature(temperature)
        cluster_rpc.humidity_server.receive_humidity(humidity)
        cluster_rpc.ph_server.receive_ph(ph)
        cluster_rpc.ilumination_server.receive_ilumination(ilumination)
        cluster_rpc.water_level_server.receive_water_level(water_level)
        cluster_rpc.water_temperature_server.receive_water_temperature(water_temperature)
        cluster_rpc.drawer_status_server.receive_drawer_status(drawer_status)
        if len(images) > 0:
            cluster_rpc.image_server.receive_image(images[i % len(images)])
        time.sleep(10)
        temperature = random.uniform(23.0, 26.0)
        ph = random.uniform(6.6, 7.4)
        humidity = random.uniform(93.0, 97.9)
        ilumination = bool(random.getrandbits(1))
        water_level = random.randint(0,2)
        water_temperature = random.uniform(23.0, 26.0)
        drawer_status = random.randint(0,3)
        i += 1
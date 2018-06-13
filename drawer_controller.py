import os
from nameko.rpc import rpc


def get_current_drawer_state():
    current_state = int(os.environ.get("DRAWER_STATE", "0"))
    return current_state


class DrawerController():
    def __init__(self):
        print("starting!")

    name = "drawer_controller"

    @rpc
    def handle_drawer(self, current_state):
        os.environ["DRAWER_STATE"] = str(current_state)
        return current_state

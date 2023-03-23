from dino_runner.utils.constants import MEGA_MOTO, MOTO_TYPE, LIFE
from dino_runner.components.power_ups.power_up import PowerUp

class Moto(PowerUp):
    def __init__(self):
        super().__init__(MEGA_MOTO, MOTO_TYPE)
        
class Life(PowerUp):
    def __init__(self):
        super().__init__(LIFE, MOTO_TYPE)



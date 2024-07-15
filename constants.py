"""
Author: Mubarak Idoko
Date: 2024-06-08

Constant Definitions
"""

# screen dimensions
WIDTH, HEIGHT = 1000, 1000

# game constants
FPS = 60
RADIUS = 400
CAR_RADIUS = 10
NUM_CARS = 10
NORMAL_SPEED = 1
SLOW_SPEED = 0.2
FAST_SPEED = 2
COLLISION_DISTANCE = 10 * CAR_RADIUS  # Minimum distance to avoid collisions
MIN_FLUCTUATION = -0.2
MAX_FLUCTUATION = 0.2

# other constants
CAR_ASSETS_DIR = 'assets/'
TELEMETRY_FILE = 'telemetry/car_simulation_telemetry.csv'

# car images
CAR_IMAGE_FILENAMES = [
    'black_car.png',
    'blue_truck.png',
    'green_car.png',
    'orange_car.png',
    'yellow_car.png'
]

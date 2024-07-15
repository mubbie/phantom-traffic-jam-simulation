"""
Author: Mubarak Idoko
Date: 2024-06-08

Traffic Simulator (with Pygame)
Pygame docs: https://www.pygame.org/docs/
"""

# import libraries
import random
import pygame

# import from project
from constants import (NUM_CARS, WIDTH, HEIGHT, RADIUS, FPS, NORMAL_SPEED,
                       CAR_ASSETS_DIR, TELEMETRY_FILE, CAR_IMAGE_FILENAMES)
from colors import BLACK, ROAD_COLOR, GRASSY_GREEN
from car import Car
from functions import (change_speeds, reset_speeds, avoid_collisions,
                       collect_telemetry, fluctuate_speeds, draw_lane_markings, 
                       load_car_asset_images, write_telemetry)

# initialize Pygame
pygame.init()

# set screen dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulator")

# load assets
CAR_IMAGES = load_car_asset_images(CAR_ASSETS_DIR, CAR_IMAGE_FILENAMES)

# Resize car images
car_images = [pygame.transform.scale(img, (35, 60)) for img in CAR_IMAGES]

# Telemetry
telemetry_data = []

# Initialize cars
cars = [Car(angle=i * (360 / NUM_CARS),
            speed=NORMAL_SPEED,
            image=random.choice(car_images)) for i in range(NUM_CARS)]

# Simulation variables
run = True
clock = pygame.time.Clock()
time_counter = 0
speed_change_interval = 18000  # Frames
reset_speed_interval = 200
fluctuation_interval = 60

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(GRASSY_GREEN)

    # Draw the roundabout
    pygame.draw.circle(screen, ROAD_COLOR, (WIDTH // 2, HEIGHT // 2), RADIUS + 40)
    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), RADIUS - 40)

    # Draw lane markings
    draw_lane_markings(screen=screen)
    # Update and draw cars
    for car in cars:
        car.update()
        car.draw(screen=screen)

    # Avoid collisions
    avoid_collisions(cars=cars)

    # Collect telemetry data
    collect_telemetry(telemetry_data=telemetry_data, cars=cars, time_counter=time_counter)
    # Random speed fluctuations
    if time_counter % fluctuation_interval == 0:
        fluctuate_speeds(cars)

    # Check for speed changes
    if time_counter % speed_change_interval == 0:
        change_speeds(cars)
        # Schedule the next speed change and reset intervals
        speed_change_interval = random.randint(400, 600)
        reset_speed_interval = random.randint(100, 200)
    elif time_counter % speed_change_interval == reset_speed_interval:
        reset_speeds(cars)

    time_counter += 1
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# Save telemetry data to CSV
write_telemetry(TELEMETRY_FILE, telemetry_data)

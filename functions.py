"""
Author: Mubarak Idoko
Date: 2024-06-08

Function Definitions
"""

# import libraries
import random
import os
import math
import csv
from typing import List, Tuple
import pygame

# import from project
from constants import (SLOW_SPEED, FAST_SPEED, NORMAL_SPEED, COLLISION_DISTANCE,
                       NUM_CARS, MIN_FLUCTUATION, MAX_FLUCTUATION, WIDTH, HEIGHT, RADIUS)
from colors import LANE_MARKINGS_COLOR
from car import Car

def draw_lane_markings(screen: pygame.Surface):
    """Draw lane markings for road on the screen

    Args:
        screen (pygame.Surface): The pygame screen to draw on
    """
    dash_length = math.pi / 20  # length of each dash in radians
    gap_length = math.pi / 40   # length of each gap in radians
    for i in range(0, int(2 * math.pi / (dash_length + gap_length))):
        start_angle = i * (dash_length + gap_length)
        end_angle = start_angle + dash_length
        pygame.draw.arc(screen,
                        LANE_MARKINGS_COLOR,
                        [WIDTH // 2 - RADIUS - 5, HEIGHT // 2 - RADIUS - 5,
                            2 * RADIUS + 10, 2 * RADIUS + 10],
                        start_angle, end_angle, 8)

# Speed change function
def change_speeds(cars: List[Car]):
    """Change the speeds of cars

    Args:
        cars (List[Car]): Cars current in the simulation
    """
    slow_cars = random.sample(cars, 2)
    fast_cars = random.sample([car for car in cars if car not in slow_cars], 2)
    for car in slow_cars:
        car.speed = SLOW_SPEED
    for car in fast_cars:
        car.speed = FAST_SPEED

# Reset speeds function
def reset_speeds(cars: List[Car]):
    """Reset the speeds of cars to normal

    Args:
        cars (List[Car]): Cars current in the simulation
    """
    for car in cars:
        car.speed = NORMAL_SPEED

def fluctuate_speeds(cars: List[Car]):
    """Fluctuate the speeds of cars

    Args:
        cars (List[Car]): Cars current in the simulation
    """
    for car in cars:
        fluctuation = random.uniform(MIN_FLUCTUATION, MAX_FLUCTUATION)
        car.speed = max(0.5, car.speed + fluctuation)

# Collision avoidance function
def avoid_collisions(cars: List[Car]):
    """Prevent cars from colliding with each others 
        i.e. force them to maintain a minimum distance by slowing down

    Args:
        cars (List[Car]): Cars current in the simulation
    """
    for i in range(NUM_CARS):
        car = cars[i]
        next_car = cars[(i + 1) % NUM_CARS]
        if distance(car.position(), next_car.position()) < COLLISION_DISTANCE:
            car.speed = min(car.speed, next_car.speed)

# Distance calculation
def distance(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float:
    """Calculate the distance between two points

    Args:
        pos1 (Tuple[float, float]): The first point
        pos2 (Tuple[float, float]): The second point

    Returns:
        float: The distance between the two points
    """
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Telemetry collection function
def collect_telemetry(telemetry_data: list, cars: List[Car], time_counter: int):
    """Collect telemetry data for the simulation

    Args:
        telemetry_data (list): Telemetry data collected so far
        cars (List[Car]): Cars current in the simulation
        time_counter (int): Simulation time counter
    """
    for i, car in enumerate(cars):
        telemetry_data.append({
            'time': time_counter,
            'car_id': i,
            'angle': car.angle,
            'speed': car.speed,
            'x': car.position()[0],
            'y': car.position()[1]
        })

def write_telemetry(telemetry_file_path: str, telemetry_data: list):
    """Write telemetry data to a CSV file

    Args:
        telemetry_data (list): Telemetry data collected so far
    """
    with open(telemetry_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['time', 'car_id', 'angle', 'speed', 'x', 'y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in telemetry_data:
            writer.writerow(data)
         
def load_car_asset_images(directory: str, filenames: list) -> list:
    """Load car asset images for simulation

    Args:
        directory (str): path to the directory containing the images
        filenames (list): list of car image filenames

    Returns:
        list: collection of car images
    """
    return [pygame.image.load(f"{directory}{filename}") for filename in filenames]

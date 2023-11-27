import random

class ParkingSpace:
    def __init__(self, total_area, spot_length=8, spot_width=12):
        self.spot_length = spot_length
        self.spot_width = spot_width
        self.available_spots = total_area // (spot_length * spot_width)
        self.spot_list = [None] * self.available_spots

    def occupy_spot(self, car, spot):
        if self.spot_list[spot] is None:
            self.spot_list[spot] = car
            return f"Car with license plate {car} parked successfully in spot {spot}"
        else:
            return f"Spot {spot} is occupied. Car with license plate {car} could not be parked."

class Automobile:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"{self.license_plate}"

    def park(self, parking_space):
        spot = random.randint(0, len(parking_space.spot_list) - 1)
        return parking_space.occupy_spot(str(self), spot)

def main():
    parking_area_size = 2000  # Change this value as needed
    car_license_plates = ["ABC1234", "DEF5678", "GHI9012", "JKL3456", "MNO7890"]

    parking_space = ParkingSpace(parking_area_size)

    automobiles = [Automobile(license_plate) for license_plate in car_license_plates]

    while automobiles and parking_space.available_spots > 0:
        random.shuffle(automobiles)
        automobile = automobiles.pop()
        result = automobile.park(parking_space)
        print(result)

    if parking_space.available_spots == 0:
        print("Parking space is full.")

if __name__ == "__main__":
    main()

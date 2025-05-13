#type:ignore
from datetime import datetime, timedelta

class car:
    def __init__(self, car_id, model, daily_rate, available=True):
        self.car_id = car_id
        self.model = model
        self.daily_rate = daily_rate
        self.available = available
    
    def __str__(self):
        status = "Available" if self.available else "Rented"
        return f"Car ID: {self.car_id}, Model: {self.model}, Daily Rate: ${self.daily_rate}, Status: {status}"

class Rental:
    def __init__(self, car, customer_name, days_rented):
        self.car = car
        self.customer_name = customer_name
        self.days_rented = days_rented
        self.rental_date = datetime.now()
        self.return_date = self.rental_date + timedelta(days=days_rented)
        self.total_cost = self.car.daily_rate * self.days_rented
        self.returned = False
    
    def mark_returned(self):
        self.car.available = True
        self.returned = True
    
    def __str__(self):
        status = "Returned" if self.returned else "Not Returned"
        return f"Customer: {self.customer_name}, Car ID: {self.car.car_id}, Rental Date: {self.rental_date}, Return Date: {self.return_date}, Total Cost: ${self.total_cost}, Status: {status}"

class RentalSystem:
    def __init__(self):
        self.cars = []
        self.rentals = []
    
    def add_car(self, car):
        if car.car_id not in [c.car_id for c in self.cars]:
            self.cars.append(car)
        else:
            print(f"Car with ID {car.car_id} already exists.")
    
    def display_cars(self):
        for car in self.cars:
            print(car)
    def rent_car(self, car_id, customer_name, days_rented):
        for car in self.cars:
            if car.car_id == car_id and car.available:
                car.available = False
                rental = Rental(car, customer_name, days_rented)
                self.rentals.append(rental)
                print(f"Car rented successfully ✅\n Rental details:\n{rental}")
                return
        print("Car not available for rent.")
    
    def return_car(self, car_id):
        for rental in self.rentals:
            if rental.car.car_id == car_id and not rental.returned:
                rental.mark_returned()
                print(f"Car returned successfully ✅\n Rental details:\n{rental}")
                return
        print("Car not found or already returned.")
        
def main():
    system = RentalSystem()
    system.add_car(car("1", "Toyota Camry", 50))
    system.add_car(car("2", "Honda Accord", 60))
    system.add_car(car("3", "Ford Focus", 40))
    system.add_car(car("4", "Chevrolet Malibu", 55))
    system.add_car(car("5", "Nissan Altima", 65))
    
    print("===============Welcome to the Car Rental System===============\n")
    while True:
        print("\nOptions:")
        print("1. Display available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            print("\nAvailable Cars:")
            system.display_cars()
        elif choice == "2":
            car_id = input("Enter the car ID to rent: ")
            customer_name = input("Enter your name: ")
            days_rented = int(input("Enter the number of days to rent: "))
            system.rent_car(car_id, customer_name, days_rented)
        elif choice == "3":
            car_id = input("Enter the car ID to return: ")
            system.return_car(car_id)
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()

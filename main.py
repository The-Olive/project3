class AirplaneSeating:
    def __init__(self):
        # Initialize seating chart: F (First-Class), E (Emergency), R (Regular)
        self.seats = [
            ["F1", "F2", "F3", "F4"],
            ["F5", "F6", "F7", "F8"],
            ["E1", "E2", "E3", "E4"],
            ["E5", "E6", "E7", "E8"],
            ["R1", "R2", "R3", "R4"]
        ]
        self.taken_seats = []
        self.first_class_fee = 50.0

    def display_seats(self):
        print("\nCurrent Seating Chart:")
        for row in self.seats:
            print(" | ".join(["[X]" if seat in self.taken_seats else seat for seat in row]))
        print()

    def is_seat_available(self, seat):
        return seat not in self.taken_seats

    def prompt_emergency_acceptance(self):
        while True:
            response = input("Emergency row seats require you to assist in case of an emergency. Do you accept? (yes/no): ").strip().lower()
            if response == "yes":
                return True
            elif response == "no":
                return False
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

    def book_seats(self):
        self.display_seats()
        while True:
            try:
                num_seats = int(input("How many seats would you like to purchase? "))
                if num_seats <= 0 or num_seats > 20:
                    print("Please enter a valid number of seats.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        total_cost = 0

        for _ in range(num_seats):
            self.display_seats()
            seat = input("Enter the seat you want to purchase (e.g., F1, E1, R1): ").strip().upper()
            if not any(seat in row for row in self.seats):
                print("Invalid seat. Please try again.")
                continue

            if not self.is_seat_available(seat):
                print("Seat is already taken. Please select another seat.")
                continue

            if seat.startswith("F"):
                total_cost += self.first_class_fee
                print(f"{seat} is a First-Class seat. A fee of ${self.first_class_fee:.2f} applies.")
            elif seat.startswith("E"):
                if not self.prompt_emergency_acceptance():
                    print("You must accept responsibility to book an emergency row seat.")
                    continue

            self.taken_seats.append(seat)
            print(f"{seat} successfully booked.")

        print(f"\nBooking complete. Total cost: ${total_cost:.2f}")
        self.display_seats()


def main():
    print("Welcome to the Airplane Seat Booking System!")
    plane = AirplaneSeating()

    while True:
        plane.book_seats()
        cont = input("Would you like to book more seats? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Thank you for using the booking system. Have a nice flight!")
            break


if __name__ == "__main__":
    main()
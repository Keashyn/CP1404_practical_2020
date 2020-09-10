from Prac_08.taxi import Taxi


def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(40)
    print(my_taxi)
    print("Total cost of trip ${:.2f}".format(my_taxi.get_fare()))


main()
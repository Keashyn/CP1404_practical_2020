
"Testing for Sliver service Taxi."
from Prac_08.sliver_serivce_taxi import SliverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SliverServiceTaxi("Lexus", 100, 8)
    taxi.drive(20)
    print(taxi)
    taxi.add_fuel(8)
    print(taxi.get_fare())
main()
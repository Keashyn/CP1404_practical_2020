from Prac_08.taxi import Taxi
def main():
    bmw=Taxi("Bmw 1", 100)
    bmw.drive(40)
    print(bmw)
    print("Fair cost's ${:.2f}".format(bmw.get_fare()))
    bmw.start_fare()
    bmw.drive(100)
    print(bmw)
    print("Fair cost's ${:.2f".format(bmw.get_fare()))
main()
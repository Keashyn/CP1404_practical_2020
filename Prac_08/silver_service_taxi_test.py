from Prac_08.silver_taxi_service import Silver_Service_Taxi
def main():
    hummer=Silver_Service_Taxi("hamme",20,2)
    hummer.drive(18)
    print(hummer)
    print("${:.2f}".format(hummer.get_fare()))
main()
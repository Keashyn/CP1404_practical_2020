from Prac_08.silver_Service_taxi import SilverTaxiService
def main():
    hummer=SilverTaxiService("hamme",20,2)
    hummer.drive(18)
    print(hummer)
    print("${:.2f}".format(hummer.get_fare()))
main()
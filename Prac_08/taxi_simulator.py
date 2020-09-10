from Prac_08.silver_Service_taxi
import SilverServiceTaxi
from Prac_08.taxi \
import Taxi
def main():
    Menu="C: Choose Taxi\nD:Drive\nQ:Quit"
    taxies=[Taxi("Bmw",100),SilverTaxiService("Truck",100,2),SilverSeviceTaxi("Hummer",200,4)]
    fare=0
    print(Menu)
    user_choice=input(">>>").upper()
    while user_choice != "Q":
        if user_choice =="C":
            taxi_number=0
            print("Taxi's are avalaiable")
            for taxi in taxies:
                print("{}-{}".format(taxi_number,taxi))
                taxi_number +=1
            taxi_choice=int(input("Choose Taxi:"))
            print("Bill to date ${:.2f}".format(fare))
        elif user_choice =="D":
            distance=int(input("Drive how far?"))
            taxies[taxi_choice].drive(distance)
            fare+=taxies[taxi_choice].get_fuel()
            print("Your taxi will cost you ${:.2f}".format(fare))
        print(Menu)
        user_choice=input(">>>")
    print("Total trip of cost is ${:.2f}".format(fare))
    print("Taxi's are now:")
    for taxi in taxies:
        taxi_number=0
        print("{}-{}".format(taxi_number,taxi))
        taxi_number++1
        """elif user_choice == "D":"""
main()


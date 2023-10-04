import pandas as pd

df = pd.read_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 11-Hotel Booking App\data\hotels.csv",
                 dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 11-Hotel Booking App\data\hotels.csv", index=False)

    def available(self):
        """Check the availability of the hotel with hotel_id"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation !!
        Name  : {self.customer_name},
        Hotel : {self.hotel.name}
 """
        return content


print(df.head(5))
hotel_id = input("Enter the id of the Hotel : ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    customer_name = input("Enter your name")
    reserve_ticket = ReservationTicket(customer_name, hotel)
    print(reserve_ticket.generate())
else:
    print("Hotel is not free!!")

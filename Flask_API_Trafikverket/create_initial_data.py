from app import app, db
from models import User, Car

with app.app_context():
    db.create_all()

users_data = [
    {"first_name": "Anna", "last_name": "Svensson", "personal_number": "19701234-5678", "address": "Gatan 1, 123 45 Staden"},
    {"first_name": "Erik", "last_name": "Johansson", "personal_number": "19840516-1234", "address": "Vägen 2, 234 56 Byen"},
    {"first_name": "Lisa", "last_name": "Larsson", "personal_number": "19950720-2345", "address": "Stigen 3, 345 67 Kommunen"},
    {"first_name": "Johan", "last_name": "Andersson", "personal_number": "19890609-3456", "address": "Allén 4, 456 78 Församlingen"},
    {"first_name": "Maria", "last_name": "Karlsson", "personal_number": "19761230-4567", "address": "Boulevard 5, 567 89 Området"},
    {"first_name": "Niklas", "last_name": "Nilsson", "personal_number": "19980915-5678", "address": "Parkvägen 6, 678 90 Provinsen"},
    {"first_name": "Sofia", "last_name": "Eriksson", "personal_number": "19870913-5678", "address": "Brovägen 7, 789 01 Landskapet"},
    {"first_name": "Karl", "last_name": "Pettersson", "personal_number": "19910612-2345", "address": "Avenyn 8, 890 12 Regionen"},
    {"first_name": "Emma", "last_name": "Lundgren", "personal_number": "19980722-3456", "address": "Platsen 9, 901 23 Distriktet"},
    {"first_name": "Mikael", "last_name": "Berg", "personal_number": "19841228-4567", "address": "Lokalgatan 10, 012 34 Sektorn"}
    ]

# create and add users to the database
with app.app_context():
    users = []
    for data in users_data:
        # user = User(first_name=data["first_name"], 
        #     last_name=data["last_name"], 
        #     personal_number=data["personal_number"], 
        #     address=data["address"])
        user = User(**data) # **data to unpack dictionary
        db.session.add(user)
        users.append(user)  # save user objects in a list
    db.session.commit()  # commit to database

    # update users list with the user objects from the database
    for user in users:
        db.session.refresh(user)

# create cars data
cars_data = [
    {"brand": "Porsche", "model_name": "911 GT2 RS", "model_year": "2023", "color": "Green", "registration_plate": "XYZ123", "owner_id": users[0].id},
    {"brand": "Volvo", "model_name": "XC90", "model_year": "2021", "color": "Black", "registration_plate": "ABC123", "owner_id": users[0].id},
    {"brand": "Porsche", "model_name": "944 Turbo S", "model_year": "1988", "color": "Purple", "registration_plate": "SAA123", "owner_id": users[1].id},
    {"brand": "Datsun", "model_name": "240Z", "model_year": "1977", "color": "Red", "registration_plate": "TES123", "owner_id": users[1].id},
    {"brand": "BMW", "model_name": "M340i", "model_year": "2021", "color": "Grey", "registration_plate": "BMW123", "owner_id": users[2].id},
    {"brand": "Audi", "model_name": "Quattro", "model_year": "1980", "color": "Grey", "registration_plate": "AUD123", "owner_id": users[3].id},
    {"brand": "Mercedes-Benz", "model_name": "300 SL", "model_year": "1954", "color": "Silver", "registration_plate": "MER123", "owner_id": users[4].id},
    {"brand": "Lancia", "model_name": "Delta HF Integrale", "model_year": "1993", "color": "Blue", "registration_plate": "FOR123", "owner_id": users[5].id},
    {"brand": "Toyota", "model_name": "Supra", "model_year": "2002", "color": "White", "registration_plate": "TOY123", "owner_id": users[6].id},
    {"brand": "Honda", "model_name": "NSX-R", "model_year": "2002", "color": "Black", "registration_plate": "HON123", "owner_id": users[7].id},
    {"brand": "Mazda", "model_name": "RX-7 Spirit R", "model_year": "2002", "color": "Blue", "registration_plate": "SKO123", "owner_id": users[8].id},
    {"brand": "Nissan", "model_name": "Skyline GT-R V·Spec II Nür", "model_year": "2002", "color": "Purple", "registration_plate": "NIS123", "owner_id": users[9].id},
    {"brand": "Hyundai", "model_name": "i30 N", "model_year": "2017", "color": "Blue", "registration_plate": "HYU123", "owner_id": users[5].id},
    {"brand": "Audi", "model_name": "RS6", "model_year": "2017", "color": "Black", "registration_plate": "PEU123", "owner_id": users[6].id},
    {"brand": "Abarth", "model_name": "500 Competizione", "model_year": "2018", "color": "Yellow", "registration_plate": "FIA123", "owner_id": users[4].id}
    ]

# create and add cars to the database
with app.app_context():
    for data in cars_data:
        car = Car(**data) 
        db.session.add(car)
    db.session.commit()  

print("Database has been created and has been populated with initial data.")

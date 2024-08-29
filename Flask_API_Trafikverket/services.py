from models import db, User, Car

# statiska metoder gör att man kan anropa dessa metoder, 
# utan att behöva skapa en instans av klassen. 
# vilket förenklar åtkomsten och gör koden mer modulär och lätt att använda


class UserService:
    @staticmethod 
    def get_all_users():
        return [user.to_dict() for user in User.query.all()]

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.filter_by(id=user_id).first() 
        return user.to_dict() if user else None

    @staticmethod
    def create_user(data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

    @staticmethod
    def update_user(user_id, data):
        user = User.query.filter_by(id=user_id).first()
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            db.session.commit()
            return user.to_dict()
        return None

    @staticmethod
    def delete_user(user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

class CarService:
    @staticmethod
    def get_all_cars():
        return [car.to_dict() for car in Car.query.all()]

    @staticmethod
    def get_car_by_id(car_id):
        car = Car.query.filter_by(id=car_id).first()
        return car.to_dict() if car else None

    @staticmethod
    def create_car(data):
        car = Car(**data)
        db.session.add(car)
        db.session.commit()
        return car.to_dict()

    @staticmethod
    def update_car(car_id, data):
        car = Car.query.filter_by(id=car_id).first()
        if car:
            for key, value in data.items():
                setattr(car, key, value if value is not None else getattr(car, key)) # setattr och getattr används för att sätta och hämta attribut på objektet car 
            db.session.commit()
            return car.to_dict()
        return None

    @staticmethod
    def delete_car(car_id):
        car = Car.query.filter_by(id=car_id).first()
        if car:
            db.session.delete(car)
            db.session.commit()
            return True
        return False

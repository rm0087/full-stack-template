from config import app, db
from models import Person



if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        

        print("Seeding complete!")

        
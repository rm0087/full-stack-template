from flask import request
from config import app, db
from models import db, Person

with app.app_context():
    pass

# USER SIGNUP #

# CHECK SESSION #

# SESSION LOGIN/LOGOUT #

# EXAMPLE OTHER RESOURCES #.

# APP RUN #
if __name__ == '__main__':
    app.run(port=5555, debug=True)



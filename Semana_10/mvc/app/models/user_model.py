from database import db

class User(db.Model):
    __tablename__ = 'users'
    #definimos las columnas
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    def __init__(self, first_name,last_name, email, password, date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date = date
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #los query's de usuario van aquí!!
    @staticmethod
    def get_all():
        return User.query.all()
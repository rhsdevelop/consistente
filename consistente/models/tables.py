from consistente import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def __init__(self, username, password, name, email, phone, active):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.active = active
        self.db = db
    
    def __repr__(self):
        return '<User %r>' % self.username

    def get_id(self):
        return str(self.id)

    def verify_password(self, pwd):
        return self.password == pwd
    
    def save(self):
        db.session.commit()

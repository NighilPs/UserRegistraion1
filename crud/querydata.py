from sqlalchemy.orm import Session
from models.properties import User



def get_user(db: Session):
    return db.query(User).all()

def post_user(db:Session,full_name,password,email,phone):
    email_exist = db.query(User).filter(User.email == email).first()
    if not email_exist:
        data = User(full_name = full_name,password = password,email=email,phone=phone)
        db.add(data)
        db.commit()
        return data.id
    return False

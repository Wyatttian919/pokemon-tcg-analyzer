from app.core.database import SessionLocal
from app.models.user import User


db = SessionLocal()


user = db.query(User).filter(
    User.id == 1
).first()


if user:
    db.delete(user)

    db.commit()

    print("User deleted!")

else:
    print("User not found")


db.close()
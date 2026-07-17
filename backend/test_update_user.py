from app.core.database import SessionLocal
from app.models.user import User


db = SessionLocal()


user = db.query(User).filter(
    User.id == 1
).first()


if user:
    user.email = "new@example.com"

    db.commit()

    print("User updated!")

else:
    print("User not found")


db.close()
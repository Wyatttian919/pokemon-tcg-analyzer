from app.core.database import SessionLocal
from app.models.user import User

db = SessionLocal()

user = User(
    username="yaotian",
    email="yaotian@example.com",
    password_hash="hashed_password"
)


db.add(user)
db.commit()
db.close()

print("User created!")
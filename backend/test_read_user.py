from app.core.database import SessionLocal
from app.models.user import User


db = SessionLocal()


user = db.query(User).first()


print(user.username)
print(user.email)


db.close()
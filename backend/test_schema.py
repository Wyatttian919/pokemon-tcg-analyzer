from app.schemas.user import UserCreate


user = UserCreate(
    username="yaotian",
    email="test@example.com",
    password="123456"
)


print(user)
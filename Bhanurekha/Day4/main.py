def user_received(user: User):
    return {
        "message": "user received successfully",
        "name": user.name,
        "age": user.age
    }
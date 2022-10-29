from fastapi import APIRouter

userRouter = APIRouter()


@userRouter.post("/users")
def Store(user: User):
    newUser = {"id": user.id, "name": user.name,
               "email": user.email, "password": user.password}
    conn.execute(users.insert().values(newUser))
    return conn.execute(users.select().where(users.c.id == user.id)).first()

@userRouter.delete("/users/{id}")
def Delete(id):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=OK)
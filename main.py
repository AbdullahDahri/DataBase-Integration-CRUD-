from fastapi import FastAPI,Depends
from schemas import UserCreate, UserUpdate, UserResponse
from sqlalchemy.orm import Session
from database import SessionLocal,engine,Base
from models import users
app=FastAPI()
Base.metadata.create_all(bind=engine)
app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message":"Welcome to User Management API"}


@app.get("/user",response_model=list[UserResponse])
def get_user(db:Session=Depends(get_db)):
    user=db.query(users).all()
    return user

@app.get("/user/{id}",response_model=UserResponse)
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    user=db.query(users).filter(users.id==id).first()
    if not user:
        return {"message":"User not found"}
    return user
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(users).filter(
        users.email == user.email
    ).first()

    if existing_user:
        return {"message": "Email already exists"}

    new_user = users(
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(users).filter(
        users.id == user_id
    ).first()

    if not user:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}

@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    updated_user: UserCreate,
    db: Session = Depends(get_db)
):

    user = db.query(users).filter(
        users.id == user_id
    ).first()

    if not user:
        return {"message": "User not found"}

    user.name = updated_user.name
    user.email = updated_user.email
    user.age = updated_user.age

    db.commit()

    return {
        "message": "User updated successfully",
        "user": user
    }

@app.patch("/users/{user_id}")

def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db)
):

    user = db.query(users).filter(
        users.id == user_id
    ).first()

    if not user:
        return {"message": "User not found"}

    if updated_user.name is not None:
        user.name = updated_user.name

    if updated_user.email is not None:
        user.email = updated_user.email

    if updated_user.age is not None:
        user.age = updated_user.age

    db.commit()

    return {
        "message": "User updated successfully",
        "user": user
    }
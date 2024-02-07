from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User
from app.database.connection import conn

router = APIRouter()

@router.get("/users", response_model=List[User])
async def read_users():
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()
    cursor.close()
    return [{"id": user[0], "username": user[1], "email": user[2]} for user in users]

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    if user_data:
        user = User(id=user_data[0], username=user_data[1], email=user_data[2])
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/users/", response_model=User)
async def create_user(user: User):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (user.username, user.email))
    conn.commit()
    user.id = cursor.lastrowid
    cursor.close()
    return user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = %s, email = %s WHERE id = %s", (user.username, user.email, user_id))
    conn.commit()
    cursor.close()
    user.id = user_id
    return user

@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    return {"message": "User deleted successfully"}

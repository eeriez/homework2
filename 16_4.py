from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=2, max_length=20, description='Enter username',
                                                    example='User1')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='20')]
                      ):

    if len(users) == 0:
        user.id = 1
    else:
        max = 0
        for user in users:
            if user.id > max:
                max = user.id
        user.id = max + 1
    user.username = username
    user.age = age
    users.append(user)

    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter ID', example='25')],
        username: Annotated[str, Path(min_length=2, max_length=20, description='Enter username', example='User1')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='20')]):

    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter ID', example='25')]):

    try:
        for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail='User was not found')
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

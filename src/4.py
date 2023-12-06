from datetime import datetime

from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


some_api_response = {
    "id": 123,
    "signup_ts": "2019-06-01 12:22",
    "tastes": {
        "wine": 9,
        b"cheese": 7,
        "cabbage": "1",
    },
}

user = User(**some_api_response)

print(user)

some_bad_data = {
    "id": "John Doe",
    "signup_ts": "last Tuesday",
    "tastes": {
        "i hate tomatoes": -1337,
    },
}

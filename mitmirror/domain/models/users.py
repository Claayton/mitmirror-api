"""interface de tupla nomeada para User"""
from collections import namedtuple


User = namedtuple(
    "User",
    [
        "id",
        "name",
        "email",
        "username",
        "password_hash",
        "secundary_id",
        "is_staff",
        "is_active_user",
        "last_login",
        "date_joined",
    ],
)

from voluptuous import Schema, PREVENT_EXTRA


user_schema = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

number_user_schema = Schema(
    {
        "data": user_schema,
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

list_users_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user_schema],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

resource_schema = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

list_resource_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [resource_schema],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)



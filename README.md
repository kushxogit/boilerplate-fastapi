## Basic folder structure

I have structured our project into two modules: src and test:
```
.
└── backend/
    ├── src/
    │   ├── config/
    │   ├── routes/
    │   ├── util/
    │   └── __init__.py
    ├── test/
    │   ├── routes/
    │   ├── test_util/
    │   ├── __init.py__
    │   ├── app_test.py
    │   └── conftest.py
    ├── main.py
    └── requirements.txt
```

For Backend Development, We will be focusing on the folder `routes` and I have structured it below
```
.
└── backend/
    └── src/
        └── routes/
            ├── auth/
            │   ├── internal/
            │   │   ├── auth_reader.py
            │   │   └── auth_writer.py
            │   ├── rest_api/
            │   │   └── auth_controller.py
            │   ├── store/
            │   │   ├── auth_models.py
            │   │   └── auth_schemas.py
            │   ├── auth_main.py
            │   └── auth_service.py
            ├── users
            ├── bookings
            ├── rooms
            └── __init__.py
```

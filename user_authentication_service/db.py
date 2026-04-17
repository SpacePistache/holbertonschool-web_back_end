def add_user(self, email: str, hashed_password: str):
    """Add a new user to the database"""

    user = User(email=email, hashed_password=hashed_password)

    self._session.add(user)
    self._session.commit()

    return user

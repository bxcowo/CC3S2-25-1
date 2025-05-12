from _pytest.fixtures import showfixtures
from typing_extensions import DefaultDict


class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class UserManager:
    def __init__(self, hash_service=None, repo=None, email_service=None) -> None:
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()
        self.email_service = email_service

    def _default_hash_service(self):
        class DefaultHashService:
            def hash(self, plain_text: str) -> str:
                return plain_text

            def verify(self, plain_text: str, hashed_text: str) -> bool:
                return plain_text == hashed_text

        return DefaultHashService()

    def _default_repo(self):
        class InternalRepo:
            def __init__(self) -> None:
                self.data = {}

            def save_user(self, username, hashed_pw):
                if self.exists(username):
                    raise UserAlreadyExistsError(f"{username} ya existe.")
                self.data[username] = hashed_pw

            def get_user(self, username):
                return self.data.get(username)

            def exists(self, username):
                return username in self.data

        return InternalRepo()

    def add_user(self, username, password):
        hashed_pw = self.hash_service.hash(password)
        self.repo.save_user(username, hashed_pw)
        if self.email_service:
            self.email_service.send_welcome_email(username)

    def user_exists(self, username):
       return self.repo.exists(username)

    def authenticate_user(self, username, password):
        stored_hash = self.repo.get_user(username)
        if stored_hash is None:
            raise UserNotFoundError(f"El usuario {username} no existe")
        return self.hash_service.verify(password, stored_hash)

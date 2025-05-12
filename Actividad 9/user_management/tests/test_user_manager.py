import pytest
from user_management.user_manager import UserManager, UserAlreadyExistsError
from unittest.mock import MagicMock


def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "bxco"
    password = "unova4ever"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado"

class FakeHashService:
    """Servicio 'fake' que devuelve un hash simplificado con un prefijo, y lo verifica"""
    def hash(self, plain_text: str) -> str:
        return f"fakehash: {plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash: {plain_text}"

def test_autenticar_usuario_existoso_con_hash():
    # Arrange
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "bxco"
    password = "unovaever"
    manager.add_user(username, password)

    # Act
    autenticado = manager.authenticate_user(username, password)

    # Assert
    assert autenticado, "El usuario debería autenticarse correctamente con la contraseña correcta"

def test_hash_service_es_llamado_al_agregar_usuario():
    # Arrange
    mock_hash_service = MagicMock()
    manager = UserManager(hash_service=mock_hash_service)
    username = "bxco"
    password = "unova4ever"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_hash_service.hash.assert_called_once_with(password)

def test_no_se_puede_agregar_usuario_existente_stub():
    # Arrange
    class StubUserRepo(InMemoryUserRepository):
        def exists(self, username):
            return True

    stub_manager = UserManager(repo=StubUserRepo())
    # Act
    with pytest.raises(UserAlreadyExistsError) as exc:
        stub_manager.add_user("cualquier", "1234")

    # Assert
    assert "ya existe" in str(exc.value)

class InMemoryUserRepository:
    """Fake de repositorio en memoria"""
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

def test_inyectar_repositorio_inmemory():
    # Arrange
    repo = InMemoryUserRepository()
    manager = UserManager(repo=repo)
    username = "bxco"
    password = "unova4ever"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username)

def test_envio_correo_bienvenida_al_agregar_usuario():
    # Arrange
    mock_email_service = MagicMock()
    manager = UserManager(email_service=mock_email_service)
    username = "bxco"
    password = "unova4ever"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_email_service.send_welcome_email.assert_called_once_with(username)

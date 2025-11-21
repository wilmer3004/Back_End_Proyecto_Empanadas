from abc import ABC, abstractmethod

class Auth_Interface(ABC):
    """
    Interface for authentication services.
    Defines the required methods that any Auth Service must implement.
    """

    @abstractmethod
    def login_user(self, user_name: str, password_user: str):
        """
        Authenticate a user and return user data or an error.
        
        :param user_name: The username of the user.
        :param password_user: The user's password.
        :return: Dictionary with user data or error message.
        """
        pass

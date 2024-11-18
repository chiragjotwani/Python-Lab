class PasswordManager:
    def __init__(self):
        self.__password = None  # Private attribute to store the password

    def set_password(self, password):
        """Set the password."""
        self.__password = password

    def get_password(self):
        """Get the password."""
        return self.__password

if __name__ == "__main__":
    pm = PasswordManager()
    
    pm.set_password("my_secure_password")
    
    print("The password is:", pm.get_password())
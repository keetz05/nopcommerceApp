import configparser
config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def get_application_url():
        URL =config.get('common info','baseUrl')
        return URL
    @staticmethod
    def get_username():
        username = config.get('common info','Email')
        return username
    @staticmethod
    def get_password():
        password = config.get('common info','password')
        return password

    @staticmethod
    def get_first_name():
        first_name = config.get('reg info','firstname')
        return first_name
    @staticmethod
    def get_last_name():
        last_name = config.get('reg info','lastName')
        return last_name
    @staticmethod
    def get_email():
        email = config.get('reg info','Email')
        return email
    @staticmethod
    def get_phone():
        phone = config.get('reg info','telephone')
        return phone
    @staticmethod
    def get_Password_fields():
        password = config.get('reg info','Password_fields')
        return password
    @staticmethod
    def get_confirm_password():
        confirm_password = config.get('reg info','confirm_password')
        return confirm_password




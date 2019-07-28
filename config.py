import os

basedir = os.path.abspath(os.path.dirname(__file__))   # you are here


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    import socket
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "no key defined"

    # Mail Settings

    # DB Settings

    # Other app settings to set or retrieve from os envs
    BOOTSTRAP_SERVE_LOCAL = True if not internet() else False
    print(" * Bootstrap service is local: {}".format(str(BOOTSTRAP_SERVE_LOCAL)))

    @staticmethod
    def init_app(app):
        """
        Add in additional application wide configs here
        :param app:
        :return: Nothing
        """
        pass


# Add in various configurations as subclasses of Config
class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


# Create a dictionary for class configurations
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
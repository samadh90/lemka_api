from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    """Classe Google pour récupérer les informations de l'utilisateur et les renvoyer"""

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the Google oAUTH2 api to fetch the user info
        """
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request())

            if 'accounts.google.com' in idinfo['iss']:
                return idinfo

        except:
            return "Le jeton est invalide ou a expiré"

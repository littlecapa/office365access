"""
Object for all functions dealing with Onedrive
"""
import msal, requests

GRAPH_AUTHORITY_URL = "https://login.microsoftonline.com/consumers/"
GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0/me/"
DEFAULT_SCOPES = ["User.Read", "User.Export.All, Files.ReadWrite.All"]

class onedriveAccess:

    def __init__(self, authUrl = GRAPH_AUTHORITY_URL, baseUrl = GRAPH_BASE_URL, scopes = DEFAULT_SCOPES):
        self.authUrl = authUrl
        self.baseUrl = baseUrl
        self.scopes = scopes

    def setIds(self, clientId, secret):
        self.clientId = clientId
        self.secret = secret
        self.setAuthUrl()
        
    def setAuthUrl(self):
        self.client_instance = msal.ConfidentialClientApplication(
            client_id = self.clientId,
            client_credential = self.secret,
            authority = self.authUrl)
        self.authorization_request_url = self.client_instance.get_authorization_request_url(self.scopes)

    def getAuthUrl(self):
        return self.authorization_request_url

    def setTokenFromRequest(self, request):
        self.authorization_code = request.GET["code"]
        self.tokenDictionary = self.client_instance.acquire_token_by_authorization_code(code=self.authorization_code, scopes=self.scopes)
        self.access_token = self.tokenDictionary["access_token"]
        self.refresh_token = self.tokenDictionary["refresh_token"]
        self.name = self.tokenDictionary["id_token_claims"]["name"]
        print (self.access_token)
        print (self.refresh_token)

    def getToken(self):
        return self.access_token, self.refresh_token
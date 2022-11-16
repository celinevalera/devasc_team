from .heart import HeartApi,HeartsApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(HeartsApi, "/api/hearts")
    api.add_resource(HeartApi, "/api/hearts/<id>")
    api.add_resource(SignupApi, "/api/auth/signup")
    api.add_resource(LoginApi, "/api/auth/login")
BASE_URL = "http://127.0.0.1:8000"

CREATE_URL = f"{BASE_URL}/employee/create"
INFO_URL   = f"{BASE_URL}/employee/info"
CHANGE_URL = f"{BASE_URL}/employee/change"
LOGIN_URL  = f"{BASE_URL}/auth/login"


# ASSUMPTION: no /docs schema was reachable while writing this, so these
# default credentials and payload fields are guesses based on the CompanyApi
# pattern taught in the lesson. Confirm against Swagger (`/openapi.json`) or
# a real 422 response once the server is reachable, then update here.
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"
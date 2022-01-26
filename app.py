# -*- coding: utf-8 -*-

from urllib.parse import parse_qs
from chalice import Chalice, AuthResponse
from my_package.lbd import hello, increment

app = Chalice(app_name="my_load_test_app")


@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.handler(event, context)


@app.authorizer()
def demo_auth(auth_request):
    token = auth_request.token
    if token == "allow":
        return AuthResponse(routes=["*"], principal_id="user")
    else:
        # By specifying an empty list of routes,
        # we're saying this user is not authorized
        # for any URLs, which will result in an
        # Unauthorized response.
        return AuthResponse(routes=[], principal_id='user')


@app.route("/", authorizer=demo_auth)
def index():
    return {"message": "Hello World!"}


@app.route(
    "/incr",
    methods=["POST", ],
    content_types=[
        "application/json",
    ],
    name="incr",
    authorizer=demo_auth,
)
def handler_increment():
    # {"key": "some_key"}
    response = increment.handler(app.current_request.json_body, None)
    return response

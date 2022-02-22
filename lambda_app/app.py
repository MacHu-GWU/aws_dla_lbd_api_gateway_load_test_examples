# -*- coding: utf-8 -*-

from chalice import Chalice, AuthResponse
from my_package import __chalice_app_name__
from my_package.lbd import hello, increment

# define a Chalice app
app = Chalice(app_name=__chalice_app_name__)


# a pure native lambda function
@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.handler(event, context)


@app.authorizer()
def demo_auth(auth_request):
    """
    Implement custom Authorization logic

    More details about built-in Custom Authorizer integration with Chalice
    can be found at https://aws.github.io/chalice/topics/authorizers.html?highlight=authorizer#built-in-authorizers
    """
    token = auth_request.token
    if token == "allow":
        return AuthResponse(routes=["*"], principal_id="user")
    else:
        # By specifying an empty list of routes,
        # we're saying this user is not authorized
        # for any URLs, which will result in an
        # Unauthorized response.
        return AuthResponse(routes=[], principal_id="user")


# define an API endpoint powered by AWS Lambda
@app.route(
    "/",
    methods=["GET", ],
    name="index",
    authorizer=demo_auth,
)
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
def incr():
    # expect {"key": "some_key"}
    event = app.current_request.json_body
    response = increment.handler(event, None)
    return response


# even though we already have a rest API handler, we want to have a pure lambda
# function version of it for testing without using API gateway
@app.lambda_function(name="increment")
def handler_increment(event, context):
    return increment.handler(event, None)

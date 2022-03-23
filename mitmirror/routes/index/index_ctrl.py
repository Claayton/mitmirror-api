def index():
    json_routes = {
        "/root/": {
            "Methods": "['GET']",
            "Action": "Returns a Hello message with username",
            "Required token": "True"
        },
        "/api/auth/": {
            "Methods": "['POST']",
            "Action": "Receive username and password in json format; Return the new token generated and its expiration time in json format",
            "Required token": "False"
        },
        "/api/users/": {
            "Methods": "['GET', 'POST']",
            "Action": {
                "['GET']": "Return data from all registered users",
                "['POST']": "Receives data in json format from the client to register a new user; Return the data again in json format, now with the encrypted password"
            },
            "Required token": "False"
        },
        "/api/users/<id>/": {
            "Methods": "['GET', 'PUT', 'DELETE']",
            "Action": {
                "['GET']": "Return data from a single user referenced by <id>",
                "['PUT']": "Updates data from a single user referenced by <id>",
                "['DELETE']": "Delete a user referenced by <id>"
            },
            "Required token": "False"
        }
    }
    return json_routes

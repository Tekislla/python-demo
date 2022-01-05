import jwt
import traceback


class AuthorizationClient:
    def verifyJwt(token):
        try:
            public_key = """-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg8ZurYJ1rtugQMbaSZvoGuIsWs1nBBU6Az+EUyb4qioD+g7a0FVy9HmeapsF5YvEpz353KAqvsQxVV5DVSTy+jRmW0oRLhuHU88Y4etfUN+9pXzsSBQv8OXshvQjpz5fS8NM1csz4BYoXlDnvhB0xXJbtC+d1IJXwJT98UxYLdobAAWOkyE7WXPHVkMO4q43I/da17rkFaZoCgCGe1hW8YXWJftWEX7HxYcQnXP0Ft+/F3oO5+R51u9Eb7SBLCzAbqsz5sFzNCUN1pe7pNGI7NK3t3+XcA6VkDHJZ/GSc4lQA1daL1SwmGATvpq7fy5tPMpaSsGJvcfW0IcWbYR69wIDAQAB\n-----END PUBLIC KEY-----"""
            jwt.decode(token, public_key, algorithms=['HS256', 'RS256'], audience='account')
            return 1
        except Exception:
            print(traceback.print_exc())
            return 0
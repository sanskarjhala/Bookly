from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from src.auth.utlis import decode_token
from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi import status


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        print("=-------------------CREDENTAILS---------------", creds)

        token = creds.credentials

        token_Data = decode_token(token=token)

        if not self.valid_token(token=token):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Access Token"
            )

        self.verify_token_data(token_data=token_Data)

        return creds

    def valid_token(self, token: str) -> bool:
        token_data = decode_token(token=token)
        print("------------------ TOKEN DATA -------------- ", token_data)
        if token_data is None:
            return False
        else:
            return True

    def verify_token_data(self, token_data):
        raise NotImplementedError("Please Override this method in child classes")


class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please Provide and access Token",
            )


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and not token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide refresh Token",
            )

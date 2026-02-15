from rest_framework import status
from rest_framework.response import Response


class SuccessResponse(Response):
    def __init__(
        self, data=None, message="Operation successful", status_code=status.HTTP_200_OK
    ):
        response = {"success": True, "message": message, "data": data}
        return super().__init__(response, status=status_code)


class ErrorResponse(Response):
    def __init__(
        self,
        error=None,
        message="Operation failed",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        response = {"success": False, "message": message, "error": error}
        return super().__init__(response, status=status_code)

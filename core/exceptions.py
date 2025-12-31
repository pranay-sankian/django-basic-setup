from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    NotAuthenticated,
    AuthenticationFailed,
    NotFound,
    APIException,
)
from rest_framework import status
from .api.utils import api_response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, NotAuthenticated):
        return api_response(
            success=False,
            message="Authentication token is missing",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    if isinstance(exc, AuthenticationFailed):
        return api_response(
            success=False,
            message="Invalid or expired authentication token",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    if isinstance(exc, NotFound):
        return api_response(
            success=False,
            message="Not Found",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    # Any other DRF-handled exception (403, 400, etc.)
    if isinstance(exc, APIException):
        return api_response(
            success=False,
            message=str(exc.detail),
            status_code=exc.status_code,
        )

    # Truly unhandled exceptions (500)
    if response is None:
        return api_response(
            success=False,
            message="Internal server error",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return response

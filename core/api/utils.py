from rest_framework.response import Response


def api_response(success, message=None, data=None, status_code=200):
    return Response(
        {
            "success": success,
            "message": message,
            "status_code": status_code,
            "data": data,
        },
        status=status_code,
    )

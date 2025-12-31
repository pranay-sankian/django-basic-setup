import time


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # run once when server starts

    def __call__(self, request):
        # runs before the view
        start_time = time.time()

        print(f"Incoming request {request.method} {request.path}")

        response = self.get_response(request)
        # view runs here

        # runs after the view
        duration = time.time() - start_time
        print(f"Response status: {response.status_code} | Time: {duration:2f}s")

        return response

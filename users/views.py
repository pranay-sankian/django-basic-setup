from rest_framework.response import Response
from rest_framework.decorators import action
# Used to create custom endpoints inside a ViewSet.

from rest_framework.viewsets import ModelViewSet
# Gives us CRUD APIs automatically.

from .models import CustomUser
from .serializer import CustomUserSerilizer

# A decorator is a function that modifies or extends another function or method without changing its original code.
# In Python, decorators are written using @.

# Create your views here.


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer

    @action(
        detail=False,
        methods=["get"],
        url_path="active",
        url_name="active-users",
    )
    def get_active_users(self, request):
        users = CustomUser.objects.filter(status="active")
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

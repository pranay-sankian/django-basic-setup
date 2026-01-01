from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, UserCreateSerializer

from .utils import api_response

from .pagination import UserPagination

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserListAPI(APIView):
    def get(self, request):
        if not request.user.is_superuser and request.user.id != id:
            return api_response(
                success=False,
                message="You do not have permission to access this user",
                status_code=403,
            )

        users = User.objects.all()

        # filters based on the email, first name and the last name

        email = request.GET.get("email")
        first_name = request.GET.get("first_name")
        last_name = request.GET.get("last_name")

        if email:
            users = users.filter(email__icontains=email)

        if first_name:
            users = users.filter(first_name__icontains=first_name)

        if last_name:
            users = users.filter(last_name__icontains=last_name)

        # pagination
        paginator = UserPagination()
        paginated_users = paginator.paginate_queryset(users, request)

        # serializer = UserSerializer(users, many=True)
        serializer = UserSerializer(
            paginated_users, many=True
        )  # getting the list so many=true

        message = "Users fetched successfully" if users.exists() else "No User found"

        return api_response(
            success=True,
            message=message,
            # data=serializer.data,
            data={
                "count": users.count(),
                "next": paginator.get_next_link(),
                "previous": paginator.get_previous_link(),
                "results": serializer.data,
            },
            status_code=status.HTTP_200_OK,
        )

    # create a new user
    def post(self, request):
        if not request.user.is_superuser and request.user.id != id:
            return api_response(
                success=False,
                message="You do not have permission to access this user",
                status_code=403,
            )

        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return api_response(
                success=True,
                message="User created successfully",
                data=UserSerializer(user).data,
                status_code=status.HTTP_201_CREATED,
            )

        return api_response(
            success=False,
            # message="username , email are required",
            status_code=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors,
        )


class UserDetailAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # get user by Id
    # request.user is cheked here id=id
    def get(self, request, id):
        if not request.user.is_superuser and request.user.id != id:
            return api_response(
                success=False,
                message="You do not have permission to access this user",
                status_code=403,
            )

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return api_response(
                success=False,
                message="User not Found",
                status_code=404,
            )

        serializer = UserSerializer(user)
        return api_response(
            success=True,
            message="User fetched successfully",
            data=serializer.data,
            status_code=200,
        )

    # update user by id (partial)
    def put(self, request, id):
        if not request.user.is_superuser and request.user.id != id:
            return api_response(
                success=False,
                message="You do not have permission",
                status_code=403,
            )

        user = User.objects.get(id=id)

        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return api_response(
                success=True,
                message="User updated successfully",
                data=serializer.data,
            )

        return api_response(
            success=False,
            message="Update Failed",
            data=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # delete user by id
    def delete(self, request, id):

        if not request.user.is_superuser and request.user.id != id:
            return api_response(
                success=False,
                message="You do not have permission",
                status_code=403,
            )

        try:
            user = User.objects.get(id=id)
            user.delete()
        except User.DoesNotExist:
            return api_response(
                success=False,
                message="User not Found",
                status_code=status.HTTP_404_NOT_FOUND,
            )

        return api_response(
            success=True,
            message="User deleted successfully",
            status_code=status.HTTP_204_NO_CONTENT,
        )

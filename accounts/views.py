from djoser.views import UserViewSet

signup = UserViewSet.as_view({"post": "create"})

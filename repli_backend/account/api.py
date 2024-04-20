from django.http import JsonResponse

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .forms import SignupForm


# Set the 'authentication_classes' and 'permission_classes' decorators to be empty so that we can access this view without being authenticated.
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data

    message = "success"

    form = SignupForm(
        {
            "email": data.get("email"),
            "name": data.get("name"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    if form.is_valid():
        form.save()
    else:
        message = "error"
        # message = form.errors.as_json()

    return JsonResponse({"message": message})
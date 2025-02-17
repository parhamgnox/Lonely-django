from rest_framework import serializers
from django.shortcuts import get_object_or_404
from acounts.models import CustomeUser


class ResetPasswordEmailSerializer(serializers.Serializer):
    """
    We write this class for reset pass word with email
    first we check the email and if is existed send email
    """

    email = serializers.CharField(label=("Email"), write_only=True)

    def validate(self, attrs):
        """
        this function check user email
        """
        user = get_object_or_404(CustomeUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs

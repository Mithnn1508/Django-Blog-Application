from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class userRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        if (validated_data["password"]!=validated_data["confirm_password"]):
            raise serializers.ValidationError("Password and Confirm Password not Matched")
        try:
            obj = User.objects.create_user(username=validated_data['username'],password=validated_data["password"])
        except Exception as e:
            raise serializers.ValidationError(e)
        obj.set_password(validated_data["password"])
        obj.save()
        return validated_data
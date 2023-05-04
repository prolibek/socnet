from rest_framework import serializers

class ProfileLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()

class ProfileRegisterSerializer(serializers.Serializer):
    pass

class PostListSerializer(serializers.Serializer):
    pass
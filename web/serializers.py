

from rest_framework import serializers

from user.serializers import UserSerializer
from web.models import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Questions
        fields = '__all__'

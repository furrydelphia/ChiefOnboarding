from rest_framework import serializers

from admin.sequences.models import Sequence
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    sequences = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate_sequences(self, value):
        if Sequence.objects.filter(pk__in=value).count() != len(value):
            raise serializers.ValidationError("Not all sequence ids are valid.")
        return value

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "start_day",
            "role",
            "email",
            "position",
            "phone",
            "buddy",
            "manager",
            "message",
            "linkedin",
            "facebook",
            "twitter",
            "timezone",
            "language",
            "sequences",
            "department"
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = ["id", "name"]

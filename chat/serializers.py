from rest_framework import serializers


class MatrixMessageSerializer(serializers.Serializer):
    room_id = serializers.CharField()
    content = serializers.CharField()


class MatrixCreateRoomSerializer(serializers.Serializer):
    room_alias = serializers.CharField(max_length=50, required=True)
    room_name = serializers.CharField(max_length=100, required=False)
    topic = serializers.CharField(max_length=255, required=False)

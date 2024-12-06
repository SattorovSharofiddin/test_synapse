import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MatrixMessageSerializer, MatrixCreateRoomSerializer

access_token = "syt_YWRtaW4_DLGPoeFCZWLHJdFtVgXQ_4Ilo2q"


class SendMessageView(APIView):
    def post(self, request):
        serializer = MatrixMessageSerializer(data=request.data)
        if serializer.is_valid():
            room_id = serializer.validated_data['room_id']
            content = serializer.validated_data['content']

            url = f"http://localhost:8448/_matrix/client/v3/rooms/{room_id}/send/m.room.message?access_token={access_token}"
            data = {
                "msgtype": "m.text",
                "body": content
            }
            response = requests.post(url, json=data)

            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            return Response(response.json(), status=response.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateRoomView(APIView):
    def post(self, request):
        serializer = MatrixCreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            room_alias = serializer.validated_data.get('room_alias')
            room_name = serializer.validated_data.get('room_name', None)  # Optional field
            topic = serializer.validated_data.get('topic', None)  # Optional field

            # Matrix API endpoint
            url = f"http://localhost:8448/_matrix/client/v3/createRoom?access_token={access_token}"

            # Data to send to Matrix server
            data = {
                "room_alias_name": room_alias
            }
            if room_name:
                data["name"] = room_name
            if topic:
                data["topic"] = topic

            # Send POST request to create a room
            response = requests.post(url, json=data)
            return Response(response.json(), status=response.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# {
#   "room_id": "!ZjfLyhuidSJjoArdTo:im.commeta.uz",
#   "content": "Hello, Matrix!"
# }


# {
#     "room_alias": "my-awesome-room",
#     "room_name": "My Awesome Room",
#     "topic": "Welcome to my awesome room!"
# }

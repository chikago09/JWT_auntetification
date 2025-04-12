from rest_framework.views import APIView
from rest_framework.response import Response



class ProductAPIView(APIView):
    def get(self, request):
        data = {"message": "Успешно отправлен!"}
        return Response(data)
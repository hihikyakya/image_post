from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from myapp.models import ImagePost
from .serializers import PostSerializer
from .parse_image import save_data_url_to_image
class UploadView(APIView):
    def get(self, request):
      blogs = ImagePost.objects.all()
      # 여러 개의 객체를 serialization하기 위해 many=True로 설정
      serializer = PostSerializer(blogs, many=True)
      return Response(serializer.data)
      
    def post(self, request, *args, **kwargs):
      serializer = PostSerializer(data = request.data)
      imageURL=request.data.imageURL
      title=request.data.title
      save_data_url_to_image(imageURL, title)
      if(serializer.is_valid()):
          serializer.save()
          return Response(serializer.data ,status=200)
      return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
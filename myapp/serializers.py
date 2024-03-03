from rest_framework import serializers
from .models import ImagePost
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = ImagePost
    fields = '__all__'
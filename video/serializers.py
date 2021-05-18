from rest_framework import  serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('link_video', 'title', 'created_at', 'updated_at')

from random import choices
from rest_framework import serializers
from shortlink.settings import CHARACTERS, SHORT_URL_SIZE
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(read_only=True)

    class Meta:
        model = Link
        fields = ('url', 'short_url',)

    def create(self, validated_data):

        while True:
            short_url = ''.join(choices(CHARACTERS, k=SHORT_URL_SIZE))

            if not Link.objects.filter(short_url=short_url):
                validated_data['short_url'] = short_url
                return super().create(validated_data)

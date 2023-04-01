from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import LinkSerializer
from .models import Link


class LinkApiView(APIView):

    def get(self, request, short_url):
        link = get_object_or_404(Link, short_url=short_url)
        link.save()
        return redirect(link.url)


class LinkCreateView(APIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def post(self, request):
        obj = Link.objects.filter(url=request.data['url'])
        if obj:
            return Response({'post': LinkSerializer(obj.values()[0]).data})
        serializer = LinkSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({'post': serializer.data})

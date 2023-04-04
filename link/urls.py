from django.urls import path
from .views import LinkApiView, LinkCreateView

urlpatterns = [
    path('', LinkCreateView.as_view(), name='create_link'),
    path('<str:short_url>/', LinkApiView.as_view())

]

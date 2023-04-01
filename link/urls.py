from django.urls import path
from .views import LinkApiView, LinkCreateView

urlpatterns = [
    path('', LinkCreateView.as_view()),
    path('<str:short_url>/', LinkApiView.as_view())

]

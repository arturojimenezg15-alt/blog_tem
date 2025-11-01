from django.urls import path
from .views import PublicationListView, PublicationCreteView

urlpatterns = [
    path('', PublicationListView.as_view(), name='Publications-list'),
    path('publication/new/', PublicationCreteView.as_view(), name='Publication-create'),
]

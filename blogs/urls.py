from django.urls import path
from .views import (
                    PublicationListView, 
                    PublicationCreteView,
                    PublicationDetailView,
                    PublicationUpdateView,
                    PublicationDeleteView
                  )                   

urlpatterns = [
    path('', PublicationListView.as_view(), name='Publications-list'),
    path('publication/new/', PublicationCreteView.as_view(), name='Publication-create'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='Publication-detail'),
    path('publication/<int:pk>/edit/', PublicationUpdateView.as_view(), name='Publication-update'),
    path('publication/<int:pk>/delete/', PublicationDeleteView.as_view(), name='Publication-delete'),
]

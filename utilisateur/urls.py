from django.urls import path

from utilisateur.views import *

urlpatterns = [
    path('profil/', ProfilAPIView.as_view()),
    path('articles/<slug:slug>/like/', ArticleLikeAPIView.as_view(), name='article-like'),

    path('profil/adresse/create', AdresseCreateAPIView.as_view()),  # CREATE adresse
    path('profil/adresse/', AdresseRUDAPIView.as_view()),  # GET PUT PATCH DELETE adresse

    path('profil/mensurations/', UserMensurationListCreateAPIView.as_view()),
    path('profil/mensurations/<int:pk>/', UserMensurationRUDApiView.as_view()),
    path('profil/mensurations/<int:ref_user_mensuration_id>/mesures/', UserMensurationMesureListApiView.as_view()),
    path('profil/mensurations/<int:ref_user_mensuration_id>/mesures/<int:pk>/', UserMensurationMesureUpdateApiView.as_view()),

    path('profil/demandes_devis/', UserDemandeDevisListCreateApiView.as_view()),
    path('profil/demandes_devis/<int:pk>/', UserDemandeDevisRUApiView.as_view()),

    # path('profil/devis/'),
    # path('profil/devis/<str:devis_numero>/details/'),
    # path('profil/devis/<str:devis_numero>/details/<int:pk>/'),
    # TODO - Devis
    # TODO - Rendez-vous
]

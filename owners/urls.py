from django.urls import path

from owners.views import OwnersView, DogsView, OwnersDogView

urlpatterns = [
    path('', OwnersView.as_view()),
    path('/dogs', DogsView.as_view()),
    path('/ownersdog', OwnersDogView.as_view())
]
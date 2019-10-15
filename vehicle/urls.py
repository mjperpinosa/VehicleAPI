from django.urls import path
from . import views

urlpatterns = [
    #Role URLs
    path("hotlists/", views.HotListView.as_view()),
    path("entries/", views.VehicleEntryView.as_view()),
    path("stats/", views.get_stats),
    path("hot-entries", views.VehicleEntryHotListView),
    path("vehicles/filter/<str:filter>", views.VehicleEntryFilter),
    path("vehicle/<str:plate_number>", views.VehicleDetail.as_view())

]

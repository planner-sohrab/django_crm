from django.urls import path
from .views import LeadDeleteView, LeadDetailView, LeadUpdateView, LeadListView, LeadCreateView, lead_create_view, lead_detail_view, lead_list_view, lead_update_view


app_name = "leads"
urlpatterns = [
    path("", LeadListView.as_view(), name="lead_list"),
    path("<int:pk>/", LeadDetailView.as_view(), name="lead_list_detail"),
    path("create/", LeadCreateView.as_view(), name="lead_create"),
    path("<int:pk>/update/", LeadUpdateView.as_view(), name="lead_update"),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name="lead_delete")
]
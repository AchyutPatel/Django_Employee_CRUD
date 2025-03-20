from django.urls import path
from .views import Create_or_Update_employee, All_employee, Delete_employee

urlpatterns = [
    path("", view=All_employee, name="All_employee"),
    path("create/", view=Create_or_Update_employee, name="Create_employee"),
    path("update/<int:e_id>/", view=Create_or_Update_employee, name="Update_employee"),
    path("delete/<int:e_id>/", view=Delete_employee, name="Delete_employee"),
]
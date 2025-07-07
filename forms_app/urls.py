from django.urls import path
from .views import submit_wheel_specification, get_wheel_specifications, submit_bogie_checksheet

urlpatterns = [
    path('api/forms/wheel-specifications', submit_wheel_specification),
    path('api/forms/wheel-specifications/', get_wheel_specifications),
    path('api/forms/bogie-checksheet', submit_bogie_checksheet),
]

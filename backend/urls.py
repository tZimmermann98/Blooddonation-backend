from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers


#URLConf
#router = routers.DefaultRouter()
#router.register(r'appointments',views.ApintmentsViewSet) #registers the rout to appointments



urlpatterns =[
    #path('', include(router.urls)),
    #path("free_appointments/", include("rest_framework.urls", namespace="rest_framework")),

    path('free_appointments/', views.free_appointmentsList.as_view()),
    path('reserved_appointments/', views.reserved_appointmentsList.as_view()),
    path('assigned_appointments/', views.assigned_appointmentsList.as_view()),
    path('kill_questions/', views.kill_questionsList.as_view()),
    #path('blood_donation_free_appointments/<int:pk>', views.blood_donation_free_appointmentsDetail.as_view()),
    path('', views.index, name = 'index')
]

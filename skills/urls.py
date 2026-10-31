from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_skill, name='add_skill'),
    path('my-skills/', views.my_skills, name='my_skills'),
    path('browse/', views.browse_skills, name='browse_skills'),
    path('send-request/<int:skill_id>/', views.send_request, name='send_request'),
    path('incoming-requests/',views.incoming_requests, name='incoming_requests'),
    path('respond-request/<int:request_id>/',views.respond_request,name='respond_request'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home1,name='home1'),
    path('about/',views.about,name='about'),
    path('<int:chai_id>/',views.contact,name='contact'),
    path('chaidetails/',views.chai_details,name='chai_details'),
    path('chai_review/',views.chai_review,name='chai_review')
]


from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('learn', views.learn,name="learn"),
    path('indo/<int:in_id>', views.indo,name="indo"),
    path('indo1/<int:in_id>', views.indo1,name="indo1"),
    path('qa/<int:q_id>', views.qa,name="qa"),
    path('qa1/<int:q_id>', views.qa1,name="qa1"),
    path('search', views.search,name="search"),
]
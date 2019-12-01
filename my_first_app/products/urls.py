from djangourls import path #to user path function
from . import views #import views modules form current folder
 
#Some possible urls
#products
#products/1/detail
#products/new
 
 
urlpatterns = [
    path('', views.index), #note: do not call this function, just pass a reference
    path('', views.index),
    path('', views.index),
]

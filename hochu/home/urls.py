from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView, name='all'),
    path('suc', views.SucView, name='suc'),
    path('calc', views.CalcView, name='calc'),
    path('cert', views.CertView, name='cert'),
    path('cont', views.ContView, name='cont'),
    path('forg', views.ForgView, name='forg'),
    path('metalprof', views.MetalprofView, name='metalprof'),
    path('metaltile', views.MetaltileView, name='metaltile'),
    path('monolith', views.MonolithView, name='monolith'),
    path('polycarb', views.PolycarbView, name='polycarb'),
    path('privpol', views.PrivpolView, name='privpol'),
    path('profpipe', views.ProfpipeView, name='profpipe'),
    path('softroof', views.SoftroofView, name='softroof'),
    path('wood', views.WoodView, name='wood'),  
]
#'upload_form'
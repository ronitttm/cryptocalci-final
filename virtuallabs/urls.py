from django.contrib import admin
from django.urls import path,include
from virtuallabs import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home,name="home"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path('signout', views.signout, name='signout'),
    path("virtuallabs", views.exp_list, name="exp_list"),
    path("experiment1", views.exp1, name="exp1"),
    path("experiment2", views.exp2, name="exp2"),
    path("experiment3", views.exp3, name="exp3"),
    path("experiment4", views.exp4, name="exp4"),
    path("experiment5", views.exp5, name="exp5"),
    path("experiment6", views.exp6, name="exp6"),
    path("experiment7", views.exp7, name="exp7"),
    path("experiment8", views.exp8, name="exp8"),
    path("experiment9", views.exp9, name="exp9"),
    path("experiment10", views.exp10, name="exp10"), 
    path('generate_pdf1', views.display_image_and_code1, name='generate1'),
    path('generate_pdf2', views.display_image_and_code2, name='generate2'),
    path('generate_pdf3', views.display_image_and_code3, name='generate3'),
    path('generate_pdf4', views.display_image_and_code4, name='generate4'),
    #path('generate_pdf5', views.display_image_and_code4, name='generate5')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

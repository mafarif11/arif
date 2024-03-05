from django.urls import path
from.import views

urlpatterns=[
    path('j',views.home,name='home'),
    path('homee',views.home,name='homee'),
    path('add',views.add,name='add'),
    path('f',views.dash,name="dash"),
    path('up/<int:id>',views.up,name='up'),
    path('de/<int:id>',views.de,name='de'),
    path('first1',views.first,name='first1'),
    path('last1',views.last,name='last1'),
    path('all1',views.all,name='all1'),
    path('back',views.bac,name='bac'),
    path('backk',views.back,name='back'),
    path('logg',views.logg,name='logg'),
    path('regg',views.regg,name='regg'),
    path('',views.emoj,name='emoj'),
    #path('semo',views.semo,name='semo'),
    path('vieww',views.place_text_on_image,name='vieww'),
]



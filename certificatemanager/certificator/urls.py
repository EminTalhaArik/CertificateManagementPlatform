from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'E-Katılımcı'               
admin.site.index_title = 'E-Katılımcı'                 
admin.site.site_title = 'E-Katılımcı' 

urlpatterns = [
    path('', view=views.main, name='index'),
    path('katilim-belgesi/<int:code>', view=views.generate_certificate, name='katilim-belgesi')
]

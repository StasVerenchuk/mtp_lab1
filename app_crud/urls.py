from django.urls import path
from .views import CrudHomeView
from . import views

urlpatterns = [
    path('', CrudHomeView.as_view(), name='crud_home'),
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name='update_url'),
    path('del/<int:f_oid>', views.deleteView, name='delete_url'),
]

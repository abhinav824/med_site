from django.urls import path,include
from django.conf import settings

from . import views

app_name='med'

urlpatterns=[
             path('',views.home,name='home'),
             path('login/',views.login_page,name='login'),
             path('logout/',views.logout_view,name='logout'),
             path('medicine/<int:id>',views.medicine_details,name='medicine'),
             path('medicine/<int:id>/order',views.order,name='order'),
             path('medicine/<int:med_id>/place_order/<int:s_id>',views.place_order,name='place_order'),
             path('recent_orders_p/',views.recent_orders_p,name='recent_orders_p'),
             path('recent_orders_r/',views.recent_orders_r,name='recent_orders_r'),

]

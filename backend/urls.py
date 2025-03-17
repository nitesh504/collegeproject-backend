from django.contrib import admin
from django.urls import path
from core.views import signup, user_login
from django.http import HttpResponseRedirect  
import core.views 
from core.views import OrderListCreateView 

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/signup/')),  
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('get-recommendation/', core.views.get_personal_recommendation, name='get_recommendation'),
    path('create-booking/', core.views.create_booking, name='create_booking'),
    path('get-bookings/', core.views.get_bookings, name='get_bookings'),
    path('api/create-venue-booking/', core.views.create_venue_booking, name='create_venue_booking'),
    path('api/get-venue-bookings/', core.views.get_venue_bookings, name='get_venue_bookings'),
    path('banquets/', core.views.BanquetListView.as_view(), name='banquet-list'),  
    path('banquets/<int:pk>/', core.views.BanquetDetailView.as_view(), name='banquet-detail'),  
   path('api/order/', OrderListCreateView.as_view(), name='create-order'),
   path('pundits/', core.views.PunditListView.as_view(), name='pundit-list'),
    path('pundits/<int:pk>/', core.views.PunditDetailView.as_view(), name='pundit-detail'),
    path('api/enquiry/', core.views.submit_enquiry, name='submit_enquiry'),
    path('api/enquiries/', core.views.get_enquiries, name='get_enquiries'),
]

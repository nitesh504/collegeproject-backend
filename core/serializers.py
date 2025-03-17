from rest_framework import serializers
from .models import PunditBooking, Banquet, Order, Pundit, PersonalRecommendation, VenueBooking, Enquiry

class PunditBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PunditBooking
        fields = ['id', 'name', 'phone', 'email', 'event_type', 'samagri', 'date', 'address', 'detail']
class BanquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banquet
        fields = ['id', 'name', 'location', 'starting_price',  'description']
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [ 'product', 'name', 'email', 'phone', 'additional_instructions']
class PunditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pundit
        fields = ['id', 'name', 'education', 'price']
class PersonalRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalRecommendation
        fields = ['horoscope', 'education', 'finance', 'travel', 'education_image', 'finance_image', 'travel_image']
class VenueBookingSerializer(serializers.ModelSerializer):
    banquet = serializers.CharField(source='banquet.name', read_only=True)  

    class Meta:
        model = VenueBooking
        fields = [
            'id', 'banquet', 'phone', 'email', 
            'start_date', 'end_date', 'number_of_guests',
            'event_type', 'additional_request'
        ]
class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'message']
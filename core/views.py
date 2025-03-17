from rest_framework import status
import jwt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta
from .models import PersonalRecommendation, PunditBooking, VenueBooking, Banquet,Pundit, Enquiry, Order
from .serializers import PunditBookingSerializer, BanquetSerializer, OrderSerializer,PunditSerializer,PersonalRecommendationSerializer,VenueBookingSerializer,EnquirySerializer
from rest_framework.views import APIView
from rest_framework.response import Response




JWT_SECRET = "your_secret_key" 
JWT_ALGORITHM = "HS256"


def generate_jwt_token(user):
    payload = {
        "id": user.id,
        "username": user.username,
        "is_admin": user.is_superuser,
        "exp": datetime.utcnow() + timedelta(hours=1)  
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)
            
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({"message": "User created successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

# Login View
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            
           
            if username == "niteshdulal31@gmail.com" and password == "Nepal@123":
                token = jwt.encode(
                    {"username": username, "is_admin": True, "exp": datetime.utcnow() + timedelta(hours=1)},
                    JWT_SECRET,
                    algorithm=JWT_ALGORITHM,
                )
                return JsonResponse({"message": "Admin login successful", "redirect_url": "/admin/", "is_admin": True, "token": token})
            
           
            user = authenticate(username=username, password=password)
            if user:
       
                login(request, user)
                
           
                token = generate_jwt_token(user)
                
            
                if user.is_superuser:
                    return JsonResponse({"message": "Admin login successful", "redirect_url": "/admin/", "is_admin": True, "token": token})
                
            
                return JsonResponse({"message": "Login successful", "redirect_url": "/user-home/", "is_admin": False, "token": token})
            
            return JsonResponse({"error": "Invalid credentials"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_personal_recommendation(request):
    if request.method == "POST":
        try:
     
            data = json.loads(request.body)
            name = data.get('name')
            horoscope = data.get('horoscope')
            birthday = data.get('birthday')

        
            try:
                recommendation = PersonalRecommendation.objects.get(horoscope=horoscope)
                
         
                birth_date = datetime.strptime(birthday, "%Y-%m-%d")
                birth_month = birth_date.month
                
                
                financial_decision = f"Financial advice for {horoscope}: Invest in long-term assets."
                if birth_month in [6, 7, 8]:
                    travel_decision = f"Travel advice for {horoscope}: Ideal time for a summer vacation."
                else:
                    travel_decision = f"Travel advice for {horoscope}: Stay cautious with travel during this period."
                
                health_decision = f"Health advice for {horoscope}: Focus on a balanced diet and regular exercise."
                
               
                response = {
                    "name": name,
                    "horoscope": recommendation.horoscope,
                    "education": recommendation.education,
                    "education_image": recommendation.education_image.url if recommendation.education_image else None,
                    "finance": recommendation.finance,
                    "finance_image": recommendation.finance_image.url if recommendation.finance_image else None,
                    "travel": recommendation.travel,
                    "travel_image": recommendation.travel_image.url if recommendation.travel_image else None,
                    "financial_decision": financial_decision,
                    "travel_decision": travel_decision,
                    "health_decision": health_decision,
                }

                return JsonResponse(response, status=200)
            except PersonalRecommendation.DoesNotExist:
                return JsonResponse({"error": "No recommendation found for the given horoscope."}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method."}, status=400)

@csrf_exempt
def create_booking(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            name = data.get("name")
            phone = data.get("phone")
            email = data.get("email")
            event_type = data.get("event_type")
            samagri = data.get("samagri")
            date = data.get("date")
            address = data.get("address")
            detail = data.get("detail", "")
            
       
            booking = PunditBooking.objects.create(
                name=name,
                phone=phone,
                email=email,
                event_type=event_type,
                samagri=samagri,
                date=date,
                address=address,
                detail=detail
            )
            
    
            return JsonResponse({"message": "Booking created successfully", "booking": PunditBookingSerializer(booking).data}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def get_bookings(request):
    if request.method == "GET":
        try:
            bookings = PunditBooking.objects.all()
          
            return JsonResponse({"bookings": PunditBookingSerializer(bookings, many=True).data}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def create_venue_booking(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            banquet_id = data.get("banquet")
            phone = data.get("phone")
            email = data.get("email")
            start_date = data.get("start_date")
            end_date = data.get("end_date")
            number_of_guests = data.get("number_of_guests")
            event_type = data.get("event_type")
            additional_request = data.get("additional_request")
            try:
                banquet = Banquet.objects.get(id=banquet_id)
            except Banquet.DoesNotExist:
                return JsonResponse({"error": "Banquet not found"}, status=404)
            
            booking = VenueBooking(
                banquet=banquet,
                phone=phone,
                email=email,
                start_date=start_date,
                end_date=end_date,
                number_of_guests=number_of_guests,
                event_type=event_type,
                additional_request=additional_request
            )
            booking.save()
            return JsonResponse({
                'message': 'Venue Booking created successfully',
                'booking': {
                    'id': booking.id,
                    'banquet': booking.banquet.name,
                    'phone': booking.phone,
                    'email': booking.email,
                    'start_date': booking.start_date,
                    'end_date': booking.end_date,
                    'number_of_guests': booking.number_of_guests,
                    'event_type': booking.event_type,
                    'additional_request': booking.additional_request
                }
            }, status=201)

        except Exception as e:
            return JsonResponse({
                'message': f'Error creating booking: {str(e)}'
            }, status=400)

    else:
        return JsonResponse({
            'message': 'Invalid request method'
        }, status=405)
    

@csrf_exempt
def get_venue_bookings(request):
    try:
        
        bookings = VenueBooking.objects.all()

        
        serializer = VenueBookingSerializer(bookings, many=True)

       
        return JsonResponse({'bookings': serializer.data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class BanquetListView(APIView):
    def get(self, request):
        """
        Fetch and return the list of all banquets
        """
        banquets = Banquet.objects.all()
        serializer = BanquetSerializer(banquets, many=True)
        return Response(serializer.data)

class BanquetDetailView(APIView):
    def get(self, request, pk):
        """
        Fetch a single banquet by its ID
        """
        try:
            banquet = Banquet.objects.get(pk=pk)
            serializer = BanquetSerializer(banquet)
            return Response(serializer.data)
        except Banquet.DoesNotExist:
            return Response({"error": "Banquet not found"}, status=404)
class PunditListView(APIView):
    def get(self, request):
        """
        Fetch and return the list of all pundits
        """
        pundits = Pundit.objects.all()
        serializer = PunditSerializer(pundits, many=True)
        return Response(serializer.data)

class PunditDetailView(APIView):
    def get(self, request, pk):
        """
        Fetch a single pundit by its ID
        """
        try:
            pundit = Pundit.objects.get(pk=pk)
            serializer = PunditSerializer(pundit)
            return Response(serializer.data)
        except Pundit.DoesNotExist:
            return Response({"error": "Pundit not found"}, status=404)

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Order created successfully."}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def submit_enquiry(request):
    if request.method == 'POST':
        try:
         
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        serializer = EnquirySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Enquiry submitted successfully'}, status=201)
        return JsonResponse({'error': 'Invalid data', 'details': serializer.errors}, status=400)

def get_enquiries(request):
    enquiries = Enquiry.objects.all()  
    serializer = EnquirySerializer(enquiries, many=True) 
    return JsonResponse({'enquiries': serializer.data}) 
class OrderListCreateView(APIView):
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
   
    def get(self, request):
        orders = Order.objects.all()  
        serializer = OrderSerializer(orders, many=True)  
        return Response(serializer.data) 

   
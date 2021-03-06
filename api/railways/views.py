from django.http import JsonResponse

from rest_framework import generics, permissions
from rest_framework import views
from rest_framework.exceptions import NotFound

from api.railways.serializers import (
    RouteItemSerializer,
    RouteSerializer,
    SpecificRideSerializer,
    StationSerializer,
    TicketBuySerializer,
    TicketSerializer,
    UserTicketsSerializer,
)

from railways.models import (
    Ride,
    Route,
    RouteItem,
    Station,
    Ticket,
)


class StationListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class RouteListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteItemListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)

    queryset = RouteItem.objects.all()
    serializer_class = RouteItemSerializer


class SpecificRidesAPI(generics.ListAPIView):
    serializer_class = SpecificRideSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        try:
            departure_station = Station.objects.get(
                title=self.request.query_params.get('departure_station', None)
            )
        except Station.DoesNotExist:
            raise NotFound({
                'departure_station': 'This station does not exist'
            })

        try:
            arrival_station = Station.objects.get(
                title=self.request.query_params.get('arrival_station', None)
            )
        except Station.DoesNotExist:
            raise NotFound({
                'arrival_station': 'This station does not exist'
            })

        departure_date = self.request.query_params.get('departure_date', None)

        return Ride.objects.filter(
            departure_date=departure_date,
            route__departure_station=departure_station,
            route__arrival_station=arrival_station
        )

    def list(self, request, *args, **kwargs):
        serializer = SpecificRideSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        return super().list(request, *args, **kwargs)


class TicketListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.dict()

        data['user_email'] = request.user.email

        serializer = TicketBuySerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(
            {
                'Purchase status': ['Success', ]
            },
            status=201
        )


class UserTickets(generics.ListAPIView):
    serializer_class = UserTicketsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Ticket.objects.filter(customer=self.request.user)


class BuyTicket(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        data = request.data.dict()

        data['user_email'] = request.user.email

        serializer = TicketBuySerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(
            {
                'Purchase status': ['Success', ]
            },
            status=201
        )


class TicketDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

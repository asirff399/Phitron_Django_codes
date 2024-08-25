from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Pet,PetType,Adoption
from .serializers import PetSerializer,PetTypeSerializer
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from rest_framework import filters, pagination


# class PetPagination(pagination.PageNumberPagination):
#     page_size = 6 # items per page
#     page_size_query_param = page_size
#     max_page_size = 100

class PetViewset(viewsets.ModelViewSet):   
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['pet_type__name','adoption_status']
    # pagination_class = PetPagination


class PetTypeViewset(viewsets.ModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer

@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet,id=pet_id)
    customer = request.user.customer
    if pet.adoption_status == 'Available' and customer.balance >= pet.price:
        customer.balance -= pet.price
        customer.save()

        Adoption.objects.create(pet=pet,customer=request.user)

        pet.adoption_status = 'Adopted'
        pet.save()

        return redirect('',pet_id=pet_id)
    else:
        return redirect('',pet_id=pet_id)

class PetList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def get(self,request,format=None):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = PetSerializer(data = request.data)
        serializer.author=request.user
        print(request.user)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetails(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_object(self,pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        pet = self.get_object(pk)

        if request.user != pet.author and not request.user.is_staff:
            return Response({"detail": "You do not have permission to edit this pet."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PetSerializer(pet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        pet = self.get_object(pk)

        if request.user != pet.author and not request.user.is_staff:
            return Response({"detail": "You do not have permission to delete this pet."}, status=status.HTTP_403_FORBIDDEN)
        
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Portfolioapp import models
from Portfolioapp.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')

        print(name,email,content)
        
        if not content:
            messages.error(request, 'Message cannot be empty')
            return render(request, 'contact.html')
            
        # name validation
        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of name should be greater than 2 and less than 30 words')
            return render(request,'contact.html')
        
        # email validation
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'invalid email try again')
            return render(request,'contact.html')
        
        # number validation
        # if len(number)>2 and len(number)<13:
        #     pass
        # else:
        #     messages.error(request,'invalid number try again')
        #     return render(request,'contact.html')

        ins=models.Contact(name=name,email=email,content=content)
        ins.save()
        messages.success(request,'Thank you for contacting me || Your Message have been Saved')
        print('data has been saved to database')
        print('the request is no pass')
    
    return render(request, 'contact.html')





# Api:API 1: CREATE Contact (POST)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer

@api_view(['POST'])
def create_contact_api(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Contact message saved successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Api:API 2: RETRIEVE Contacts (GET – Admin Only)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_contacts_api(request):
    contacts = Contact.objects.all().order_by('-created_at')
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)



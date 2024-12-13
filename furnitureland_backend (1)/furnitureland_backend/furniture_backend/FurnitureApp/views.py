from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.shortcuts import get_object_or_404

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from FurnitureApp.models import User, Furniture
from FurnitureApp.serializers import UserSerializer, FurnitureSerializer

# endpoint for furniture adding and retrieving
@csrf_exempt
def furnitureApi(request, id=00):

    # get all furnitures
    if request.method == 'GET':
        if id == 00:
            # Retrieve all furniture items
            items = Furniture.objects.all()
            items_serializer = FurnitureSerializer(items, many=True)
            return JsonResponse(items_serializer.data, safe=False)
        else:
            # Retrieve a specific furniture item by ID
            item = get_object_or_404(Furniture, pk=id)
            item_serializer = FurnitureSerializer(item)
            return JsonResponse(item_serializer.data, safe=False)
    
    # add new furniture item
    elif request.method == 'POST':
        furniture_data = JSONParser().parse(request)
        furniture_serializer = FurnitureSerializer(data=furniture_data)
        if furniture_serializer.is_valid():
            furniture_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    # update furniture item
    elif request.method in ['PUT', 'PATCH']:
        item = get_object_or_404(Furniture, pk=id)
        furniture_data = JSONParser().parse(request)
        furniture_serializer = FurnitureSerializer(item, data=furniture_data, partial=True)
        if furniture_serializer.is_valid():
            furniture_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    
    # delete furniture item
    elif request.method == 'DELETE':
        item = get_object_or_404(Furniture, pk=id)
        item.delete()
        return JsonResponse("Deleted Successfully", safe=False)

    return JsonResponse("Invalid Method", safe=False)
    
#end point for user registration   
@csrf_exempt
def userRegApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)

        # Hash the password before saving to the database
        hashed_password = make_password(user_data['Password'])
        user_data['Password'] = hashed_password

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Registered Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

#endpoint for user login
@csrf_exempt
def userLoginApi(request):
    if request.method == 'POST':
        login_data = JSONParser().parse(request)
        email = login_data.get('email', '')
        password = login_data.get('password', '')

        try:
            user = User.objects.get(Email=email)

            # Check if the provided password matches the stored hashed password
            if check_password(password, user.Password):
                user_serializer = UserSerializer(user)
                serialized_user = user_serializer.data
                return JsonResponse({"status": "Login Successful", "user": serialized_user}, safe=False)
            else:
                return JsonResponse({"status": "Login Failed. Incorrect password"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

    return JsonResponse({"error": "Invalid Request Method"}, status=400)
    
# Endpoint to get all users
@csrf_exempt
def getAllUsersApi(request):
    print("Hello")
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    return JsonResponse({"error": "Invalid Request Method"}, status=400)

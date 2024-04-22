from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import Memberserializer
from members.models import Task


@api_view(['GET'])
def getroutes(request):
    
    routes = [
        {'GET': '/api/members/'},        # Retrieve all members
        {'GET': '/api/members/<id>'},    # Retrieve a specific member
        {'POST': '/api/members/'},       # Create a new member
        {'PUT': '/api/members/<id>'},    # Update a specific member (replace entire resource)
        {'PATCH': '/api/members/<id>'},  # Update a specific member (partially)
        {'DELETE': '/api/members/<id>'},    
    ]
    #return JsonResponse(routes, safe=False)
    return Response(routes)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getmembers(request):
    memb = Task.objects.all()
    serializer = Memberserializer(memb, many=True)
    return Response(serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getmember(request,pk):
    memb = Task.objects.get(id=pk)
    serializer = Memberserializer(memb,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postmember(request):
    if request.method == 'POST':
        serializer = Memberserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def updatemember(request, pk):
    try:
        member = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = Memberserializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletemember(request, pk):
    try:
        member = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Member not found"}, status=404)

    member.delete()
    return Response({"success": "Member deleted successfully"}, status=204)



@api_view(['GET'])
def search_members(request):
    search_query = request.GET.get('title', None)   #None if no find
    if search_query:
        members = Task.objects.filter(title__icontains=search_query)
        serialized_members = Memberserializer(members, many=True)
        return Response(serialized_members.data)
    else:
        return Response({'error': 'No search query provided'}, status=400)
    


# def searchmem(request):

#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')  #Qlookup

#     tags = Tag.objects.filter(name__icontains=search_query)

#     member = members.objects.distinct().filter(
#         Q(title__icontains=search_query) |
#         Q(description__icontains=search_query) |
#     )
#     return member, search_query

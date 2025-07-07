from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import WheelSpecification, BogieChecksheet
from .serializers import WheelSpecificationSerializer, BogieChecksheetSerializer

@api_view(['POST'])
def submit_wheel_specification(request):
    serializer = WheelSpecificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "submittedBy": serializer.data['submittedBy'],
                "submittedDate": serializer.data['submittedDate'],
                "status": "Saved"
            }
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_wheel_specifications(request):
    filters = {}
    if request.GET.get('formNumber'):
        filters['formNumber'] = request.GET['formNumber']
    if request.GET.get('submittedBy'):
        filters['submittedBy'] = request.GET['submittedBy']
    if request.GET.get('submittedDate'):
        filters['submittedDate'] = request.GET['submittedDate']

    queryset = WheelSpecification.objects.filter(**filters)
    serializer = WheelSpecificationSerializer(queryset, many=True)
    return Response({
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": serializer.data
    })

@api_view(['POST'])
def submit_bogie_checksheet(request):
    serializer = BogieChecksheetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "inspectionBy": serializer.data['inspectionBy'],
                "inspectionDate": serializer.data['inspectionDate'],
                "status": "Saved"
            }
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

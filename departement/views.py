from django.shortcuts import render


# Create your views here.

@api_view(['GET', 'POST'])
def rest_store(request):
    if request.method == 'GET':
        queryset = DepartementModel.objects.all()
        serializer = DepartementSerializer(queryset, many=True)
        
    elif request.method == 'POST':
        pass
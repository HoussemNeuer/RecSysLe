from rest_framework.response import Response 

from rest_framework.decorators import api_view 

import RecTulips as RS


@api_view(['GET'])
def getData(request):

    person = {'3ouuziav5tUsanSvGBiGrShtk263' : RS.TOP10("3ouuziav5tUsanSvGBiGrShtk263")}
    
    RS.Rate(1,2,3,'12-03-2000')

    return Response(person)



@api_view(['POST'])
def addItem(request):

    RS.Rate(request.data['user_id'],request.data['item_id'],request.data['rating'],request.data['date'])
    print(request.data['user_id'])


    return Response()


@api_view()
def Suggest(request):

    print()
    
    return Response({'Suggestions' : RS.TOP10(request.query_params['uid']) })
from collections import Counter

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def lambda_function(request):
    question = request.data.get('question')
    solution = []
    c = Counter(question)
    for item, count in c.most_common():
        for _ in range(count):
            solution.append(item)
    return Response({
        'solution': solution
    }, status=status.HTTP_200_OK)

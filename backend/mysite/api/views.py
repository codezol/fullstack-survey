from .models import Question, Answer
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
# For admin users to view and create survey questions
class QuestionsListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

# For admin users to retrieve and delete a survey question
class QuestionRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

# For admin users to view all of the answers
class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminUser]

# For all users to retrieve a question
class QuestionRetrieve(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
# For all users to retrieve all questions
class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

# For all users to be able to send an answer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class AnswerCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AnswerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# allow admin users to delete all answers
class DeleteAllAnswersView(APIView):
    permission_classes = [IsAdminUser] 

    def delete(self, request):
        Answer.objects.all().delete()
        return Response({"message": "All answers have been deleted."}, status=status.HTTP_204_NO_CONTENT)

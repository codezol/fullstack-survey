from django.urls import path
from . import views

urlpatterns = [
    path('questions/listcreate', views.QuestionsListCreate.as_view(), name='questions-list-create'),
    path('questions/', views.QuestionsList.as_view(), name='questions-list'),
    path('questions/<int:pk>/', views.QuestionRetrieve.as_view(), name='question-retrieve'),
    path('questions/destroy/<int:pk>/', views.QuestionRetrieveDestroy.as_view(), name='question-retrieve-destroy'),
    path('answers/', views.AnswerListCreate.as_view(), name='answers-list-create'),
    path('answers/create/', views.AnswerCreate.as_view(), name='answer-create'),
    path('answers/delete-all', views.DeleteAllAnswersView.as_view(), name='delete-all-answers')
]

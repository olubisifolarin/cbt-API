from django.urls import path
from cbtapp import views
from django.conf import settings

app_name = 'cbtapp'

urlpatterns = [
    path('', views.QuizzesView.as_view(), name='quizzes'),
    path('answer/', views.AnswerView.as_view(), name='answer')

]
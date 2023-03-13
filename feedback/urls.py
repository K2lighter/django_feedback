from django.urls import path
from .views import index, done, update_feedback, FeedbackView, UpdateFeedbackView, DoneView, ListFeedbackView

urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedbackView.as_view()),
    path('<int:id_feedback>', UpdateFeedbackView.as_view()),
    path('list_feedback', ListFeedbackView)
]

from django.urls import path
from rest_framework.routers import SimpleRouter

from back.views import QuestionsView, user_visit

router = SimpleRouter()
router.register('questions', QuestionsView)

urlpatterns = [
    path(r'visit/', user_visit)
]

urlpatterns += router.urls

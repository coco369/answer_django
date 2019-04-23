
from rest_framework.routers import SimpleRouter

from back.views import QuestionsView

router = SimpleRouter()
router.register('questions', QuestionsView)

urlpatterns = [

]

urlpatterns += router.urls


from rest_framework.routers import SimpleRouter

from user.views import UserView

router = SimpleRouter()
router.register('user', UserView)

urlpatterns = [

]

urlpatterns += router.urls

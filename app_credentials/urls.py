from django.urls import path

from smp_commons.views import get_open_api_view
from smp_commons.routers import SmpRouter

from . import views


router = SmpRouter()
router.register('', views.CredentialViewSet, base_name='credential')

urlpatterns = router.urls

urlpatterns.append(path('swagger.json', get_open_api_view(urlpatterns)))

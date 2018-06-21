from smp_base_django.urls import urlpatterns
from smp_base_django.routers import SmpRouter

from . import views


router = SmpRouter()
router.register('credentials', views.CredentialViewSet, base_name='credential')

urlpatterns += router.urls

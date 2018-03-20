from smp_commons.routers import SmpRouter

from . import views


router = SmpRouter()
router.register('', views.CredentialViewSet, base_name='credential')

urlpatterns = router.urls

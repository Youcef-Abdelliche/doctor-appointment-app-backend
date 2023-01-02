from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register("doctors", views.DoctorViewSet, basename="doctors")

urlpatterns = router.urls

from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from api import views
router=DefaultRouter()
from rest_framework.authtoken.views import ObtainAuthToken
router.register("register",views.Createuserviw,basename="registration"),
router.register("cakes",views.Cakelistview,basename="cakes"),
router.register("carts",views.Cartlistview,basename="cartlist"),
router.register("reviews",views.Reviewlistview,basename="Reviewlist"),

urlpatterns = [
        path("token/",ObtainAuthToken.as_view()),

]+router.urls



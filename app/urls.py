from django.urls import path
from app.views import *


urlpatterns = [
    path('', login_view, name="login"),
    path('storefront/', storefront_page, name = "storefront"),
    path('register/', register_view, name = "register"),
    path('logout/', logout_view, name="logout")
    path('item_detail/', item_view, name="details")

]

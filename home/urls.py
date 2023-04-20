from django.urls import path 
# from . import views 
from . views import *



urlpatterns = [
    #path('', views.function in view.py file, #name= template),
    path('', index, name= 'index'),
    path('category/', category, name='category'),
    path('product/', product, name='product'),
    path('categories/<str:id>/', categories, name='categories'),
    # path('categories/<slug:slug>/', categories, name=categories)
    path('details/<str:id>/', details, name='details'),
    path("contact/", contact, name="contact"),
    path("signin/", signin, name="signin" ),
    path("signout/", signout, name="signout"),
    path("signup/", signup, name="signup"),
    path("profile/", profile, name="profile"),
    path("profile_update/", profile_update, name="profile_update"),
    path("password/", password, name="password"),
    path("shopcart/", shopcart, name="shopcart"),
    path("displaycart/", displaycart, name="displaycart"),
    path("deleteitems/", deleteitems, name="deleteitems"),
    path("change/", change, name="change"),
    path("checkout/", checkout, name="checkout"),
    path("pay/", pay, name="pay"),
    path("callback/", callback, name="callback"),
    path("search/", search, name="search")

]






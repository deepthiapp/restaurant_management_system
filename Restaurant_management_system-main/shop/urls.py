from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.handleSignUp, name='handleSignUp'),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('about/', views.about, name="AboutUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('checkout/', views.checkout, name="Checkout"),
    path('productView/<int:myid>', views.productView, name="productView"),
    path('orderView/', views.orderView, name="orderView"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('pay/', views.pay, name="pay"),
    path('make_payment/<int:amount>/', views.homepage, name='payment'),
    path('make_payment/<int:amount>/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('cancel_order/', views.cancel_order, name='cancel_order'),  # Add this line for cancel_order view

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="shop/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="shop/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="shop/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="shop/password_reset_done.html"),
         name="password_reset_complete"),
]

from django.urls import path, include,re_path
from . import views
# from . import f_views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf.urls import url
from logisticsapp.views import *
from .views import *


app_name = 'logisticsapp'

urlpatterns = [
#!------------------    ACCOUNT TABLE    ------------------#!

    path('register', RegistrationApiVew.as_view()),
    path('login', LoginView.as_view()),
    path('forgot-password-send-otp', ForgotPasswordSendOtp.as_view()),
    path('otp-verify-forgot-pass', OtpVerificationForgotpass.as_view()),
    path('password-reset', ForgotPasswordReset.as_view()),
    path('change-password', ChangePassword.as_view()),

    path('signup-phone-number', SignUpPhoneNumberApiView.as_view()),

    path('login-view', LoginApiView.as_view()),

    path('verify-otp', VerifyOtpPhoneNumberApiView.as_view()),

    path('signup-user', SignupUserApiView.as_view()),

    path('signup-driver-owner', SignUpforDriverOrOwner.as_view()),

#!------------------    MASTER TABLE    ------------------#!

    path('user-role-ref', UserRoleRefView.as_view()),
    path('user-role-ref/<int:pk>', UserRoleRefView.as_view()),

    path('vehicle-types', VehicleTypesView.as_view()),
    path('vehicle-types/<int:pk>', VehicleTypesView.as_view()),

    path('city', CityView.as_view()),
    path('city/<int:pk>', CityView.as_view()),

    path('coupons', CouponsView.as_view()),
    path('coupons/<int:pk>', CouponsView.as_view()),

    path('status', StatusView.as_view()),
    path('status/<int:pk>', StatusView.as_view()),

    path('subcription-plan', SubscriptionView.as_view()),
    path('subcription-plan/<int:pk>', SubscriptionView.as_view()),

#!------------------------------------------------------------------------------------------


    path('custom-user', CustomUserView.as_view()),  #!   pending
    path('custom-user/<int:pk>', CustomUserView.as_view()),

    # path('owner', OwnerView.as_view()),
    # path('owner/<int:pk>', OwnerView.as_view()),

    path('driver', DriverView.as_view()),   #!   pending
    path('driver/<int:pk>', DriverView.as_view()),

    path('review', ReviewApiView.as_view()),
    path('review/<int:pk>', ReviewApiView.as_view()),

    path('vehicle', VehicleView.as_view()),
    path('vehicle/<int:pk>', VehicleView.as_view()),

    path('customer-address', CustomerAddressView.as_view()),
    path('customer-address/<int:pk>', CustomerAddressView.as_view()),


    path('pickup-details', PickupDetailsView.as_view()),
    path('pickup-details/<int:pk>', PickupDetailsView.as_view()),

    path('drop-details', DropDetailsView.as_view()),
    path('drop-details/<int:pk>', DropDetailsView.as_view()),

    path('placed-order', PlacedOrderView.as_view()),
    path('placed-order/<int:pk>', PlacedOrderView.as_view()),



    path('in-order', InOrderView.as_view()),
    path('in-order/<int:pk>', InOrderView.as_view()),


    path('payment-detail', PaymentDetailView.as_view()),
    path('payment-detail/<int:pk>', PaymentDetailView.as_view()),

    path('account-detail', AccountView.as_view()),
    path('account-detail/<int:pk>', AccountView.as_view()),

    path('latitude_longitude', DriverLatitudeLongitudeView.as_view()),

    path('user_destination', UserDestinationsView.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

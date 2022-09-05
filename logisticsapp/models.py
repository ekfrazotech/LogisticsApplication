import base64
from ctypes import addressof
from operator import mod
from turtle import up
from django.db import models
from django.contrib.auth.models import User
# from django.db.models.base import Model

#!------------------    MASTER TABLE    ------------------#!


class UserRoleRef(models.Model):
    user_role_name = models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp")
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp")

class City(models.Model):
    city_name= models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp")
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp")

class VehicleTypes(models.Model):
    vehicle_type_name= models.CharField(max_length=250, blank=True, null=True)
    capacity= models.CharField(max_length=250, blank=True, null=True)
    size = models.CharField(max_length=250, blank=True, null=True)
    details= models.CharField(max_length=250, blank=True, null=True)
    per_km_price= models.CharField(max_length=100, blank=True, null=True)
    min_charge = models.CharField(max_length=100, blank=True, null=True)
    max_time_min = models.CharField(max_length=100, blank=True, null=True)
    badge = models.CharField(max_length=100, blank=True, null=True) # (mandatory/not)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp")
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp")

class Coupons(models.Model):

    coupon_name= models.CharField(max_length=250, blank=True, null=True)
    coupon_discount= models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp")
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp")

class Status(models.Model):

    status_name= models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)


class Subscription(models.Model):

    sub_plan_name= models.CharField(max_length=250, blank=True, null=True)
    price= models.CharField(max_length=250, blank=True, null=True)
    validity_period= models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

#!------------------------------------------------------------------------#!




class Vehicle(models.Model):
    vehicletypes = models.ForeignKey(VehicleTypes, on_delete=models.CASCADE, blank=True, null=True, related_name='vehicletypes')
    vehicle_name = models.CharField(max_length=250, blank=True, null=True)
    vehicle_number = models.CharField(max_length=250, blank=True, null=True)

    permit_front_side_img = models.TextField(max_length=100, blank=True, null=True)
    permit_front_side_img_path = models.TextField(max_length=100, blank=True, null=True)

    registration_certificate_front_side_img = models.TextField(max_length=250, blank=True, null=True)
    registration_certificate_front_side_img_path= models.TextField(max_length=250, blank=True, null=True)

    registration_certificate_back_side_img = models.TextField(max_length=250, blank=True, null=True)
    registration_certificate_back_side_img_path= models.TextField(max_length=250, blank=True, null=True)

    pollution_certificate_front_side_img = models.TextField(max_length=250, blank=True, null=True)
    pollution_certificate_front_side_img_path= models.TextField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

class Account(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='User')
    acc_holder_name = models.CharField(max_length=100, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    account_no = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code = models.CharField(max_length=100, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)


class Driver(models.Model):

    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    account  = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True, related_name='types')
    owner_id= models.CharField(max_length=250, blank=True, null=True)
    subcription = models.ForeignKey(Subscription, on_delete=models.CASCADE, blank=True, null=True)
    account  = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    driver_driving_license= models.CharField(max_length=250, blank=True, null=True)
    badge= models.CharField(max_length=250, blank=True, null=True)
    driving_license_image_path = models.CharField(max_length=250, blank=True, null=True)
    base64=  models.TextField(max_length=50000, blank=True, null=True)

    license_status= models.CharField(max_length=100, blank=True, null=True)

    validity_start_date_time= models.CharField(max_length=250, blank=True, null=True)
    validity_end_date_time = models.CharField(max_length=250, blank=True, null=True)
    driver_status = models.CharField(max_length=100, blank=True, null=True)
    vehicle_status = models.CharField(max_length=100, blank=True, null=True)
    license_expire_date = models.CharField(max_length=100, blank=True, null=True)
    permit_expire_date = models.CharField(max_length=100, blank=True, null=True)
    fitness_certificate_expire_date = models.CharField(max_length=100, blank=True, null=True)
    emission_test_expire_date = models.CharField(max_length=100, blank=True, null=True)
    insurence_expire_date = models.CharField(max_length=100, blank=True, null=True)
    rc_expire_date = models.CharField(max_length=100, blank=True, null=True)
    license_img = models.CharField(max_length=100, blank=True, null=True)
    
    # emission_test_img = models.CharField(max_length=100, blank=True, null=True)
    insurence_img = models.CharField(max_length=100, blank=True, null=True)
    rc_img = models.CharField(max_length=100, blank=True, null=True)

    passbook_img = models.CharField(max_length=100, blank=True, null=True)

    fitness_certificate_front_side_img = models.TextField(max_length=100, blank=True, null=True)
    fitness_certificate_front_side_img_path = models.TextField(max_length=100, blank=True, null=True)

    live_lattitude = models.CharField(max_length=100, blank=True, null=True)
    live_longitude = models.CharField(max_length=100, blank=True, null=True)






class CustomUser(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    role= models.ForeignKey(UserRoleRef, on_delete=models.CASCADE, blank=True, null=True)
    city= models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

    driver= models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True)

    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    mobile_number=models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    email= models.EmailField(max_length=250, blank=True, null=True)
    alternate_number= models.CharField(max_length=250, blank=True, null=True)
    zip_code= models.CharField(max_length=250, blank=True, null=True)
    address= models.CharField(max_length=250, blank=True, null=True)
    adhar_card= models.CharField(max_length=250, blank=True, null=True)
    reset_otp = models.CharField(max_length=100, null=True, blank=True)
    profile_image_path=models.TextField(max_length=250, blank=True, null=True)
    base64=  models.TextField(max_length=50000, blank=True, null=True)

    adhar_card_front_side_img= models.TextField(max_length=250, blank=True, null=True)
    adhar_card_front_side_img_path= models.TextField(max_length=250, blank=True, null=True)
    
    adhar_card_back_side_img= models.TextField(max_length=250, blank=True, null=True)
    adhar_card_back_side_img_path= models.TextField(max_length=250, blank=True, null=True)


    pan_card= models.CharField(max_length=250, blank=True, null=True)
    pan_image_path=models.TextField(max_length=250, blank=True, null=True)
    pan_card_base64=  models.TextField(max_length=50000, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

    whatsup_number  = models.CharField(max_length=100, null=True, blank=True)




class Review(models.Model):

    review_stars = models.CharField(max_length=250, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp")
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp")
    review_type = models.CharField(max_length=250, blank=True, null=True)
    linked_id = models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

class CustomerAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    label= models.CharField(max_length=250, blank=True, null=True)
    house_number= models.CharField(max_length=250, blank=True, null=True)
    address= models.CharField(max_length=250, blank=True, null=True)
    area= models.CharField(max_length=250, blank=True, null=True)
    landmark= models.CharField(max_length=250, blank=True, null=True)

    zipcode= models.CharField(max_length=250, blank=True, null=True)
    latitude= models.CharField(max_length=250, blank=True, null=True)
    longitude= models.CharField(max_length=250, blank=True, null=True)
    contact_number= models.CharField(max_length=250, blank=True, null=True)
    contact_name= models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)


class PickupDetails(models.Model):
    customer_address  = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, blank=True, null=True)

    pickup_date = models.CharField(max_length=250, blank=True, null=True)
    pickup_time = models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

class DropDetails(models.Model):

    customer_address  = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, blank=True, null=True)
    drop_date = models.CharField(max_length=250, blank=True, null=True)
    drop_time = models.CharField(max_length=250, blank=True, null=True)
    priority = models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

class PlacedOrder(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    pickup = models.ForeignKey(PickupDetails, on_delete=models.CASCADE, blank=True, null=True)
    vehicle_type = models.ForeignKey(VehicleTypes, on_delete=models.CASCADE, blank=True, null=True)
    drop= models.CharField(max_length=250, blank=True, null=True)

    estimated_kms = models.CharField(max_length=250, blank=True, null=True)
    estimated_amount = models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

class InOrder(models.Model):

    placed_order= models.ForeignKey(PlacedOrder, on_delete=models.CASCADE, blank=True, null=True)
    coupon= models.ForeignKey(Coupons, on_delete=models.CASCADE, blank=True, null=True)
    driver= models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    status_details= models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)

    final_amount= models.CharField(max_length=250, blank=True, null=True)
    comment= models.CharField(max_length=250, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

class PaymentDetails(models.Model):

    in_order  = models.ForeignKey(InOrder, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.CharField(max_length=250, blank=True, null=True)
    provider = models.CharField(max_length=250, blank=True, null=True)
    payment_status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)

    create_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="create_timestamp",blank=True, null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)

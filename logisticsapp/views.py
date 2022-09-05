#-----------import----------
from django.conf import settings
from django.db.models import base
from django.db.utils import IntegrityError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
# from requests import api
from rest_framework.response import Response
from requests.api import head, request
# import time
# import datetime
from django.utils.decorators import method_decorator
from logisticsapp.decorator import *
import requests
import random
import json
import inspect
from django.core.mail import message, send_mail, EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponsePermanentRedirect
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.serializers import Serializer
from .models import *
import jwt
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework import generics,viewsets, status
from django.contrib import auth
from .serializers import *
from rest_framework import viewsets, status
from logisticsapp.backends import *
from rest_framework.authtoken.views import ObtainAuthToken

import re
from mimetypes import guess_extension

import base64
import time
# import datetime
from datetime import datetime, timedelta
import pandas as pd

class RegistrationApiVew(APIView):
    def post(self,request):
        data = request.data
        response = {}

        role_id=data.get('role_id')
        city_id=data.get('city_id')

        first_name=data.get('first_name')
        last_name=data.get('last_name')
        mobile_number=data.get('mobile_number')
        alternate_number=data.get('alternate_number')
        email=data.get('email')
        company_name=data.get('company_name')
        address=data.get('address')
        adhar_card=data.get('adhar_card')
        zip_code=data.get('zip_code')
        password= data.get('password')
        profile_image =data.get('profile_image')

        pan_card =data.get('pan_card')
        pan_card_image =data.get('pan_card_image')


        user_role = UserRoleRef.objects.get(id=role_id)
        username = email + user_role.user_role_name
        response_result = {}
        response_result['result'] = {}
        if data:
            if User.objects.filter(Q(username=username) ).exists():
                return Response({'error':'User already exists with same role'}, status= status.HTTP_409_CONFLICT)
            else:
                create_user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)

                # profile image
                if pan_card_image != '':
                    user_details = User.objects.get(id=create_user.id)
                    user_name = str(user_details.first_name)+str(random.randint(0,1000))
                    print(pan_card_image,'pan_card_image')
                    split_base_url_data=pan_card_image.split(';base64,')[1]
                    # print(split_base_url_data,'split_base_url_data')
                    imgdata1 = base64.b64decode(split_base_url_data)

                    data_split = pan_card_image.split(';base64,')[0]
                    extension_data = re.split(':|;', data_split)[1]
                    guess_extension_data = guess_extension(extension_data)

                    # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data

                    # filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/pancard/"+user_name+guess_extension_data
                    filename1 = "/logistics/site/public/media/driving_license_file/"+user_name+guess_extension_data

                    image_name = user_name+guess_extension_data
                    ss=  open(filename1, 'wb')
                    print(ss)
                    ss.write(imgdata1)
                    ss.close()
                if pan_card_image != '':


                    user_create = CustomUser.objects.create(
                        user_id = create_user.id,
                        role_id = role_id,
                        city_id = city_id,
                        first_name = first_name,
                        last_name = last_name,
                        mobile_number = mobile_number,
                        alternate_number = alternate_number,
                        email = email,
                        company_name = company_name,
                        address = address,
                        adhar_card = adhar_card,
                        zip_code = zip_code,
                        pan_card_base64=pan_card_image
                        )
                    if pan_card_image:
                        # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                        # user_create.pan_image_path = 'http://127.0.0.1:8000/media/pancard/'+ (str(image_name))
                        user_create.pan_image_path = 'https://logistics.thestorywallcafe.com/media/pancard/'+ (str(image_name))
                        
                        user_create.save()



                if profile_image != '':


                    user_details = User.objects.get(id=create_user.id)
                    user_name = str(user_details.first_name)+str(random.randint(0,1000))
                    split_base_url_data=profile_image.split(';base64,')[1]
                    # print(split_base_url_data,'split_base_url_data')
                    imgdata1 = base64.b64decode(split_base_url_data)

                    data_split = profile_image.split(';base64,')[0]
                    extension_data = re.split(':|;', data_split)[1]
                    guess_extension_data = guess_extension(extension_data)

                    # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                    # filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/profile/"+user_name+guess_extension_data
                    filename1 = "/logistics/site/public/media/profile/"+user_name+guess_extension_data
                    image_name = user_name+guess_extension_data
                    ss=  open(filename1, 'wb')
                    print(ss)
                    ss.write(imgdata1)
                    ss.close()

                if profile_image != '':


                    user_create = CustomUser.objects.create(
                        user_id = create_user.id,
                        role_id = role_id,
                        city_id = city_id,
                        first_name = first_name,
                        last_name = last_name,
                        mobile_number = mobile_number,
                        alternate_number = alternate_number,
                        email = email,
                        company_name = company_name,
                        address = address,
                        adhar_card = adhar_card,
                        zip_code = zip_code,
                        base64=profile_image
                        )
                    if profile_image:
                        # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                        # user_create.profile_image_path = 'http://127.0.0.1:8000/media/profile/'+ (str(image_name))
                        user_create.profile_image_path = 'https://logistics.thestorywallcafe.com/media/profile/'+ (str(image_name))
                        user_create.save()


                else:
                    print('in else')
                    user_create = CustomUser.objects.create(
                        user_id = create_user.id,
                        role_id = role_id,
                        city_id = city_id,
                        first_name = first_name,
                        last_name = last_name,
                        mobile_number = mobile_number,
                        alternate_number = alternate_number,
                        email = email,
                        company_name = company_name,
                        address = address,
                        adhar_card = adhar_card,
                        zip_code = zip_code,
                        base64=profile_image,
                        pan_card=pan_card,
                        pan_card_base64=pan_card_image
                        )
                    auth_token = jwt.encode(
                                {'user_id': create_user.id, 'role_id': user_create.role_id, 'city_id': user_create.city_id,
                                }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                    authorization = 'Bearer'+' '+auth_token

                    response_result = {}
                    response_result['result'] = {
                        'result': {'data': 'Register successful',
                        'token':authorization,
                        'user_id':create_user.id,
                        'custom_user_id':user_create.id,
                        'role_id':user_role.id,
                        'username':first_name,
                        'email':user_create.email
                        }}
                    response['Authorization'] = authorization
                    response['status'] = status.HTTP_200_OK
                    return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)


                if (user_role.user_role_name == 'DRIVER'):
                    driver_driving_license=data.get('driver_driving_license')
                    badge=data.get('badge')

                    vehicle_name=data.get('vehicle_name')
                    vehicle_number=data.get('vehicle_number')
                    owner_id=data.get('owner_id') # string If Owner is a driver, then owner_ID is -1
                    license_status=data.get('license_status')
                    subcription=data.get('subcription_id')
                    driver_status =data.get('driver_status')
                    vehicle_status =data.get('vehicle_status')
                    license_expire_date =data.get('license_expire_date')
                    permit_expire_date =data.get('permit_expire_date')
                    fitness_certificate_expire_date =data.get('fitness_certificate_expire_date')
                    emission_test_expire_date =data.get('emission_test_expire_date')
                    insurence_expire_date =data.get('insurence_expire_date')
                    rc_expire_date =data.get('rc_expire_date')

                    get_days = Subscription.objects.get(id=subcription)
                    vsd = datetime.now()
                    ved = pd.to_datetime(str(vsd)) + pd.DateOffset(days=int(get_days.validity_period))
                    print(vsd,'vsd split time')
                    print(ved,'ved split time')
                    start1 = str(vsd).split(".")[0]
                    end1 = str(ved).split(".")[0]
                    print(start1,'start1 split time')
                    print(end1,'end1 split time')
                    validity_start_date_time = time.mktime(datetime.strptime(str(start1), "%Y-%m-%d %H:%M:%S").timetuple())
                    print(validity_start_date_time,'validity_start_date_time timestamp')
                    validity_end_date_time = time.mktime(datetime.strptime(str(end1), "%Y-%m-%d %H:%M:%S").timetuple())
                    print(validity_end_date_time,'validity_end_date_time timestamp')

                    user_details = User.objects.get(id=create_user.id)


                    user_name = str(user_details.first_name)+str(random.randint(0,1000))

                    driving_license_image=data.get('driving_license_image')

                    split_base_url_data=driving_license_image.split(';base64,')[1]
                    imgdata1 = base64.b64decode(split_base_url_data)

                    data_split = driving_license_image.split(';base64,')[0]
                    extension_data = re.split(':|;', data_split)[1]
                    guess_extension_data = guess_extension(extension_data)

                    # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                    # filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/driving_license/"+user_name+guess_extension_data
                    filename1 = "/logistics/site/public/media/driving_license_file/"+user_name+guess_extension_data
                    image_name = user_name+guess_extension_data
                    ss=  open(filename1, 'wb')
                    print(ss)
                    ss.write(imgdata1)
                    ss.close()
                    vehicle_create = Vehicle.objects.create(vehicle_name=vehicle_name,vehicle_number=vehicle_number,)
                    driver_data = Driver.objects.create(
                        driver_driving_license = driver_driving_license,
                        badge = badge,
                        user_id = create_user.id,
                        vehicle_id = vehicle_create.id,
                        owner_id = owner_id,
                        base64=driving_license_image,
                        subcription_id=subcription,

                        license_status=license_status,
                        validity_start_date_time=validity_start_date_time,
                        validity_end_date_time=validity_end_date_time,
                        driver_status = driver_status,
                        vehicle_status = vehicle_status,
                        license_expire_date = license_expire_date,
                        permit_expire_date = permit_expire_date,
                        fitness_certificate_expire_date = fitness_certificate_expire_date,
                        emission_test_expire_date = emission_test_expire_date,
                        insurence_expire_date = insurence_expire_date,
                        rc_expire_date = rc_expire_date,
                            )


                    response_result['result']['driver_driving_license']=  driver_data.driver_driving_license,
                    response_result['result']['badge']    = driver_data.badge,
                    response_result['result']['user_id']   = driver_data.user_id,
                    response_result['result']['vehicle_id']  = driver_data.vehicle_id,
                    response_result['result']['owner']    = driver_data.owner_id,


                    if driving_license_image:
                        # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                        # driver_data.driving_license_image_path = 'http://127.0.0.1:8000/media/driving_license/'+ (str(image_name))
                        driver_data.driving_license_image_path = 'https://logistics.thestorywallcafe.com/media/driving_license_file/'+ (str(image_name))
                        driver_data.save()


                auth_token = jwt.encode(
                            {'user_id': create_user.id, 'role_name':user_role.user_role_name,'role_id': user_create.role_id, 'city_id': user_create.city_id,
                            }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+auth_token


                response_result['result'] = {
                    'result': {'data': 'Register successful',
                    'token':authorization,
                    'user_id':create_user.id,
                    'custom_user_id':user_create.id,
                    'role_id':user_create.role_id,
                    'role_name':user_role.user_role_name,
                    'username':first_name,
                    'email':user_create.email
                    }}
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)


        else:
            return Response({'error':'Please fill all the details'})


class LoginView(APIView):


    def post(self, request):
        response = {}
        data = request.data
        username = data.get('username')
        password = data.get('password')
        role_id = data.get('role_id')
        user_role = UserRoleRef.objects.get(id=role_id)

        username = username + user_role.user_role_name

        user_check = User.objects.get(username= username)

        if user_check:
            user = auth.authenticate(username=username, password=password)

            if user:
                user_data = User.objects.get(id=user.id)
                c_user = CustomUser.objects.get(user_id=user.id)

                auth_token = jwt.encode(
                    {'user_id': user.id, 'username': user.first_name, 'email': user.email,'role_name':user_role.user_role_name,'role_id':c_user.role_id,}, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+auth_token
                response_result = {}
                response_result['result'] = {
                    'detail': 'Login successfull',
                    'user_id':user_data.id,
                    'custom_user_id':c_user.id,
                    'username':user_data.first_name,
                    'email':user_data.email,
                    'role_id':c_user.role_id,
                    'role_name':user_role.user_role_name,
                    'token':authorization,
                    'status': status.HTTP_200_OK}
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                # return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)


            else:
                header_response = {}
                response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
                return Response(response['error'], headers=header_response,status= status.HTTP_401_UNAUTHORIZED)

            return Response(response_result, headers=response,status= status.HTTP_200_OK)
        else:

            response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
            return Response(response['error'], status= status.HTTP_401_UNAUTHORIZED)


class SignUpPhoneNumberApiView(APIView):
    def post(self,request):
        data = request.data

        mobile_number = data.get('mobile_number')
        user_role_name = data.get('user_role_name')
        if UserRoleRef.objects.filter(Q(user_role_name=user_role_name)).exists():
            user_role = UserRoleRef.objects.get(user_role_name=user_role_name)
            otp = random.randint(100000, 999999)

            # user_role_ref_data = UserRoleRef.objects.create(user_role_name=user_role_name)

            if CustomUser.objects.filter(Q(mobile_number=mobile_number)).exists():
                return Response({'error':{'message':'User have  already registered'}})
            

            else:
                store_otp = CustomUser.objects.create(mobile_number=mobile_number,reset_otp=int(otp),
                role_id = user_role.id 
                )
                
                data_dict = {}
                data_dict["OTP"] = otp
            
                auth_token = jwt.encode(
                                    {'user_id': store_otp.id, 'user_role_name':user_role_name,
                                    'role_id': user_role.id,'mobile_number':mobile_number,'otp':otp

                                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                print(auth_token,'this is auth_token')
                authorization = 'Bearer'+' '+auth_token

                response_result = {}
                response = {}
                response_result['result'] = {
                            'result': {'data': 'Register successful',
                            'token':authorization,
                            'user_id':store_otp.id,
                            "mobile_number":mobile_number,
                            "user_role_name":user_role_name,
                            # 'email':user_create.email,
                            'role_id': user_role.id,
                            'otp':otp
                            # 'result':data_dict
                            
                            }}
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)
        else:
            return Response({'error':{'message':'UserRole  doesnot exists'}})




        

        

class LoginApiView(APIView):
    def post(self,request):
        data = request.data

        mobile_number = data.get('mobile_number')
            
        user_role_name = data.get('user_role_name')

       
        role = UserRoleRef.objects.get(Q(user_role_name=user_role_name))
       
        otp = random.randint(100000, 999999)
        response = {}
        if CustomUser.objects.filter(Q(mobile_number=mobile_number) ).exists():
            print("CustomUser")
            cuser = CustomUser.objects.get(Q(mobile_number=mobile_number))
            store_otp = CustomUser.objects.filter(id=cuser.id).update(reset_otp=int(otp))
            data_dict = {}
            data_dict["OTP"] = otp  

            if cuser:
                                    
                auth_token = jwt.encode(
                    {'cuser_id':cuser.id,'user_role_name':user_role_name,'role_id':role.id,"mobile_number":mobile_number,'otp':otp,
                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+auth_token
                response_result = {}
                response = {}
                response_result['result'] = {
                    'detail': 'Login successfull',
                    

                    'cuser_id':cuser.id,
                    "mobile_number":mobile_number,
                    
                    'user_role_name':user_role_name,
                    
                    'role_id':role.id,
                    'otp':otp,
                    'token':authorization,
                    'status': status.HTTP_200_OK
                    }
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)


            else:
                header_response = {}
                response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
                return Response(response['error'], headers=header_response,status= status.HTTP_401_UNAUTHORIZED)

        else:
            
            response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
            return Response(response['error'], status= status.HTTP_401_UNAUTHORIZED)

                
            
        
        


# class LoginApiView(APIView):
#     def post(self,request):
#         data = request.data

#         mobile_number = data.get('mobile_number')
        
#         user_role_name = data.get('user_role_name')
       
#         role = UserRoleRef.objects.get(Q(user_role_name=user_role_name))
       
#         otp = random.randint(100000, 999999)

#         if CustomUser.objects.filter(Q(mobile_number=mobile_number) & Q(role_id=role.id)).exists():
#             print("CustomUser")
#             cuser = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))
#             store_otp = CustomUser.objects.filter(id=cuser.id).update(reset_otp=int(otp))
           
#         else:
#             return Response({'error':{'message':'User doesnot exist'}})
            
            
#         data_dict = {}
#         data_dict["OTP"] = otp
#         return Response({'result':data_dict})






class VerifyOtpPhoneNumberApiView(APIView):
    def post(self, request):
        data = request.data
        otp_recieved = data.get('otp')
        mobile_number= data.get('mobile_number')
        user_role_name = data.get('user_role_name')
        role = UserRoleRef.objects.get(Q(user_role_name=user_role_name))
        

        if  CustomUser.objects.filter(Q(reset_otp=otp_recieved) & Q(mobile_number=mobile_number) & Q(role_id=role.id)).exists():
            return Response({'result':{'message': 'verified user'}})
        else:
            return Response({'error':{'message': 'Unauthorized!'}})



class SignupUserApiView(APIView):
    def post(self, request):
        data = request.data

        first_name  =data.get('first_name')
        last_name =data.get('last_name')
        company_name =data.get('company_name')
        mobile_number=data.get('mobile_number')
        email =data.get('email')
        whatsup_number =data.get('whatsup_number')


        if  CustomUser.objects.filter(Q(mobile_number=mobile_number)).exists():
            
            user_check = CustomUser.objects.filter(mobile_number=mobile_number).update(
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                email=email,
                whatsup_number=whatsup_number,)
            
            return Response({'result':{'message': 'User Created!'}})
        else:

            return Response({'error':{'message': 'Your not registered user, please register!'}})



class SignUpforDriverOrOwner(APIView):
    def post(self, request):
        data = request.data

        # Customuser User
        user_role_name = data.get('user_role_name')
        

        first_name=data.get('first_name')
        mobile_number=data.get('mobile_number')
        
        adhar_card_front_side_img=data.get('adhar_card_front_side_img')
        adhar_card_back_side_img=data.get('adhar_card_back_side_img')


        # adhar_card_front_side_img_path=data.get('adhar_card_front_side_img_path')

        
        # adhar_card_back_side_img_path=data.get('adhar_card_back_side_img_path')





        # Driver details
        driver_driving_license=data.get('driver_driving_license_number')
        badge=data.get('badge')

        registration_certificate_front_side_img=data.get('registration_certificate_front_side_img')
        registration_certificate_back_side_img=data.get('registration_certificate_back_side_img')
        
        pollution_certificate_front_side_img=data.get('pollution_certificate_front_side_img')


        # no mandatory
        fitness_certificate_front_side_img=data.get('fitness_certificate_front_side_img') 
        # no mandatory
        permit_front_side_img=data.get('permit_front_side_img')
        


        if UserRoleRef.objects.filter(Q(user_role_name=user_role_name)).exists():

            role = UserRoleRef.objects.get(Q(user_role_name=user_role_name))
        
            if CustomUser.objects.filter(Q(mobile_number=mobile_number) & Q(role_id=role.id) ).exists():


                user_details = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))

                user_name = str(user_details.first_name)+str(random.randint(0,1000))

                    # Spliting the base64 image and get data 
                split_adhar_card_f_url_data = adhar_card_front_side_img.split(';base64,')[1]

                    # decode the base64 and store in varibale 
                imgdata1 = base64.b64decode(split_adhar_card_f_url_data)

                    # Getting the extension fron base64 image
                data_split = adhar_card_front_side_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)


                    # Save the file path in varibale

                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                adhar_card_front_side_img_filename1 = "/logistics/site/public/media/adhar_card/"+user_name+guess_extension_data
                adhar_card_front_path = "https://logistics.thestorywallcafe.com/media/adhar_card/"+user_name+guess_extension_data
                    # Open the empty file 
                ss =  open(adhar_card_front_side_img_filename1, 'wb')
                    # write the base64 data to that empty file
                ss.write(imgdata1)
                    # close the file
                ss.close()


                
                
                

                # adhar_card_back_side_img
                user_details = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))

                user_name = str(user_details.first_name)+str(random.randint(0,1000))

                    # Spliting the base64 image and get data 
                split_adhar_card_b_url_data = adhar_card_back_side_img.split(';base64,')[1]

                    # decode the base64 and store in varibale 
                imgdata1 = base64.b64decode(split_adhar_card_b_url_data)

                    # Getting the extension fron base64 image
                data_split = adhar_card_back_side_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)


                    # Save the file path in varibale

                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                adhar_card_back_side_img_filename = "/logistics/site/public/media/adhar_card/"+user_name+guess_extension_data
                adhar_card_back_path = "https://logistics.thestorywallcafe.com/media/adhar_card/"+user_name+guess_extension_data
                    # Open the empty file 
                ss =  open(adhar_card_back_side_img_filename, 'wb')
                    # write the base64 data to that empty file
                ss.write(imgdata1)
                    # close the file
                ss.close()




                # registration_certificate_front_side_img
                user_details = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))

                user_name = str(user_details.first_name)+str(random.randint(0,1000))

                    # Spliting the base64 image and get data 
                split_registration_certificate_front_url_data = registration_certificate_front_side_img.split(';base64,')[1]

                    # decode the base64 and store in varibale 
                imgdata1 = base64.b64decode(split_registration_certificate_front_url_data)

                    # Getting the extension fron base64 image
                data_split = adhar_card_front_side_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)


                    # Save the file path in varibale

                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                registration_certificate_front_side_img_filename = "/logistics/site/public/media/registration_certificate/"+user_name+guess_extension_data
                
                registration_certificate_front_side_path = "https://logistics.thestorywallcafe.com/media/registration_certificate/"+user_name+guess_extension_data
                    # Open the empty file 
                ss =  open(registration_certificate_front_side_img_filename, 'wb')
                ss.write(imgdata1)
                ss.close()



                # registration_certificate_back_side_img
                user_details = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))

                user_name = str(user_details.first_name)+str(random.randint(0,1000))

                    # Spliting the base64 image and get data 
                split_registration_certificate_back_side_url_data = registration_certificate_back_side_img.split(';base64,')[1]

                    # decode the base64 and store in varibale 
                imgdata1 = base64.b64decode(split_registration_certificate_back_side_url_data)

                    # Getting the extension fron base64 image
                data_split = adhar_card_front_side_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)


                    # Save the file path in varibale

                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                registration_certificate_back_side_img_filename = "/logistics/site/public/media/registration_certificate/"+user_name+guess_extension_data
                registration_certificate_back_side_path = "https://logistics.thestorywallcafe.com/media/registration_certificate/"+user_name+guess_extension_data
                    # Open the empty file 
                ss =  open(registration_certificate_back_side_img_filename, 'wb')
                ss.write(imgdata1)
                ss.close()

                # pollution_certificate_front_side_img

                user_details = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))

                user_name = str(user_details.first_name)+str(random.randint(0,1000))

                    # Spliting the base64 image and get data 
                pollution_certificate_front_side_img_url_data = pollution_certificate_front_side_img.split(';base64,')[1]

                    # decode the base64 and store in varibale 
                imgdata1 = base64.b64decode(pollution_certificate_front_side_img_url_data)

                    # Getting the extension fron base64 image
                data_split = adhar_card_front_side_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)


                    # Save the file path in varibale

                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                pollution_certificate_front_side_img_url_data_filename = "/logistics/site/public/media/pollution_certificate/"+user_name+guess_extension_data
                pollution_certificate_front_side_img_path = "https://logistics.thestorywallcafe.com/media/pollution_certificate/"+user_name+guess_extension_data
                    # Open the empty file 
                ss =  open(pollution_certificate_front_side_img_url_data_filename, 'wb')
                ss.write(imgdata1)
                ss.close()
               
                driver_data = Driver.objects.create(driver_driving_license=driver_driving_license,
                                badge=badge,fitness_certificate_front_side_img=fitness_certificate_front_side_img,
                                                    )

                vehicle_data = Vehicle.objects.create(registration_certificate_front_side_img_path=registration_certificate_front_side_path,
                                                        registration_certificate_back_side_img_path=registration_certificate_back_side_path,
                                                        
                                                        registration_certificate_front_side_img=registration_certificate_front_side_img,
                                                        registration_certificate_back_side_img=registration_certificate_back_side_img,

                                                        pollution_certificate_front_side_img=pollution_certificate_front_side_img,
                                                        pollution_certificate_front_side_img_path=pollution_certificate_front_side_img_path,

                                                        permit_front_side_img=permit_front_side_img,
                                                        )


                CustomUser.objects.filter(Q(mobile_number=mobile_number) & Q(role_id=role.id) ).update(
                    driver_id=driver_data.id,
                    vehicle_id=vehicle_data.id,
                    first_name = first_name,
                    #customer
                    adhar_card_front_side_img=adhar_card_front_side_img,
                    adhar_card_back_side_img=adhar_card_back_side_img,

                    # registration_certificate_front_side_img=registration_certificate_front_side_img,
                    # registration_certificate_back_side_img=registration_certificate_back_side_img,
                    # pollution_certificate_front_side_img=pollution_certificate_front_side_img,

                    adhar_card_front_side_img_path  =  adhar_card_front_path,
                    adhar_card_back_side_img_path = adhar_card_back_path,
                    
                    )

                if  fitness_certificate_front_side_img != ' ':

                    user_details = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))

                    user_name = str(user_details.first_name)+str(random.randint(0,1000))

                        # Spliting the base64 image and get data 
                    fitness_certificate_front_side_img_url_data = fitness_certificate_front_side_img.split(';base64,')[1]

                        # decode the base64 and store in varibale 
                    imgdata1 = base64.b64decode(fitness_certificate_front_side_img_url_data)

                        # Getting the extension fron base64 image
                    data_split = adhar_card_front_side_img.split(';base64,')[0]
                    extension_data = re.split(':|;', data_split)[1]
                    guess_extension_data = guess_extension(extension_data)


                        # Save the file path in varibale

                    # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                    fitness_certificate_front_side_img_url_data_filename = "/logistics/site/public/media/fitness_certificate/"+user_name+guess_extension_data
                    fitness_certificate_front_side_img_path = "https://logistics.thestorywallcafe.com/media/fitness_certificate/"+user_name+guess_extension_data
                        # Open the empty file 
                    ss =  open(fitness_certificate_front_side_img_url_data_filename, 'wb')
                    ss.write(imgdata1)
                    ss.close()
                    


                    Driver.objects.filter(Q(id=driver_data.id) ).update(
                        fitness_certificate_front_side_img_path=fitness_certificate_front_side_img_path,
                        fitness_certificate_front_side_img=fitness_certificate_front_side_img
                    
                    )

                if  permit_front_side_img != ' ':

                    user_details = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(role_id=role.id))

                    user_name = str(user_details.first_name)+str(random.randint(0,1000))

                        # Spliting the base64 image and get data 
                    permit_front_side_img_url_data = permit_front_side_img.split(';base64,')[1]

                        # decode the base64 and store in varibale 
                    imgdata1 = base64.b64decode(permit_front_side_img_url_data)

                        # Getting the extension fron base64 image
                    data_split = adhar_card_front_side_img.split(';base64,')[0]
                    extension_data = re.split(':|;', data_split)[1]
                    guess_extension_data = guess_extension(extension_data)


                        # Save the file path in varibale

                    # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                    permit_front_side_img_url_data_filename = "/logistics/site/public/media/permit_front_side/"+user_name+guess_extension_data
                    permit_front_side_img_path = "https://logistics.thestorywallcafe.com/media/permit_front_side/"+user_name+guess_extension_data
                        # Open the empty file 
                    ss =  open(permit_front_side_img_url_data_filename, 'wb')
                    ss.write(imgdata1)
                    ss.close()  

                    Vehicle.objects.filter(Q(id=vehicle_data.id) ).update(
                        permit_front_side_img_path=permit_front_side_img_path,
                        permit_front_side_img=permit_front_side_img
                    
                    )

       

                return Response({'result':{'message': 'Driver or Owner Created!'}})
 
            else:

                return Response({'error':{'error_message': 'User DoesNotExist!'}})
        else:


            return Response({'error':{'error_message': 'User role DoesNotExist!'}})




class ForgotPasswordSendOtp(APIView):

    def post(self, request):
        data = request.data

        username = data.get('username')
        otp = random.randint(100000, 999999)

        if User.objects.filter(Q(username=username)).exists():
            update_otp = CustomUser.objects.filter(email=username).update(reset_otp=int(otp))
            print(update_otp,'update_otp')

        else:
            return Response({'error':{'message':'username doesnot exists'}})

        user_check=CustomUser.objects.get(email=username)
        email=user_check.email
        print(email,'email')
        # if '@' in username:
        message = inspect.cleandoc('''Hi ,\n %s is your OTP to Forgot Password to your logistics account.\nThis OTP is valid for next 10 minutes,
                                \nWith Warm Regards,\nTeam Logistics,
                                ''' % (Otp))
        send_mail(
            'Greetings from EzTime', message
            ,
            'farhana@ekfrazo.in',
            [email],

        )
        data_dict = {}
        data_dict["OTP"] = Otp
        return Response({'result':data_dict})


class OtpVerificationForgotpass(APIView):

    def post(self, request):
        data = request.data
        otp = data.get('otp')
        user_id = data.get('user_id')
        user_check=CustomUser.objects.get(user_id=user_id)

        if otp==user_check.reset_otp:
            update_otp = CustomUser.objects.filter(user_id=user_id).update(reset_otp=None)
            return Response({'result':{'message': 'OTP matcheds successfully'}})
        else:
            return Response({'error':{'message': 'Invalid OTP'}})


class ForgotPasswordReset(APIView):

    def post(self, request):
        data = request.data

        username = data.get('username')
        password = data.get('password')
        user_check = User.objects.filter(username= username)
        if user_check:
            user_data = User.objects.get(username= username)
            user_data.set_password(password)
            user_data.save()
            message= 'Hello!\nYour password has been updated sucessfully. '
            subject= 'Password Updated Sucessfully '
            email = EmailMessage(subject, message, to=[user_data.email])
            email.send()
            return Response({'result':{'message': 'Password Updated Sucessfully'}})
        else:
            return Response({'error':{'message': 'Please Enter Valid username'}})


class ChangePassword(APIView):

    def post(self,request):
        data         =    request.data
        user_id        =    data.get('user_id')
        new_password        =    data.get('new_password')
        old_password        =    data.get('old_password')


        print(data,'dattaaaaa')
        try:
            check_user = User.objects.get(id=user_id)
            if check_user:
                if check_user.check_password(old_password):
                    check_user.set_password(new_password)
                    check_user.save()
                    return Response({'result':'password changed successfully!'})
                else:
                    return Response({
                    'error':{'message':'incorrect old password!',
                    'status_code':status.HTTP_401_UNAUTHORIZED,
                    }},status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error':{'message':'user does not exists!',
                    'status_code':status.HTTP_404_NOT_FOUND,
                    }},status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
                return Response({
                'error':{'message':'user does not exists!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)




# @method_decorator([AutorizationRequired], name='dispatch')
class UserRoleRefView(APIView):
    def get(self,request):
        CheckAccess(request)

        id = request.query_params.get('id')
        if id:
            all_data = UserRoleRef.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = UserRoleRef.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)

        data = request.data
        user_role_name=data.get('user_role_name')


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = UserRoleRef.objects.create(
                                        user_role_name=user_role_name,)


            posts = UserRoleRef.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        user_role_name=data.get('user_role_name')

        try:
            emp_role= UserRoleRef.objects.filter(id=pk).update(
                                        user_role_name=user_role_name,)



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):

        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = UserRoleRef.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})



# @method_decorator([AutorizationRequired], name='dispatch')
class CityView(APIView):
    def get(self,request):
        CheckAccess(request)

        id = request.query_params.get('id')
        if id:
            all_data = City.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = City.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data

        city_name=data.get('city_name')


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = City.objects.create(city_name=city_name,)


            posts = City.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        city_name=data.get('city_name')
        try:
            emp_role= City.objects.filter(id=pk).update(city_name=city_name,
                                            )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = City.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})


# @method_decorator([AutorizationRequired], name='dispatch')
class VehicleTypesView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = VehicleTypes.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = VehicleTypes.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        vehicle_type_name=data.get('vehicle_type_name')
        capacity=data.get('capacity')
        size=data.get('size')
        details=data.get('details')
        per_km_price = data.get('per_km_price')
        min_charge = data.get('min_charge')
        max_time_min = data.get('max_time_min')
        badge = data.get('badge')

        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            VehicleTypes.objects.create(
                                            vehicle_type_name=vehicle_type_name,
                                            capacity=capacity,
                                            size=size,
                                            details=details,
                                            per_km_price=per_km_price,
                                            min_charge = min_charge,
                                            max_time_min = max_time_min,
                                            badge = badge,)


            posts = VehicleTypes.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        vehicle_type_name=data.get('vehicle_type_name')
        capacity=data.get('capacity')
        size=data.get('size')
        details=data.get('details')
        min_charge = data.get('min_charge')
        max_time_min = data.get('max_time_min')
        badge = data.get('badge')

        try:
            VehicleTypes.objects.filter(id=pk).update(
                vehicle_type_name=vehicle_type_name,
                capacity=capacity,
                size=size,
                details=details,
                min_charge = min_charge,
                max_time_min = max_time_min,
                badge = badge,
                )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = VehicleTypes.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})



@method_decorator([AutorizationRequired], name='dispatch')
class CustomUserView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = CustomUser.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = CustomUser.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        user=data.get('user_id')
        role=data.get('role_id')
        city=data.get('city_id')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        company_name=data.get('company_name')
        mobile_number=data.get('mobile_number')
        alternate_number=data.get('alternate_number')
        zip_code=data.get('zip_code')
        address=data.get('address')
        adhar_card=data.get('adhar_card')

        profile_image =data.get('profile_image')
        if profile_image != '':
            user_details = User.objects.get(id=user_id)
            user_name = str(user_details.first_name)+str(random.randint(0,1000))
            split_base_url_data=profile_image.split(';base64,')[1]
            print(split_base_url_data,'split_base_url_data')
            imgdata1 = base64.b64decode(split_base_url_data)

            data_split = profile_image.split(';base64,')[0]
            extension_data = re.split(':|;', data_split)[1]
            guess_extension_data = guess_extension(extension_data)

            # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
            filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/profile/"+user_name+guess_extension_data
            image_name = user_name+guess_extension_data
            ss=  open(filename1, 'wb')
            print(ss)
            ss.write(imgdata1)
            ss.close()



            selected_page_no =1
            page_number = request.GET.get('page')
            if page_number:
                selected_page_no = int(page_number)


            try:
                user_create = CustomUser.objects.create(
                                                user_id=user,
                                                role_id=role,
                                                city_id=city,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                company_name=company_name,
                                                mobile_number=mobile_number,
                                                alternate_number=alternate_number,
                                                zip_code=zip_code,
                                                address=address,
                                                adhar_card=adhar_card,
                                                base64=profile_image,

                                                )

                if profile_image:
                        # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                        user_create.profile_image_path = 'http://127.0.0.1:8000/media/profile/'+ (str(image_name))
                        user_create.save()


                posts = CustomUser.objects.all().values()
                paginator = Paginator(posts,10)
                try:
                    page_obj = paginator.get_page(selected_page_no)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                return Response({'result':{'status':'Created','data':list(page_obj)}})

            except IntegrityError as e:
                error_message = e.args
                return Response({
                'error':{'message':'DB error!',
                'detail':error_message,
                'status_code':status.HTTP_400_BAD_REQUEST,
                }},status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                user_create = CustomUser.objects.create(
                                                user_id=user,
                                                role_id=role,
                                                city_id=city,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                company_name=company_name,
                                                mobile_number=mobile_number,
                                                alternate_number=alternate_number,
                                                zip_code=zip_code,
                                                address=address,
                                                adhar_card=adhar_card,
                                                )




                posts = CustomUser.objects.all().values()
                paginator = Paginator(posts,10)
                try:
                    page_obj = paginator.get_page(selected_page_no)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                return Response({'result':{'status':'Created','data':list(page_obj)}})

            except IntegrityError as e:
                error_message = e.args
                return Response({
                'error':{'message':'DB error!',
                'detail':error_message,
                'status_code':status.HTTP_400_BAD_REQUEST,
                }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        user=data.get('user_id')
        role=data.get('role_id')
        city=data.get('city_id')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        company_name=data.get('company_name')
        mobile_number=data.get('mobile_number')
        alternate_number=data.get('alternate_number')
        zip_code=data.get('zip_code')
        address=data.get('address')
        adhar_card=data.get('adhar_card')

        profile_image =data.get('profile_image')
        if profile_image != '':
            user_details = User.objects.get(id=user_id)
            user_name = str(user_details.first_name)+str(random.randint(0,1000))
            split_base_url_data=profile_image.split(';base64,')[1]
            print(split_base_url_data,'split_base_url_data')
            imgdata1 = base64.b64decode(split_base_url_data)

            data_split = profile_image.split(';base64,')[0]
            extension_data = re.split(':|;', data_split)[1]
            guess_extension_data = guess_extension(extension_data)

            # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
            filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/profile/"+user_name+guess_extension_data
            image_name = user_name+guess_extension_data
            ss=  open(filename1, 'wb')
            print(ss)
            ss.write(imgdata1)
            ss.close()



            selected_page_no =1
            page_number = request.GET.get('page')
            if page_number:
                selected_page_no = int(page_number)


            try:
                CustomUser.objects.filetr(user_id=user,).update(
                                                user_id=user,
                                                role_id=role,
                                                city_id=city,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                company_name=company_name,
                                                mobile_number=mobile_number,
                                                alternate_number=alternate_number,
                                                zip_code=zip_code,
                                                address=address,
                                                adhar_card=adhar_card,
                                                base64=profile_image,

                                                )
                user_get = CustomUser.objects.get(user_id=user,)
                if profile_image:
                        # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                        user_get.profile_image_path = 'http://127.0.0.1:8000/media/profile/'+ (str(image_name))
                        user_get.save()


                posts = CustomUser.objects.all().values()
                paginator = Paginator(posts,10)
                try:
                    page_obj = paginator.get_page(selected_page_no)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                return Response({'result':{'status':'Created','data':list(page_obj)}})

            except IntegrityError as e:
                error_message = e.args
                return Response({
                'error':{'message':'DB error!',
                'detail':error_message,
                'status_code':status.HTTP_400_BAD_REQUEST,
                }},status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                user_create = CustomUser.objects.filetr(user_id=user,).update(

                                                role_id=role,
                                                city_id=city,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                company_name=company_name,
                                                mobile_number=mobile_number,
                                                alternate_number=alternate_number,
                                                zip_code=zip_code,
                                                address=address,
                                                adhar_card=adhar_card,
                                                )




                posts = CustomUser.objects.all().values()
                paginator = Paginator(posts,10)
                try:
                    page_obj = paginator.get_page(selected_page_no)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                return Response({'result':{'status':'Created','data':list(page_obj)}})

            except IntegrityError as e:
                error_message = e.args
                return Response({
                'error':{'message':'DB error!',
                'detail':error_message,
                'status_code':status.HTTP_400_BAD_REQUEST,
                }},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = CustomUser.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})



# @method_decorator([AutorizationRequired], name='dispatch')
class PaymentDetailView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            owner_data = PaymentDetails.objects.filter(id=id).values()
            releated_drivers = Driver.objects.filter(owner_id=id).values()
            print(owner_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not owner_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':owner_data,'releated_drivers':releated_drivers}})


        else:
            owner_data = PaymentDetails.objects.all().values()
            return Response({'result':{'status':'GET','data':owner_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data


        in_order_id =data.get('in_order_id')
        amount=data.get('amount')
        provider=data.get('provider')
        pay_status=data.get('pay_status_id')




        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)

        try:
            payment_details = PaymentDetails.objects.create(
                                            in_order_id=in_order_id,
                                            amount=amount,
                                            provider=provider,
                                            pay_status_id=pay_status,
                                            )


            posts = PaymentDetails.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data


        in_order_id =data.get('in_order_id')
        amount=data.get('amount')
        provider=data.get('provider')
        pay_status=data.get('pay_status_id')

        try:
            emp_role= PaymentDetails.objects.filter(id=pk).update(
                                            in_order_id=in_order_id,
                                            amount=amount,
                                            provider=provider,
                                            pay_status_id=pay_status,
                                            )




        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = PaymentDetails.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})





# @method_decorator([AutorizationRequired], name='dispatch')
class DriverView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        response={}
        if id:
            try:
                driver_data = Driver.objects.get(id=id)

                # owner_data = Owner.objects.filter(id=driver_data.owner_id).values()
                driver_details = {
                                                'user_id':driver_data.user_id,
                                                # 'role_id':driver_data.role_id,
                                                # 'city_id':driver_data.city_id,
                                                'owner':driver_data.owner,
                                                # 'driver_name':driver_data.driver_name,
                                                # 'driver_phone_number':driver_data.driver_phone_number,
                                                'driver_driving_license':driver_data.driver_driving_license,
                                                'badge':driver_data.badge,
                                                # 'aadhaar_card':driver_data.aadhaar_card,


                }
                return Response({'result':{'status':'GET by Id','driver_details':driver_details}})
            except Driver.DoesNotExist as e:
                error_message = e.args
                return Response({
                'error':{'message':'Driver not exists error!',
                'detail':error_message,
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
            except IntegrityError as e:
                error_message = e.args
                return Response({
                'error':{'message':'DB error!',
                'detail':error_message,
                'status_code':status.HTTP_400_BAD_REQUEST,
                }},status=status.HTTP_400_BAD_REQUEST)
        else:
            driver_data = Driver.objects.all().values()
            return Response({'result':{'status':'GET','data':driver_data}})

        # if id:
        #     driver_datas = Driver.objects.filter(id=id)
        #     if driver_datas:
        #         driver_data = Driver.objects.get(id=id)
        #
        #         # owner_data = Owner.objects.filter(id=driver_data.owner_id).values()
        #         driver_details = {
        #                                         'user_id':driver_data.user_id,
        #                                         # 'role_id':driver_data.role_id,
        #                                         # 'city_id':driver_data.city_id,
        #                                         'owner':driver_data.owner,
        #                                         # 'driver_name':driver_data.driver_name,
        #                                         # 'driver_phone_number':driver_data.driver_phone_number,
        #                                         'driver_driving_license':driver_data.driver_driving_license,
        #                                         'badge':driver_data.badge,
        #                                         # 'aadhaar_card':driver_data.aadhaar_card,
        #
        #
        #         }
        #
        #
        #         print(driver_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')
        #
        #         if not driver_data:
        #             return Response({
        #             'error':{'message':'Record not found!',
        #             'status_code':status.HTTP_404_NOT_FOUND,
        #             }},status=status.HTTP_404_NOT_FOUND)
        #
        #         return Response({'result':{'status':'GET by Id','driver_details':driver_details}})
        #     else:
        #         header_response = {}
        #         response['error'] = {'error': {
        #                 'detail': 'Record not found!', 'status': status.HTTP_401_UNAUTHORIZED}}
        #         return Response(response['error'], status=status.HTTP_400_BAD_REQUEST)
        #
        #
        # else:
        #     driver_data = Driver.objects.all().values()
        #     return Response({'result':{'status':'GET','data':driver_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data

        driver_driving_license=data.get('driver_driving_license')
        badge=data.get('badge')
        user_id=data.get('user_id')
        vehicle_id=data.get('vehicle_id')
        owner=data.get('owner_id') # string If Owner is a driver, then owner_ID is -1
        license_status=data.get('license_status')
        subcription=data.get('subcription_id')

        get_month = Subscription.objects.get(id=subcription)
        vsd = datetime.now()
        ved = pd.to_datetime(str(vsd)) + pd.DateOffset(months=int(get_month.validity_period))
        start1 = str(vsd).split(" ")[0]
        end1 = str(ved).split(" ")[0]
        # print(start1,'start1 split time')
        # print(end1,'end1 split time')
        validity_start_date = time.mktime(datetime.strptime(str(start1), "%Y-%m-%d").timetuple())
        # print(validity_start_date,'validity_start_date timestamp')
        validity_end_date = time.mktime(datetime.strptime(str(end1), "%Y-%m-%d").timetuple())
        # print(validity_end_date,'validity_end_date timestamp')



        user_details = User.objects.get(id=user_id)


        user_name = str(user_details.first_name)+str(random.randint(0,1000))

        driving_license_image=data.get('driving_license_image')
        license_img=data.get('license_img')
        permit_img=data.get('permit_img')
        fitness_certificate_img=data.get('fitness_certificate_img')
        emission_test_img=data.get('emission_test_img')
        insurence_img=data.get('insurence_img')
        rc_img=data.get('rc_img')
        passbook_img=data.get('passbook_img')

        # split_base_url_data=driving_license_image.split(';base64,')[1]
        # imgdata1 = base64.b64decode(split_base_url_data)
        # data_split = driving_license_image.split(';base64,')[0]
        # extension_data = re.split(':|;', data_split)[1]
        # guess_extension_data = guess_extension(extension_data)
        # # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
        # filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/driving_license/"+user_name+guess_extension_data
        # image_name = user_name+guess_extension_data
        # ss=  open(filename1, 'wb')
        # print(ss)
        # ss.write(imgdata1)
        # ss.close()


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            driver_data = Driver.objects.create(
                driver_driving_license = driver_driving_license,
                badge = badge,
                user_id = user_id,
                vehicle_id = vehicle_id,
                owner = owner,
                base64=driving_license_image,
                subcription_id=subcription,

                license_status=license_status,
                validity_start_date=validity_start_date,
                validity_end_date=validity_end_date,

                    )

            driver_details ={
                'driver_driving_license': driver_data.driver_driving_license,
                'badge': driver_data.badge,
                'user_id': driver_data.user_id,
                'vehicle_id': driver_data.vehicle_id,
                'owner': driver_data.owner,
            }

            if driving_license_image:
                split_base_url_data=driving_license_image.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = driving_license_image.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/driving_license/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.driving_license_image_path = 'http://127.0.0.1:8000/media/driving_license/'+ (str(image_name))
                driver_data.save()
            if license_img:
                split_base_url_data=license_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = license_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/license_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.license_img = 'http://127.0.0.1:8000/media/license_img/'+ (str(image_name))
                driver_data.save()
            if permit_img:
                split_base_url_data=permit_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = permit_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/permit_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.permit_img = 'http://127.0.0.1:8000/media/permit_img/'+ (str(image_name))
                driver_data.save()

            if fitness_certificate_img:
                split_base_url_data=fitness_certificate_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = fitness_certificate_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/fitness_certificate_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.fitness_certificate_img = 'http://127.0.0.1:8000/media/fitness_certificate_img/'+ (str(image_name))
                driver_data.save()

            if emission_test_img:
                split_base_url_data=emission_test_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = emission_test_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/emission_test_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.emission_test_img = 'http://127.0.0.1:8000/media/emission_test_img/'+ (str(image_name))
                driver_data.save()

            if insurence_img:
                split_base_url_data=insurence_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = insurence_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/insurence_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.insurence_img = 'http://127.0.0.1:8000/media/insurence_img/'+ (str(image_name))
                driver_data.save()

            if rc_img:
                split_base_url_data=rc_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = rc_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/rc_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.rc_img = 'http://127.0.0.1:8000/media/rc_img/'+ (str(image_name))
                driver_data.save()

            if passbook_img:
                split_base_url_data=passbook_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = passbook_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/passbook_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.passbook_img = 'http://127.0.0.1:8000/media/passbook_img/'+ (str(image_name))
                driver_data.save()

            posts = Driver.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created',"created_driver_data":driver_details,'all_driver_data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data

        driver_driving_license=data.get('driver_driving_license')
        badge=data.get('badge')
        user_id=data.get('user_id')
        vehicle_id=data.get('vehicle_id')

        owner=data.get('owner') # string
        license_status=data.get('license_status')


        subcription=data.get('subcription_id')

        get_month = Subscription.objects.get(id=subcription)
        vsd = datetime.now()
        ved = pd.to_datetime(str(vsd)) + pd.DateOffset(months=int(get_month.validity_period))
        start1 = str(vsd).split(" ")[0]
        end1 = str(ved).split(" ")[0]
        # print(start1,'start1 split time')
        # print(end1,'end1 split time')
        validity_start_date = time.mktime(datetime.strptime(str(start1), "%Y-%m-%d").timetuple())
        # print(validity_start_date,'validity_start_date timestamp')
        validity_end_date = time.mktime(datetime.strptime(str(end1), "%Y-%m-%d").timetuple())
        # print(validity_end_date,'validity_end_date timestamp')


        user_details = User.objects.get(id=user_id)


        user_name = str(user_details.first_name)+str(random.randint(0,1000))

        # base64=data.get('base64')
        #
        #
        #
        # driving_license_image=data.get('driving_license_image')
        #
        # split_base_url_data=driving_license_image.split(';base64,')[1]
        # imgdata1 = base64.b64decode(split_base_url_data)
        #
        # data_split = driving_license_image.split(';base64,')[0]
        # extension_data = re.split(':|;', data_split)[1]
        # guess_extension_data = guess_extension(extension_data)
        #
        # # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
        # filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/driving_license/"+user_name+guess_extension_data
        # image_name = user_name+guess_extension_data
        # ss=  open(filename1, 'wb')
        # print(ss)
        # ss.write(imgdata1)
        # ss.close()



        try:
            Driver.objects.filter(id=pk).update(

                driver_driving_license = driver_driving_license,
                badge = badge,
                user_id = user_id,
                vehicle_id = vehicle_id,
                owner = owner,
                base64=driving_license_image,
                subcription_id=subcription,
                validity_start_date = validity_start_date,
                validity_end_date = validity_end_date,
                license_status=license_status,

            )
            driver_data = Driver.objects.get(id=pk)
            if driving_license_image:
                split_base_url_data=driving_license_image.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = driving_license_image.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/driving_license/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.driving_license_image_path = 'http://127.0.0.1:8000/media/driving_license/'+ (str(image_name))
                driver_data.save()
            if license_img:
                split_base_url_data=license_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = license_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/license_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.license_img = 'http://127.0.0.1:8000/media/license_img/'+ (str(image_name))
                driver_data.save()
            if permit_img:
                split_base_url_data=permit_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = permit_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/permit_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.permit_img = 'http://127.0.0.1:8000/media/permit_img/'+ (str(image_name))
                driver_data.save()

            if fitness_certificate_img:
                split_base_url_data=fitness_certificate_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = fitness_certificate_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/fitness_certificate_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.fitness_certificate_img = 'http://127.0.0.1:8000/media/fitness_certificate_img/'+ (str(image_name))
                driver_data.save()

            if emission_test_img:
                split_base_url_data=emission_test_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = emission_test_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/emission_test_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.emission_test_img = 'http://127.0.0.1:8000/media/emission_test_img/'+ (str(image_name))
                driver_data.save()

            if insurence_img:
                split_base_url_data=insurence_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = insurence_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/insurence_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.insurence_img = 'http://127.0.0.1:8000/media/insurence_img/'+ (str(image_name))
                driver_data.save()

            if rc_img:
                split_base_url_data=rc_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = rc_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/rc_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.rc_img = 'http://127.0.0.1:8000/media/rc_img/'+ (str(image_name))
                driver_data.save()

            if passbook_img:
                split_base_url_data=passbook_img.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                data_split = passbook_img.split(';base64,')[0]
                extension_data = re.split(':|;', data_split)[1]
                guess_extension_data = guess_extension(extension_data)
                # filename1 = "/eztime/site/public/media/driving_license_file/"+user_name+guess_extension_data
                filename1 = "/Users/apple/Documents/Ekfrazo/Django/logistics/Logistics/Logistics/media/passbook_img/"+user_name+guess_extension_data
                image_name = user_name+guess_extension_data
                ss=  open(filename1, 'wb')
                print(ss)
                ss.write(imgdata1)
                ss.close()

                # course_data.thumbnail_link = 'https://logistics.thestorywallcafe.com/media/file_attachment/'+ (str(course_data.thumbnail)).split('thumbnail/')[1]
                driver_data.passbook_img = 'http://127.0.0.1:8000/media/passbook_img/'+ (str(image_name))
                driver_data.save()




        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = Driver.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})





# @method_decorator([AutorizationRequired], name='dispatch')
class ReviewApiView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = Review.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = Review.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        print('data',data)
        review_stars=data.get('review_stars')
        comment=data.get('comment')
        review_type=data.get('review_type')
        linked_id=data.get('linked_id')


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = Review.objects.create(
                                            review_stars=review_stars,
                                            comment=comment,
                                            review_type=review_type,
                                            linked_id=linked_id
                                        )


            posts = Review.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data

        data = request.data
        review_stars=data.get('review_stars')
        comment=data.get('comment')
        review_type=data.get('review_type')
        linked_id=data.get('linked_id')


        try:
            emp_role= Review.objects.filter(id=pk).update(review_stars=review_stars,
                                                            comment=comment,
                                                            review_type=review_type,
                                                            linked_id=linked_id
                                        )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = Review.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})



# @method_decorator([AutorizationRequired], name='dispatch')
class VehicleView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = Vehicle.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = Vehicle.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        vehicletypes=data.get('vehicletypes_id')
        vehicle_name=data.get('vehicle_name')
        vehicle_number=data.get('vehicle_number')



        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = Vehicle.objects.create(
                                            vehicletypes_id=vehicletypes,
                                            vehicle_name=vehicle_name,
                                            vehicle_number=vehicle_number,
                                        )


            posts = Vehicle.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)


        data = request.data

        vehicletypes=data.get('vehicletypes_id')
        vehicle_name=data.get('vehicle_name')
        vehicle_number=data.get('vehicle_number')


        try:
            emp_role= Vehicle.objects.filter(id=pk).update(vehicletypes_id=vehicletypes,
                                            vehicle_name=vehicle_name,
                                            vehicle_number=vehicle_number,
                                        )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = Vehicle.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})



# @method_decorator([AutorizationRequired], name='dispatch')
class CustomerAddressView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = CustomerAddress.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = CustomerAddress.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        user=data.get('user_id')
        city=data.get('city_id')
        label=data.get('label')
        house_number=data.get('house_number')
        address=data.get('address')
        area=data.get('area')
        landmark=data.get('landmark')
        zipcode=data.get('zipcode')
        latitude=data.get('latitude')
        longitude=data.get('longitude')
        contact_number=data.get('contact_number')
        contact_name=data.get('contact_name')


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = CustomerAddress.objects.create(
                                            user_id=user,
                                            city_id=city,
                                            label=label,
                                            house_number=house_number,
                                            address=address,
                                            area=area,
                                            landmark=landmark,
                                            zipcode=zipcode,
                                            latitude=latitude,
                                            longitude=longitude,
                                            contact_number=contact_number,
                                            contact_name=contact_name,
                                        )


            posts = CustomerAddress.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        user=data.get('user_id')
        city=data.get('city_id')
        label=data.get('label')
        house_number=data.get('house_number')
        address=data.get('address')
        area=data.get('area')
        landmark=data.get('landmark')
        zipcode=data.get('zipcode')
        latitude=data.get('latitude')
        longitude=data.get('longitude')
        contact_number=data.get('contact_number')
        contact_name=data.get('contact_name')

        try:
            emp_role= CustomerAddress.objects.filter(id=pk).update(user_id=user,
                                            city_id=city,
                                            label=label,
                                            house_number=house_number,
                                            address=address,
                                            area=area,
                                            landmark=landmark,
                                            zipcode=zipcode,
                                            latitude=latitude,
                                            longitude=longitude,
                                            contact_number=contact_number,
                                            contact_name=contact_name,
                                        )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = CustomerAddress.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})




# @method_decorator([AutorizationRequired], name='dispatch')
class PickupDetailsView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = PickupDetails.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = PickupDetails.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        customer_address_id = data.get('customer_address_id')
        pd = data.get('pickup_date_time')

        pickup_date_time = time.mktime(datetime.datetime.strptime(pd, "%d/%m/%Y %I:%M %p").timetuple())

        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = PickupDetails.objects.create(
                                            customer_address_id=customer_address_id,
                                            pickup_date_time = pickup_date_time,
                                        )


            posts = PickupDetails.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        customer_address_id = data.get('customer_address_id')
        pd = data.get('pickup_date_time')
        pt = data.get('pickup_time')

        pickup_date_time = time.mktime(datetime.datetime.strptime(pd, "%d/%m/%Y %I:%M %p").timetuple())
        try:
            emp_role= PickupDetails.objects.filter(id=pk).update(
                                            customer_address_id=customer_address_id,
                                            pickup_date_time = pickup_date_time,
                                        )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = PickupDetails.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})



# @method_decorator([AutorizationRequired], name='dispatch')
class DropDetailsView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = DropDetails.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = DropDetails.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        customer_address_id=data.get('customer_address_id')
        priority=data.get('priority')
        ddt = data.get('drop_date_time')

        drop_date_time = time.mktime(datetime.strptime(ddt, "%d/%m/%Y %I:%M %p").timetuple())


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = DropDetails.objects.create(
                                            customer_address_id=customer_address_id,
                                            priority=priority,
                                            drop_date_time=drop_date_time,
                                        )


            posts = DropDetails.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        customer_address_id=data.get('customer_address_id')
        priority=data.get('priority')
        ddt = data.get('drop_date_time')

        drop_date_time = time.mktime(datetime.datetime.strptime(ddt, "%d/%m/%Y %I:%M %p").timetuple())


        try:
            emp_role= DropDetails.objects.filter(id=pk).update(customer_address_id=customer_address_id,
                                            priority=priority,
                                            drop_date_time=drop_date_time,
                                        )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = DropDetails.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})


# @method_decorator([AutorizationRequired], name='dispatch')
class PlacedOrderView(APIView):
    def get(self,request):
        CheckAccess(request)
        user_id = request.query_params.get('user_id')
        role_id = request.query_params.get('role_id')
        id = request.query_params.get('id')
       
        try:
            get_sub_id = Driver.objects.get(user_id=user_id)
        except Driver.DoesNotExist as e:
            error_message = e.args
            return Response({
            'error':{'message':'Driver not exists error!',
            'detail':error_message,
            'status_code':status.HTTP_404_NOT_FOUND,
            }},status=status.HTTP_404_NOT_FOUND)
        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

        now_date_date = datetime.now()
        now_date = str(now_date_date).split(" ")[0]
        now = time.mktime(datetime.strptime(str(now_date), "%Y-%m-%d").timetuple())



        if id:
            if (get_sub_id.validity_end_date <= now & get_sub_id.license_status == '1' ):
                all_data = PlacedOrder.objects.filter(id=id).values()
                print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

                if not all_data:
                    return Response({
                    'error':{'message':'Record not found!',
                    'status_code':status.HTTP_404_NOT_FOUND,
                    }},status=status.HTTP_404_NOT_FOUND)

                return Response({'result':{'status':'GET by Id','data':all_data}})
            else:
                return Response({
                    'error':{'message':'You are not authorized to get the orders, Please contact admin!',
                    'status_code':status.HTTP_401_UNAUTHORIZED,
                    }},status=status.HTTP_401_UNAUTHORIZED)
        else:
            if (float(get_sub_id.validity_end_date) >= float(now) and get_sub_id.license_status == '1'):
                all_data = PlacedOrder.objects.all().values()
                return Response({'result':{'status':'GET','data':all_data}})
            else:
                return Response({
                    'error':{'message':'You are not authorized to get the orders, Please contact admin!',
                    'status_code':status.HTTP_401_UNAUTHORIZED,
                    }},status=status.HTTP_401_UNAUTHORIZED)

        

    def post(self,request):
        CheckAccess(request)
        data = request.data
        # print(data,'dataaaaaaaaaaaa')
        user=data['user_id']
        pickup_id=data['pickup_id']
        drop_id_list=data['drop_id_list']#only 3
        vehicle_type_id=data['vehicle_type_id']
        print(data,'dataaaa')
        response = {}
        # time.mktime(datetime.datetime.strptime(pd, "%d/%m/%Y %I:%M %p").timetuple())
        if len(drop_id_list)>3:
            header_response = {}
            response['error'] = {'error': {
                    'detail': 'you can select only 3 stops', 'status': status.HTTP_401_UNAUTHORIZED}}
            return Response(response['error'], status=status.HTTP_400_BAD_REQUEST)
        else:

            drop_list = []

            for i in pickup_id:
                try:
                    print(i,'city')
                    pickup_address = CustomerAddress.objects.create(
                                                    user_id=user,
                                                    city_id=int(i['city_id']),
                                                    label=i['label'],
                                                    house_number=i['house_number'],
                                                    address=i['address'],
                                                    area=i['area'],
                                                    landmark=i['landmark'],
                                                    zipcode=i['zipcode'],
                                                    latitude=i['latitude'],
                                                    longitude=i['longitude'],
                                                    contact_number=i['contact_number'],
                                                    contact_name=i['contact_name'],
                                                )


                except IntegrityError as e:
                    error_message = e.args
                    return Response({
                    'error':{'message':'DB error!',
                    'detail':error_message,
                    'status_code':status.HTTP_400_BAD_REQUEST,
                    }},status=status.HTTP_400_BAD_REQUEST)

                try:
                    pickup_date = time.mktime(datetime.strptime(i['pickup_date'], "%d/%m/%Y").timetuple())
                    pickup_detail = PickupDetails.objects.create(
                                                    customer_address_id=pickup_address.id,
                                                    pickup_date = pickup_date,
                                                    pickup_time = i['pickup_time']
                                                )

                except IntegrityError as e:
                    error_message = e.args
                    return Response({
                    'error':{'message':'DB error!',
                    'detail':error_message,
                    'status_code':status.HTTP_400_BAD_REQUEST,
                    }},status=status.HTTP_400_BAD_REQUEST)


            for j in drop_id_list:
                try:
                    drop_address = CustomerAddress.objects.create(
                                                    user_id=user,
                                                    city_id=j['city_id'],
                                                    label=j['label'],
                                                    house_number=j['house_number'],
                                                    address=j['address'],
                                                    area=j['area'],
                                                    landmark=j['landmark'],
                                                    zipcode=j['zipcode'],
                                                    latitude=j['latitude'],
                                                    longitude=j['longitude'],
                                                    contact_number=j['contact_number'],
                                                    contact_name=j['contact_name'],
                                                )




                except IntegrityError as e:
                    error_message = e.args
                    return Response({
                    'error':{'message':'DB error!',
                    'detail':error_message,
                    'status_code':status.HTTP_400_BAD_REQUEST,
                    }},status=status.HTTP_400_BAD_REQUEST)


                try:
                    drop_date = time.mktime(datetime.strptime(j['drop_date'], "%d/%m/%Y").timetuple())

                    drop_details = DropDetails.objects.create(
                                                    customer_address_id=drop_address.id,
                                                    priority=j['priority'],
                                                    drop_date =drop_date,
                                                    drop_time = j['drop_time']
                                                )
                    drop_list.append(drop_details.id)
                except IntegrityError as e:
                    error_message = e.args
                    return Response({
                    'error':{'message':'DB error!',
                    'detail':error_message,
                    'status_code':status.HTTP_400_BAD_REQUEST,
                    }},status=status.HTTP_400_BAD_REQUEST)


            try:
                get_price_km = VehicleTypes.objects.get(id=vehicle_type_id )
                est_km = 100
                est_cost = est_km * int(get_price_km.per_km_price)
                client_order = PlacedOrder.objects.create(
                                                user_id=user,
                                                pickup_id=pickup_detail.id,
                                                vehicle_type_id=vehicle_type_id,
                                                drop=drop_list,
                                                estimated_kms=est_km,
                                                estimated_amount=est_cost,
                                            )


                place_order = PlacedOrder.objects.all().values()

                return Response({'result':{'status':'Created','place_order':place_order}})

            except IntegrityError as e:
                    error_message = e.args
                    return Response({
                    'error':{'message':'DB error!',
                    'detail':error_message,
                    'status_code':status.HTTP_400_BAD_REQUEST,
                    }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        user=data.get('user_id')
        pickup=data.get('pickup_id')
        drop=data.get('drop')
        estimated_kms=data.get('estimated_kms')
        estimated_amount=data.get('estimated_amount')

        try:
            emp_role= PlacedOrder.objects.filter(id=pk).update(user_id=user,
                                            pickup_id=pickup,
                                            drop=drop,
                                            estimated_kms=estimated_kms,
                                            estimated_amount=estimated_amount,)



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = PlacedOrder.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})




# @method_decorator([AutorizationRequired], name='dispatch')
class CouponsView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = Coupons.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = Coupons.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        coupon_name=data.get('coupon_name')
        coupon_discount=data.get('coupon_discount')


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = Coupons.objects.create(
                                            coupon_name=coupon_name,
                                            coupon_discount=coupon_discount,
                                        )


            posts = Coupons.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)


        data = request.data
        coupon_name=data.get('coupon_name')
        coupon_discount=data.get('coupon_discount')

        try:
            emp_role= Coupons.objects.filter(id=pk).update(coupon_name=coupon_name,
                                            coupon_discount=coupon_discount,)



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = Coupons.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})





# @method_decorator([AutorizationRequired], name='dispatch')
class StatusView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = Status.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = Status.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        status_name=data.get('status_name')



        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = Status.objects.create(
                                            status_name=status_name,

                                        )


            posts = Status.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)


        data = request.data
        status_name=data.get('status_name')


        try:
            emp_role= Status.objects.filter(id=pk).update(status_name=status_name,
                                            )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = Status.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})







# @method_decorator([AutorizationRequired], name='dispatch')
class InOrderView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = InOrder.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = InOrder.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        placed_order=data.get('placed_order_id')
        coupon=data.get('coupon_id')
        driver=data.get('driver_id')
        status_detail=data.get('status_details_id')
        final_amount=data.get('final_amount')
        comment=data.get('comment')



        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = InOrder.objects.create(placed_order_id=placed_order,
                                                coupon_id=coupon,
                                                driver_id=driver,
                                                status_details_id=status_detail,
                                                final_amount=final_amount,
                                                comment=comment,

                                        )


            posts = InOrder.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)


        data = request.data
        placed_order=data.get('placed_order_id')
        coupon=data.get('coupon_id')
        driver=data.get('driver_id')
        status_detail=data.get('status_details_id')
        final_amount=data.get('final_amount')
        comment=data.get('comment')


        try:
            emp_role= InOrder.objects.filter(id=pk).update(placed_order_id=placed_order,
                                                coupon_id=coupon,
                                                driver_id=driver,
                                                status_details_id=status_detail,
                                                final_amount=final_amount,
                                                comment=comment,

                                            )



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = InOrder.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})


#------------------- Master -----------------------------
# @method_decorator([AutorizationRequired], name='dispatch')
class SubscriptionView(APIView):
    def get(self,request):
        CheckAccess(request)
        id = request.query_params.get('id')
        if id:
            all_data = Subscription.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = Subscription.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        sub_plan_name=data.get('sub_plan_name')
        price=data.get('price')
        validity_period=data.get('validity_period')


        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = Subscription.objects.create(sub_plan_name=sub_plan_name,
                                                    price=price,
                                                    validity_period=validity_period,

                                        )


            posts = Subscription.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)


        data = request.data
        sub_plan_name=data.get('sub_plan_name')
        price=data.get('price')
        validity_period=data.get('validity_period')


        try:
            emp_role= Subscription.objects.filter(id=pk).update(sub_plan_name=sub_plan_name,
                                                    price=price,
                                                    validity_period=validity_period,

                                            )


        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = Subscription.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})





# @method_decorator([AutorizationRequired], name='dispatch')
class AccountView(APIView):
    def get(self,request):
        CheckAccess(request)

        id = request.query_params.get('id')
        if id:
            all_data = Account.objects.filter(id=id).values()
            print(all_data,'AAAAAAAAAAAAAAAAAAAAAAAAAA')

            if not all_data:
                return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

            return Response({'result':{'status':'GET by Id','data':all_data}})


        else:
            all_data = Account.objects.all().values()
            return Response({'result':{'status':'GET','data':all_data}})

    def post(self,request):
        CheckAccess(request)
        data = request.data
        user_id=data.get('user_id')
        acc_holder_name=data.get('acc_holder_name')
        bank=data.get('bank')
        branch=data.get('branch')
        account_no=data.get('account_no')
        ifsc_code=data.get('ifsc_code')



        selected_page_no =1
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)


        try:
            emp_role = Account.objects.create(user_id=user_id,
                                            acc_holder_name=acc_holder_name,
                                            bank=bank,branch=branch,
                                            account_no=account_no,
                                            ifsc_code=ifsc_code)




            posts = Account.objects.all().values()
            paginator = Paginator(posts,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Created','data':list(page_obj)}})

        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data

        user_id=data.get('user_id')
        acc_holder_name=data.get('acc_holder_name')
        bank=data.get('bank')
        branch=data.get('branch')
        account_no=data.get('account_no')
        ifsc_code=data.get('ifsc_code')


        try:
            emp_role= Account.objects.filter(id=pk).update(user_id=user_id,
                                            acc_holder_name=acc_holder_name,
                                            bank=bank,branch=branch,
                                            account_no=account_no,
                                            ifsc_code=ifsc_code)



        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':{'status':'Updated'}})

    def delete(self,request,pk):
        return_data = CheckAccess(request)
        print(return_data,'return auth')
        if return_data != 1:
            return JsonResponse({'error': {"code": "AUTHENTICATION_FAILURE", 'message': 'You not authories to perform this operation'}}, status=status.HTTP_401_UNAUTHORIZED)

        test = (0,{})


        all_values = Account.objects.filter(id=pk).delete()
        if test == all_values:

            return Response({
                'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            # all_values = EmployeeDetail.objects.filter(id=pk).delete()
            return Response({'result':{'status':'deleted'}})



class DriverLatitudeLongitudeView(APIView):
    def post(self,request):
        data = request.data
        driver_id = data.get('driver_id')
        live_lattitude = data.get('live_lattitude')
        live_longitude = data.get('live_longitude')

        driver_log_lat = Driver.objects.filter(id=driver_id).update(
            live_lattitude=live_lattitude,live_longitude=live_longitude
        )

        return Response({'result':{'status':'Driver Live Location Updated'}})




class UserDestinationsView(APIView):
    def post(self,request):
        data = request.data
        driver_reg_no = data.get('driver_reg_no')
        destination_array = data.get('destination_array')

        print(destination_array,'destination_array')

        # driver_log_lat = Driver.objects.filter(id=driver_id).update(
        #     live_lattitude=live_lattitude,live_longitude=live_longitude
        # )

        return Response({'result':{'status':'Driver destination_array recieved'}})

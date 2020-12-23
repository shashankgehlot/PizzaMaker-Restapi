from rest_framework import generics,status
from .serializer import pizza_type_serializer, pizza_size_serializer, pizza_toppings_serializer, user_pizza_serializer
from .models import pizza_size, pizza_type, pizza_toppings, user_pizza
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
# from rest_framework import status
# Create your views here.
from rest_framework import viewsets

class Pizzatoppingview(generics.GenericAPIView):
    """ This class is used to Get Pizza toppings data and
        add PizzaTopping data to database
    """

    serializer_class = pizza_toppings_serializer
    def get(self, request, format=None):
        self.data=pizza_toppings.objects.all()
        self.serializer=self.get_serializer(self.data,many=True)
        return Response({
            "data": self.serializer.data,
            "status": status.HTTP_200_OK
        })

    def post(self,request,*args,**kwargs):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            "status": status.HTTP_201_CREATED
        })




class PizzaToppingDeleteView(generics.GenericAPIView):
    """ This class is used to Delete Topping data
    this class is called when Delete method is called with deletetopping/toppingname
    here "toppingname" should exist in database.Other wise it will rise error
    """

    def delete(self,request,*args,**kwargs):
        try:
            self.data=kwargs['topping']
            self.instance = pizza_toppings.objects.get(pizza_toppings=self.data)
            self.instance.delete()
        except pizza_toppings.DoesNotExist:
             raise CustomValidation('Data For Given pizza toppings do not exist', 'data', status_code=status.HTTP_404_NOT_FOUND)
        return Response({
            "status": status.HTTP_202_ACCEPTED
        })

class PizzaSizeDeleteView(generics.GenericAPIView):
    """ This class is used to Delete Topping data
    this class is called when Delete method is called with deletesize/size
    here "size" should exist in database.Other wise it will rise error

    """
    def delete(self,request,*args,**kwargs):
        try:
            self.data=kwargs['size']
            self.instance = pizza_size.objects.get(pizza_size=self.data)
            self.instance.delete()
        except pizza_size.DoesNotExist:
             raise CustomValidation('Data For Given pizza size do not exist', 'data', status_code=status.HTTP_404_NOT_FOUND)
        return Response({
            "status": status.HTTP_202_ACCEPTED
        })

class PizzaTypeDeleteView(generics.GenericAPIView):
    """ This class is used to Delete Topping data
        this class is called when Delete method is called with deletetype/type
        here "type" should exist in database.Other wise it will rise error
        """
    def delete(self,request,*args,**kwargs):
        try:
            self.data=kwargs['type']
            self.instance = pizza_type.objects.get(pizza_type=self.data)
            self.instance.delete()
        except pizza_type.DoesNotExist:
             raise CustomValidation('Data For Given pizza type do not exist', 'data', status_code=status.HTTP_404_NOT_FOUND)
        return Response({
            "status": status.HTTP_202_ACCEPTED
        })


class Pizzasizeview(generics.GenericAPIView):
    """ This class is used to Get Pizzasize data and
           add Pizza-size data to database
    """

    serializer_class = pizza_size_serializer
    def get(self, request, format=None):
        self.data=pizza_size.objects.all()
        self.serializer=self.get_serializer(self.data,many=True)
        return Response({
            "data": self.serializer.data,
            "status": status.HTTP_200_OK
        })

    def post(self,request,*args,**kwargs):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            "status": status.HTTP_201_CREATED
        })



class Pizzatypeview(generics.GenericAPIView):
    """ This class is used to Get Pizzatype data and
              add Pizza-type data to database
    """
    serializer_class = pizza_type_serializer
    def get(self, request, format=None):
        self.data=pizza_type.objects.all()
        self.serializer=self.get_serializer(self.data,many=True)
        return Response({
            "data": self.serializer.data,
            "status": status.HTTP_200_OK
        })

    def post(self,request,*args,**kwargs):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            "status": status.HTTP_201_CREATED

        })



class makepizza(generics.GenericAPIView):
    """ User can make Pizza with the help of this class
        Model contains Field "pizzatypes","pizzasizes".
        field "pizzatoppings" is json field which can store nested data
    """
    serializer_class = user_pizza_serializer
    def get(self, request, format=None):
        self.data = user_pizza.objects.all()
        self.serializer = self.get_serializer(self.data, many=True)
        return Response({
            "data": self.serializer.data,
            "status": status.HTTP_200_OK
        })

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            "status": status.HTTP_201_CREATED
        })





class getpizzabyid(generics.GenericAPIView):
    """  with  help of getpizzabyid class we can get the data by id
         we can delete data by id
         we can update data by id
    """
    serializer_class = user_pizza_serializer
    def get(self, request,*args,**kwargs):
        try:
            self.data = user_pizza.objects.get(id=kwargs['id'])
            self.serializer = self.get_serializer(self.data)
        except user_pizza.DoesNotExist:
             raise CustomValidation('Data For Given id do not exist', 'data', status_code=status.HTTP_404_NOT_FOUND)
        return Response({
            "data": self.serializer.data,
            "status": status.HTTP_200_OK
        })

    def delete(self, request,*args,**kwargs):
         try:
             self.instance = user_pizza.objects.get(id=kwargs['id'])
             self.instance.delete()
         except user_pizza.DoesNotExist:
             raise CustomValidation('Data For Given id is already deleted', 'data', status_code=status.HTTP_404_NOT_FOUND)
         return Response({
             "status": status.HTTP_202_ACCEPTED
         })

    def put(self, request, *args, **kwargs):
        try:
            self.instance = user_pizza.objects.get(id=kwargs['id'])
            self.serializer = self.get_serializer(self.instance, data=request.data)
            self.serializer.is_valid(raise_exception=True)
            self.serializer.save()
        except user_pizza.DoesNotExist:
             raise CustomValidation('Data For Given id do not exist', 'data', status_code=status.HTTP_404_NOT_FOUND)
        return Response({
            "status": status.HTTP_202_ACCEPTED,
            "Message":"Data Updated"
        })




class filterpizza(viewsets.ViewSet):
     """
         with help of get_selected_pizza_type class we can get the get all the
         pizza made by user by filter type and Filter size.
         Filtering is based on Fields-values which exist in database.
         if fields doesnt not exist for query There function will rise validation error

     """
     def get_selected_pizza_type(self,request,*args,**kwargs):
         try:
            self.data = user_pizza.objects.all().filter(pizzatypes=kwargs['type'])
            self.serializer = user_pizza_serializer(self.data, many=True)
            if self.serializer.data==[]:
                raise CustomValidation('Data For Given pizza type do not exist', 'data',
                                       status_code=status.HTTP_404_NOT_FOUND)
            return Response({
                "data": self.serializer.data,
                "status": status.HTTP_200_OK
            })
         except user_pizza.DoesNotExist:
             raise CustomValidation('Data For Given pizza type do not exist', 'data', status_code=status.HTTP_404_NOT_FOUND)


     def get_selected_pizza_size(self,request,*args,**kwargs):
         try:
            self.data = user_pizza.objects.all().filter(pizzasizes=kwargs['size'])
            self.serializer = user_pizza_serializer(self.data, many=True)
            if self.serializer.data==[]:
                raise CustomValidation('Data For Given pizza type do not exist', 'data',
                                       status_code=status.HTTP_404_NOT_FOUND)
         except user_pizza.DoesNotExist:
             raise CustomValidation('Data For Given pizza size do not exist', 'data', status_code=status.HTTP_404_NOT_FOUND)
         return Response({
             "data": self.serializer.data,
             "status": status.HTTP_200_OK
         })







class CustomValidation(APIException):
    """
     To rise custom validation errors
    """
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else: self.detail = {'detail': force_text(self.default_detail)}
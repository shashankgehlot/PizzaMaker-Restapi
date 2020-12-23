from rest_framework import serializers
from .models import pizza_type,pizza_size,pizza_toppings,user_pizza



class pizza_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_type
        fields ='__all__'
        extra_kwargs = {"pizza_type": {"error_messages": {"required": "This Field is required"}}}

class pizza_size_serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_size
        fields = '__all__'


class pizza_toppings_serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_toppings
        fields = '__all__'
        extra_kwargs = {"pizza_toppings": {"error_messages": {"required": "This Field is required"}}}


class pizza_toppings_serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_toppings
        fields = '__all__'
        extra_kwargs = {"pizza_toppings": {"error_messages": {"required": "This Field is required"}}}


class user_pizza_serializer(serializers.ModelSerializer):

    class Meta:
        model = user_pizza
        fields = '__all__'
        extra_kwargs = {"pizzatypes": {"error_messages": {"required": "This Field is required"}},
                        "pizzasizes": {"error_messages": {"required": "This Field is required"}},
                        "pizzatoppings":{"required": "This Field is required"}}

    def validate(self, data):
        """
        if topping input put by user is not in database it will rise  validation error
        """
        list_toppings=[]
        for i in pizza_toppings.objects.all():
            list_toppings.append(i.pk)
        if 'pizzatoppings' not in data :
                raise serializers.ValidationError("Please choose  Toppings from Toppings options. options are:" + str(list_toppings))

        if data['pizzatoppings']  :
            for i in range(len(data['pizzatoppings'])):
                if (data['pizzatoppings'][i]['pizzatoppings'] in list_toppings) == False:
                    raise serializers.ValidationError("choose from Toppings options.options are"+str(list_toppings))

        return data








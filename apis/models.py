from django.db import models



# Create your models here.
class pizza_type(models.Model):
    pizza_type = models.CharField(default="regular",primary_key=True,max_length=40)
    def __str__(self):
        return self.pizza_type


class pizza_size(models.Model):
    pizza_size = models.CharField(primary_key=True,max_length=40)
    def __str__(self):
        return self.pizza_size

class pizza_toppings(models.Model):
    pizza_toppings = models.CharField(primary_key=True,unique=True,max_length=40)

    def __str__(self):
        return self.pizza_toppings





class user_pizza(models.Model):
      pizzatypes=models.ForeignKey(pizza_type,on_delete=models.CASCADE)
      pizzasizes=models.ForeignKey(pizza_size,on_delete=models.CASCADE)
      pizzatoppings=models.JSONField(default=dict,null=False,blank=False)

      def __str__(self):
          return str(self.pizzatypes)+" "+str(self.pizzasizes)




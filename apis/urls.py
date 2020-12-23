from django.urls import path
from .views import Pizzatypeview,Pizzasizeview,Pizzatoppingview,makepizza\
                    ,PizzaToppingDeleteView,filterpizza,getpizzabyid,PizzaSizeDeleteView,PizzaTypeDeleteView


urlpatterns = [
    path('pizzatype/',Pizzatypeview.as_view()),
    path('pizzasize/',Pizzasizeview.as_view()),
    path('pizzatopping/',Pizzatoppingview.as_view()),
    path('makepizza/',makepizza.as_view()),
    path('deletetopping/<str:topping>', PizzaToppingDeleteView.as_view()),
    path('deletesize/<str:size>', PizzaSizeDeleteView.as_view()),
    path('deletetype/<str:type>', PizzaTypeDeleteView.as_view()),
    path('makepizza/<int:id>', getpizzabyid.as_view()),
    path('filtertype/<str:type>', filterpizza.as_view({'get': 'get_selected_pizza_type'})),
    path('filtersize/<str:size>', filterpizza.as_view({'get': 'get_selected_pizza_size'})),
    ]

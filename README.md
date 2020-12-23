# PizzaMaker-Restapi
## Restapi For Pizza Management:
### This Application Uses Django-rest-Framework For Pizza Management.
<br>

*By Using this appication Admin can Add Pizzatypes to Database*<br>
*By Using this appication Admin can Add Pizzasizes to Database*<br>
*By Using this appication Admin can Add Pizzatoppings to Database*<br>
*By Usinng this application Admin filter Order based on Pizzatype and Pizzasize*<br>
<br>
*Based On Data about Pizzatypes,Pizzasizes,Pizzatoppings in Database 
Input provided by EndUser is Validated if If input Field not Present in Database
Api will Raise validation errors*

## DataBase Schema

| Tables        | ColumnsName   |        
| ------------- |:-------------:|          
| pizza_type   | `pizza_type` (varchar) |
| pizza_size      | `pizza_size` (varchar)      | 
| pizza_toppings  |  `pizza_toppings` (varchar)             |
| user_pizza      |   `pizza_type` (Forignkey), `pizza_size`(Forignkey), `Pizzajson`(json)|
  <br>

### Api Endpoints Details
<code>
    path('pizzatype/',Pizzatypeview.as_view())<br>
    path('pizzasize/',Pizzasizeview.as_view())
    path('pizzatopping/',Pizzatoppingview.as_view())
    path('makepizza/',makepizza.as_view())
    path('deletetopping/<str:topping>', PizzaToppingDeleteView.as_view())
    path('deletesize/<str:size>', PizzaSizeDeleteView.as_view())
    path('deletetype/<str:type>', PizzaTypeDeleteView.as_view())
    path('makepizza/<int:id>', getpizzabyid.as_view())
    path('filtertype/<str:type>', filterpizza.as_view({'get': 'get_selected_pizza_type'}))
    path('filtersize/<str:size>', filterpizza.as_view({'get': 'get_selected_pizza_size'}))
</code>

###EndPoint Details
### On Url
```
pizzatype/
```
Can take Request  `GET` ,`POST`<br>
On GET Request: Expected Response if data Is Present in data Base
```
{
    "data": [
        {
            "pizza_type": "Regular"
        },
        {
            "pizza_type": "Square"
        },
        {
            "pizza_type": "Hexagonal"
        }
    ],
    "status": 302
}
```
On Post Request: with key `pizza_type`
![sg](./Media/Post_Pizzatype.png)<br>

Expected Response:

```
{
    "status": 201
}
```



                     
 



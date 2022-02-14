from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    total_amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()

    def __str__(self):
        return "order_id:" + str(self.order_id)


class OrderUpdate(models.Model):
    UPDATES = [
        ("Stg1", "Order has been placed."),
        ("Stg2", "Order packed and out for delivery."),
        ("Stg3", "Order Delivered!")
    ]
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(
        max_length=5000, choices=UPDATES, default=UPDATES[0][0])
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id) + " - " + self.update_desc.split()[-1]

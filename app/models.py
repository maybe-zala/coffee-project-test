from django.db import models

# Create your models here.

class Inventory(models.Model):
    ingredient = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    units_avail = models.IntegerField()

    def __str__(self):
        return self.ingredient + " avail: " + str(self.units_avail)

    def get_absolute_url(self):
        return "/inventory"

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product_name + " with Price: " + str(self.price)

    def available(self):
        return all(recipe_req.enough() for recipe_req in self.reciperequirement_set.all())

    def get_absolute_url(self):
        return "/menu"
    
    def cost(self):
        item_cost = 0
        for recipe_req in self.reciperequirement_set.all():
            item_cost += recipe_req.ingredient.price
        return item_cost
    
    def profit(self):
        item_cost = self.cost()
        item_profit = self.price - item_cost
        return item_profit

class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.ingredient.ingredient + " in " + self.menu_item.product_name

    def enough(self):
        return self.quantity <= self.ingredient.units_avail

    def get_absolute_url(self):
        return "/recipe"

class Purchase(models.Model):
    menu_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_item.product_name + " at " + self.timestamp
    
    def get_absolute_url(self):
        return "/purchase"

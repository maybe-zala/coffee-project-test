from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

class InventoryListView(ListView):
    template_name = "inventory.html"
    model = Inventory
    context_object_name = "inventory_list"

class MenuListView(ListView):
    template_name = "menu.html"
    model = Product
    context_object_name = "menu_list"

class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = "inventory_update.html"
    form_class = InventoryUpdateForm
    context_object_name = "inventory_update"

class InventoryCreateView(CreateView):
    model = Inventory
    template_name = "inventory_create.html"
    form_class = InventoryCreateForm
    context_object_name = "inventory_create"

class ProductCreateView(CreateView):
    model = Product
    template_name = "menu_create.html"
    form_class = ProductCreateForm
    context_object_name = "menu_create"

class RecipeRequirementListView(ListView):
    template_name = "recipe.html"
    model = RecipeRequirement
    context_object_name = "recipe_list"

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    template_name = "recipe_create.html"
    form_class = RecipeCreateForm
    context_object_name = "recipe_create"

class PurchaseListView(ListView):
    template_name = "purchase.html"
    model = Purchase
    context_object_name = "purchase_list"

class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "purchase_create.html"
    form_class = PurchaseCreateForm
    context_object_name = "purchase_create"

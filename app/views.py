from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.views import View
from app.froms import RecipeForm,CreateUserForm
from django.contrib import messages
from app.models import FoodRecipe
# Create your views here.
class ProductView(View):
    def get(self,request):
        veg =FoodRecipe.objects.filter(category='VR')
        nonveg =FoodRecipe.objects.filter(category='NVR')
        other = FoodRecipe.objects.filter(category='O')
       
        return render(request,'index.html',{'veg':veg,'nonveg':nonveg,'other':other})

class RecipeView(View):
    def get(self,request):
        veg =FoodRecipe.objects.filter(category='VR')
        nonveg =FoodRecipe.objects.filter(category='NVR')
        other = FoodRecipe.objects.filter(category='O')
       
        return render(request,'recipes.html',{'veg':veg,'nonveg':nonveg,'other':other})


class RecipeDetailView(View):
    def get(self,request,pk):
        rdetail=FoodRecipe.objects.get(pk=pk)
        return render(request,'single-recipe.html',{'rdetail':rdetail})
    
def createrecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added!")
            return redirect('/')
        else:
            messages.error(request, "Please fill in all the fields.")
    
    context={'form':form}
    return render(request, 'createrecipe.html', context)

def crecipe(request):
    return render(request, 'createrecipe.html')

def updateRecipe(request, pk):

	recipe = FoodRecipe.objects.get(id=pk)
	form =RecipeForm(instance=recipe)

	if request.method == 'POST':
		form = RecipeForm(request.POST, instance=recipe)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
     'recipe':recipe,
     'form':form
     }
	return render(request, 'createrecipe.html', context)


def deleteOrder(request, pk):
	recipe = FoodRecipe.objects.get(id=pk)
	if request.method == "POST":
		recipe.delete()
		return redirect('/')

	context = {'item':recipe}
	return render(request, 'delete.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request,"Account created for " + user)
            return redirect("login")
    context={'form':form}
    return render(request,'registration.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,'Username Or Password is incorrect')
            
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
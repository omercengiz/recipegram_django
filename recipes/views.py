from django.shortcuts import HttpResponse, redirect, render,get_object_or_404,reverse
from .forms import RecipeForm
from .models import Recipe,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def recipes(request):
    keyword = request.GET.get("keyword")

    if keyword:
        recipes = Recipe.objects.filter(title__contains = keyword)
        return render(request,"recipes.html",{"recipes":recipes}) 
    
    recipes = Recipe.objects.all()

    return render(request,"recipes.html",{"recipes":recipes})



def index(request):
    context = {
        "numbers":[1,2,3,4,5,6]
    }
    return render(request,"index.html",context)     


def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    recipes = Recipe.objects.filter(author = request.user)

    context = {
        "recipes":recipes
    }

    return render(request,"dashboard.html",context) 

@login_required(login_url="user:login")
def addRecipe(request):
    form = RecipeForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        recipe = form.save(commit=False)
        
        recipe.author = request.user
        recipe.save()

        messages.success(request,"It is created successfully")
        return redirect("recipes:dashboard")

    return render(request,"addrecipe.html",{"form":form})


def detail(request,id):
    # recipe = Recipe.objects.filter(id = id).first()
    recipe = get_object_or_404(Recipe, id = id)

    comments =recipe.comments.all()


    return render(request,"detail.html",{"recipe":recipe,"comments":comments})

@login_required(login_url="user:login")
def updateRecipe(request,id):
    recipe = get_object_or_404(Recipe, id = id)
    form  = RecipeForm(request.POST or None,request.FILES or None,instance=recipe)
    if form.is_valid():
        recipe = form.save(commit=False) 
        
        recipe.author = request.user
        recipe.save()
        
        messages.success(request,"It is updated successfully")
        return redirect("recipes:dashboard")
    return render(request,"update.html",{"form":form})


@login_required(login_url="user:login")
def deleteRecipe(request,id):
    recipe = get_object_or_404(Recipe, id = id)
    recipe.delete()

    messages.success(request,"It is deleted successfully")
    

    return redirect("recipes:dashboard")


def addComment(request,id):

    recipe = Recipe.objects.get(pk=id)

    
    if request.POST:
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(recipe = recipe, comment_author = comment_author, comment_content = comment_content)

        newComment.save() 

    return redirect(reverse("recipes:detail",kwargs={"id":id}))

    
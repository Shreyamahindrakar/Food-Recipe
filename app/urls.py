from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.ProductView.as_view(), name="home"),
    path('recipe/',views.RecipeView.as_view(),name="recipe"),
    path('recipe-detail/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('create_recipe/', views.createrecipe, name="create_recipe"),
    path('crecipe/',views.crecipe,name="crecipe"),
    path('update_recipe/<int:pk>/', views.updateRecipe, name="update_recipe"),
    path('delete_recipe/<int:pk>/', views.deleteOrder, name="delete_recipe"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

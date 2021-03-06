# Generated by Django 3.2.8 on 2022-06-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(blank=True, max_length=122, null=True)),
                ('ingredient', models.TextField(blank=True, help_text='Ingredient used for making recipe', null=True)),
                ('description', models.TextField(blank=True, help_text='Description used for making recipe', null=True)),
                ('category', models.CharField(choices=[('VR', 'Vegetarian recipes'), ('NVR', 'Vegetarian recipes')], max_length=22)),
                ('recipe_image', models.ImageField(upload_to='recipeimg')),
            ],
        ),
    ]

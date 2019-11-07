# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 11:54:58 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 12:46:40 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Recipe:
    def __init__(self, name, cooking_time, cooking_lvl, description, recipe_type, ingredients):
        try :
            cooking_lvl = int(cooking_lvl)
            cooking_time = int(cooking_time)
  #          if name == "" or cooking_lvl > 5 or cooking_lvl < 1 or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert") or cooking_time < 0 or len(ingredients) == 0 or isinstance(ingredients, list) == False:
   #             print("Error during the processing of the given arguments. -2 ")
        #        sys.exit(0)
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.recipe_type = recipe_type
            self.name = name
            self.description = description
        except ValueError:
            print("Error during the processing of the given arguments.")

    def __str__(self, name):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += name + " :\nCooking level is : %i\nApproximatively %i minutes of preparation.\nIngredients required for %s are : %l\nThis meal is a %s and this is its description :%s\n" % (self.cooking_lvl, self.cooking_time, name, self.ingredients, self.recipe_type, self.description)
        return txt
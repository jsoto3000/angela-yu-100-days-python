###Hirst Painting Project Part 1
###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# $12 Million Stuffed Shark: The Curious Economics of Contemporary Art Paperback
# by Donald N. Thompson (Author)

import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


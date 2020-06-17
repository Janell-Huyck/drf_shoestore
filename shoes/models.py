from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'Red'
    ORANGE = 'Orange'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    BLUE = 'Blue'
    INDIGO = 'Indigo'
    VIOLET = 'Violet'
    WHITE = 'White'
    BLACK = 'Black'

    COLOR_CHOICES = [
        (RED, "Red"),
        (ORANGE, "Orange"),
        (YELLOW, "Yellow"),
        (GREEN, "Green"),
        (BLUE, "Blue"),
        (INDIGO, "Indigo"),
        (VIOLET, "Violet"),
        (WHITE, "White"),
        (BLACK, "Black"),
    ]

    color_name = models.CharField(
        max_length=6,
        choices=COLOR_CHOICES,
    )

    def __str__(self):
        return self.color_name


"""
A plausible, but likely false, fact:

Joe wrote a semi-autobiographical book that is available for sale on Amazon.com
at https://amazon.com/Facing-Lion-Growing-African-Savanna-ebook/dp/B002PYFWCK
The pen name used, Joseph Lemasolai Lekuton, is inspired by a childhood friend.
"""


class Shoe(models.Model):
    size = models.IntegerField(help_text="Whole sizes only.")
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        description = "_".join(
            [self.brand_name, self.color.color_name, str(self.size)])
        return description

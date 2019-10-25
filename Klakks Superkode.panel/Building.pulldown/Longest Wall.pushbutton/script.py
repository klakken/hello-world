# Finds the longest wall in the model. 

__title__ = "Longest\nWall"
__author__ = 'Mats K. Sundklakk'

# Collects the relevant classes 
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory,    \
                                UnitUtils, DisplayUnitType

# The script only applies to the shown revit document
doc = __revit__.ActiveUIDocument.Document

# Collects all the walls for the current revit document
wall_collector = FilteredElementCollector(doc)  \
                .OfCategory(BuiltInCategory.OST_Walls)  \
                .WhereElementIsNotElementType()

# Creates empty variables
wall_count = 0
longest_wall = 0

# Function that returns the input number as meters
def meter(double):
    	return UnitUtils.ConvertFromInternalUnits(double, DisplayUnitType.DUT_METERS)

# Iterates and counts walls to collect length data.
for wall in wall_collector:
    len_param = wall.LookupParameter('Length') 
    wall_count += 1

    if len_param and len_param.AsDouble() > longest_wall:
        longest_wall = len_param.AsDouble()

# Defines a variable to be run through the 
# convertion function and return the result in meters
longest = meter(longest_wall)

# Prints the number of walls and the longest wall
print("The number of walls is: {}".format(wall_count))
print("Longest Wall is: {}".format(longest) + " m")
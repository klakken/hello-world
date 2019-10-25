# Calculates the total Wall length of all walls in the document

__title__ = 'Total\nWall Length'
__author__ = 'Mats K. Sundklakk, Multiconsult'

# Imports relevant classes
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, UnitUtils, DisplayUnitType

# The scrips only applies to the shown revit document
doc = __revit__.ActiveUIDocument.Document

# Collects all the walls for the current revit document
wall_collector = FilteredElementCollector(doc).	\
				OfCategory(BuiltInCategory.OST_Walls).	\
				WhereElementIsNotElementType()

# Create an empty variable
total_length = 0.0

# Function that returns the input number as meters
def meter(double):
    	return UnitUtils.ConvertFromInternalUnits(double, DisplayUnitType.DUT_METERS)

# Iterate over walls and collect wall length data
for wall in wall_collector:
	length_param = wall.LookupParameter("Length")
	
	if length_param:
		total_length += meter(length_param.AsDouble())

# Collected the total length of all walls		
print("Total Wall Length is: {}".format(total_length) + " m")
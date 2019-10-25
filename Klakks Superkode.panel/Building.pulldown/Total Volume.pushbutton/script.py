# Calculates the total volume of all walls in the model. 

__title__ = "Total\nVolume"
__author__ = 'Mats K. Sundklakk'

# Collects the relevant classes 
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory,    \
                                UnitUtils, DisplayUnitType

# The script only applies to the shown revit document
doc = __revit__.ActiveUIDocument.Document

# Collects all the walls for the current revit document
wall_collector = FilteredElementCollector(doc)  \
                    .OfCategory(BuiltInCategory.OST_Walls)    \
                    .WhereElementIsNotElementType()


# Function that returns the input number as cubic meters
def cubic_meter(double):
    return UnitUtils.ConvertFromInternalUnits(double, DisplayUnitType.DUT_CUBIC_METERS)

# Create an empty variable
total_volume = 0.0

# Iterate over walls and collect Volume data
for wall in wall_collector:
    vol_param = wall.LookupParameter('Volume')
    
    if vol_param:
            total_volume += cubic_meter(vol_param.AsDouble())

# Collected the total volume of all walls
print("Total Volume is: {}".format(total_volume) + " m" + chr(0x00B3))
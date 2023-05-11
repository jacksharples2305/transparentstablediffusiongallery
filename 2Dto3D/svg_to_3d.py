import bpy
from pathlib import Path
from datetime import datetime

root = Path("C:/Users/Jack/Documents/PhD/Year 1/AI Challenge/demo")
#Remove the blender default cube
bpy.ops.object.select_all(action='DESELECT')

bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()

#Load the svg and extrude it
for file in root.glob('*.svg'):
    fp = str(file.resolve())
    bpy.ops.import_curve.svg(filepath=fp)
for curve in bpy.data.curves[:]:
    curve.extrude = .001

#Save the model and export it to be 3d printed
now = datetime.now() # current date and time
t = str(now.strftime("%H%M%S"))

bpy.ops.wm.save_as_mainfile(filepath='C:/Users/Jack/Documents/PhD/Year 1/AI Challenge/demo/jewelry_'+t+'.blend')
bpy.ops.export_mesh.stl(filepath='C:/Users/Jack/Documents/PhD/Year 1/AI Challenge/demo/jewelry_'+t+'.stl')
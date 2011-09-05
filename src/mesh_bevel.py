'''
Created on 25 Aug 2011

@author: User
'''

import bpy

def bevel(obj):
    """Bevels selected edges of the mesh
        Arguments:
            @obj (Object): An object with a mesh
            It should have some edges selected
        This function should only be called in Edit Mode.
    """
    
    edge = bpy.types.MeshEdge
    obj = bpy.types.Object
    bevel = bpy.types.BevelModifier

    bpy.ops.object.editmode_toggle()
    #add Bevel modifier
    bpy.ops.object.modifier_add(type='BEVEL')
    
    bevel = obj.modifiers[-1]
    bevel.limit_method = 'WEIGHT'
    bevel.edge_weight_method = 'LARGEST'
    
    for edge in obj.data.edges:
        if edge.select:
            edge.bevel_weight = 1.0
    
    bpy.ops.object.modifier_apply(apply_as = 'DATA', modifier = bevel.name)
    
    bpy.ops.object.editmode_toggle()
    #bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    
            
bevel(bpy.context.active_object)
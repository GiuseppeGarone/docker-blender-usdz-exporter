import bpy


def get_file_ext(filename):
    return filename.split('.')[-1]


def import_glb(filepath):
    bpy.ops.import_scene.gltf(filepath=filepath)


def purge_orphans():
    if bpy.app.version >= (3, 0, 0):
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True,
            do_linked_ids=True,
            do_recursive=True
        )
    else:
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != 'CANCELLED':
            purge_orphans()


def clear_scene():
    if len(bpy.data.cameras) > 0:
        for cam in bpy.data.cameras:
            print('Removing camera {}'.format(cam.name))
            bpy.data.cameras.remove(cam)
    if len(bpy.data.lights) > 0:
        for light in bpy.data.lights:
            print('Removing light {}'.format(light.name))
            bpy.data.lights.remove(light)
    if len(bpy.data.materials) > 0:
        for mat in bpy.data.materials:
            if mat.name != 'Dots Stroke':
                print('Removing material {}'.format(mat.name))
                bpy.data.materials.remove(mat)
    if len(bpy.data.meshes) > 0:
        for mesh in bpy.data.meshes:
            print('Removing object {}'.format(mesh.name))
            bpy.data.meshes.remove(mesh)

    purge_orphans()


def export_usd(filepath, root_prim):
    bpy.ops.wm.usd_export(filepath=filepath, root_prim_path=root_prim)

#!/usr/bin/env python3

import argparse
import bpy
import os
import sys

import importlib.util

path = '/app/scripts/__init__.py'
name = 'scripts'
spec = importlib.util.spec_from_file_location(name, path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

import scripts.utils as apputils  # NOQA


FORMATS = ('glb')


def search_input_models(folder):
    files = os.listdir(folder)
    if len(files) == 0:
        print(f'Input folder is empty')
        exit(1)

    models = list(filter(lambda x: apputils.get_file_ext(x) in FORMATS, files))
    if len(models) == 0:
        print('Input folder has no 3D models')
        exit(0)

    return models


def parse_arguments():
    argv = sys.argv
    argv = [] if '--' not in argv else argv[argv.index('--') + 1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_arguments()
    input_folder = args.input

    apputils.clear_scene()

    input_models = search_input_models(input_folder)
    print(f'Found {len(input_models)} 3D models: {input_models}')

    for model in input_models:
        print(f'Processing model: {model}')
        model_type = apputils.get_file_ext(model)
        print(f'Model type: {model_type.upper()}')

        apputils.import_glb(os.path.join(input_folder, model))

        usdz_name = model.replace(model_type, 'usdz')
        usdz_path = os.path.join(input_folder, usdz_name)
        apputils.export_usd(usdz_path, '/root')

        apputils.clear_scene()

    print('All models exported')

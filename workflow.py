from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun

funcs = {}

# init functions is used to configure function resources and local settings
def init_functions(functions: dict, project=None, secrets=None):
    for f in functions.values():
        f.apply(auto_mount())



def kfpipeline():
    
    
    # run the ingestion function with the new image and params
    builder = funcs['data_fetch'].deploy_step(skip_deployed=True)
    job = funcs['data_fetch'].as_step(image=builder.outputs['image'],outputs=['df'])
    serving = funcs['serving'].deploy_step()

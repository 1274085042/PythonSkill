import sys
from importlib import import_module

submodules = [
    "experimental",
]

# Redirect imports
for submodule in submodules:
    # pdb.set_trace()
    full_module_name = f"pytorch.distributed.tensor.{submodule}"
    sys.modules[f"pytorch.distributed._tensor.{submodule}"] = import_module(
        full_module_name
    )


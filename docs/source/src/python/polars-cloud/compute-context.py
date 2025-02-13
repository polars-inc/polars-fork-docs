# --8<-- [start:compute]
import polars_cloud as pc

ctx = pc.ComputeContext()
# --8<-- [end:compute]

# --8<-- [start:default-compute]

ctx = pc.ComputeContext(workspace="your-workspace", labels="example")
# --8<-- [end:default-compute]


# --8<-- [start:defined-compute]
ctx = pc.ComputeContext(workspace="your-workspace", 
    cpu=8, 
    memory=20, 
    labels="example")
# --8<-- [end:defined-compute]

# --8<-- [start:set-compute]
ctx = pc.ComputeContext(
    workspace="your-workspace", 
    instance_type="t2.medium", 
    labels="example"
)
# --8<-- [end:set-compute]

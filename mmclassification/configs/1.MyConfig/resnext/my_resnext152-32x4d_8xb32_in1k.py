_base_ = [
    '../../_base_/models/resnext152_32x4d.py',
    '../datasets/custom.py',
    '../schedules/AdamW.py', 
    #'/opt/ml/input/Project/mmclassification/configs/_base_/schedules/cub_bs64.py',
    
    '../default_runtime.py'
]

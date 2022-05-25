_base_ = [
    '../../_base_/models/convnext/convnext-xlarge.py',
    '../datasets/custom.py',
    '../schedules/AdamW.py', '../default_runtime.py'
]



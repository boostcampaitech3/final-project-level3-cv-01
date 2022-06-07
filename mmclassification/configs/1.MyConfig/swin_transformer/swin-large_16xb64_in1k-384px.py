# Only for evaluation
_base_ = [
    '../../_base_/models/swin_transformer/large_384.py',
    '../datasets/custom.py',
    '/opt/ml/input/Project/mmclassification/configs/_base_/schedules/cub_bs64.py', '../default_runtime.py'
]

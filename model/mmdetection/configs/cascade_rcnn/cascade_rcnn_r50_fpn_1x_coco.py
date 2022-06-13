_base_ = [
    '../_base_/models/cascade_rcnn_r50_fpn.py',
    '/opt/ml/input/Project/mmdetection/configs/1.Myconfig/datasets/custom.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

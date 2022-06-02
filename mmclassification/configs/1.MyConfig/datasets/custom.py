dataset_type = 'CustomDataset'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)



albu_train_transforms = [
     dict(type="RandomRotate90", p=1),
    dict(
        type="OneOf",
        transforms=[
            dict(type="HueSaturationValue", hue_shift_limit=10, sat_shift_limit=35, val_shift_limit=25),
            dict(type="RandomGamma"),
            dict(type="CLAHE"),
        ],
        p=0.5,
    ),
    dict(
        type="OneOf",
         transforms=[
            dict(type="RandomBrightnessContrast", brightness_limit=0.25, contrast_limit=0.25),
            
        ],
        p=0.5,
    ),
    dict(
        type="OneOf",
        transforms=[
            
            dict(type="GaussNoise"),
            dict(type="ImageCompression", quality_lower=75),
        ],
        p=0.3,
    ),
   
    
   
]



train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', size=512),
      dict(
        type='Albu',
        transforms=albu_train_transforms,
        keymap={
            'img': 'image',
        },
        update_pad_shape=False,),
    dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]



test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', size=512),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
    
]

data = dict(
    samples_per_gpu=16,
    workers_per_gpu=4,
    train=dict(

        type = 'ClassBalancedDataset',
        oversample_thr = 1e-3,
        dataset = dict(
        type=dataset_type,
        data_prefix='/opt/ml/input/Project/data/Training/image',
        ann_file='/opt/ml/input/Project/data/Training/train_3label.csv',
        pipeline=train_pipeline)

    ),
    val=dict(
        type=dataset_type,
        data_prefix='/opt/ml/input/Project/data/Validation/image',
        ann_file='/opt/ml/input/Project/data/Validation/validation_3label.csv',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_prefix='/opt/ml/input/Project/data/Test/',
        #ann_file='/opt/ml/input/Project/data/Test/inference.csv',
        pipeline=test_pipeline))

#evaluation = dict(interval=1, metric='accuracy',save_best = 'auto')
evaluation = dict(interval=1, metric='accuracy',save_best='accuracy_top-1')

#', save_best='accuracy_top-1'
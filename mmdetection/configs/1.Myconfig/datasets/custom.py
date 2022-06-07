dataset_type = 'CocoDataset'
CLASSES = ('Normal', 'xylostella','white butterfly', 'striolata', 'Pentatomidae')
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

albu_train_transforms2 = [
    dict(type='Resize',height=512,width=512,p=1),
    dict(type="RandomRotate90", p=1),
     
   
]



train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Pad', size_divisor=32),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]



test_pipeline = [
    dict(type='LoadImageFromFile'),
    #dict(type='Resize', img_scale=(512, 512), keep_ratio=True),
    dict(type='Pad', size_divisor=32),
    dict(
        type='MultiScaleFlipAug',
        img_scale=[(512, 512)],
        flip=True,
        flip_direction=["horizontal", "vertical"],
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

val_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(
        type="MultiScaleFlipAug",
        img_scale=[(512, 512)],
        flip=False,
        transforms=[
            dict(type="Resize", keep_ratio=True),
            dict(type="RandomFlip"),
            dict(type="Normalize", **img_norm_cfg),
            dict(type="Pad", size_divisor=32),
            dict(type="ImageToTensor", keys=["img"]),
            dict(type="Collect", keys=["img"]),
        ]
    ),
]


data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        classes = CLASSES,
        ann_file='/opt/ml/input/Project/bug_data/Training/train_coco_annotations.json',
        img_prefix='/opt/ml/input/Project/bug_data/Training/image/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        classes = CLASSES,
        ann_file='/opt/ml/input/Project/bug_data/Validation/val_coco_annotations.json',
        img_prefix='/opt/ml/input/Project/bug_data/Validation/image/',
        pipeline=val_pipeline),
    test=dict(
        type=dataset_type,
        classes = CLASSES,
        ann_file='/opt/ml/input/Project/bug_data/Test/annotations/result.json',
        img_prefix='/opt/ml/input/Project/bug_data/Test/image/',
        pipeline=val_pipeline))
checkpoint_config = dict(max_keep_ckpts=3, interval=1)
evaluation = dict(interval=1, metric='bbox',classwise=True,save_best = 'bbox_mAP')

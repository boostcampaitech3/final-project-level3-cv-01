model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='ResNeXt',
        depth=152,
        num_stages=4,
        out_indices=(3, ),
        groups=32,
        width_per_group=4,
        style='pytorch'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=7,
        in_channels=2048,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5)))
dataset_type = 'CustomDataset'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
albu_train_transforms = [
    dict(type='RandomRotate90', p=1),
    dict(
        type='OneOf',
        transforms=[
            dict(
                type='HueSaturationValue',
                hue_shift_limit=10,
                sat_shift_limit=35,
                val_shift_limit=25),
            dict(type='RandomGamma'),
            dict(type='CLAHE')
        ],
        p=0.5),
    dict(
        type='OneOf',
        transforms=[
            dict(
                type='RandomBrightnessContrast',
                brightness_limit=0.25,
                contrast_limit=0.25)
        ],
        p=0.5),
    dict(
        type='OneOf',
        transforms=[
            dict(type='GaussNoise'),
            dict(type='ImageCompression', quality_lower=75)
        ],
        p=0.3)
]
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', size=512),
    dict(
        type='Albu',
        transforms=[
            dict(type='RandomRotate90', p=1),
            dict(
                type='OneOf',
                transforms=[
                    dict(
                        type='HueSaturationValue',
                        hue_shift_limit=10,
                        sat_shift_limit=35,
                        val_shift_limit=25),
                    dict(type='RandomGamma'),
                    dict(type='CLAHE')
                ],
                p=0.5),
            dict(
                type='OneOf',
                transforms=[
                    dict(
                        type='RandomBrightnessContrast',
                        brightness_limit=0.25,
                        contrast_limit=0.25)
                ],
                p=0.5),
            dict(
                type='OneOf',
                transforms=[
                    dict(type='GaussNoise'),
                    dict(type='ImageCompression', quality_lower=75)
                ],
                p=0.3)
        ],
        keymap=dict(img='image'),
        update_pad_shape=False),
    dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    dict(
        type='Normalize',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        to_rgb=True),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', size=512),
    dict(
        type='Normalize',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        to_rgb=True),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
]
data = dict(
    samples_per_gpu=16,
    workers_per_gpu=4,
    train=dict(
        type='ClassBalancedDataset',
        oversample_thr=0.001,
        dataset=dict(
            type='CustomDataset',
            data_prefix='/opt/ml/input/Project/data/Training/image',
            ann_file='/opt/ml/input/Project/data/Training/train.csv',
            pipeline=[
                dict(type='LoadImageFromFile'),
                dict(type='Resize', size=512),
                dict(
                    type='Albu',
                    transforms=[
                        dict(type='RandomRotate90', p=1),
                        dict(
                            type='OneOf',
                            transforms=[
                                dict(
                                    type='HueSaturationValue',
                                    hue_shift_limit=10,
                                    sat_shift_limit=35,
                                    val_shift_limit=25),
                                dict(type='RandomGamma'),
                                dict(type='CLAHE')
                            ],
                            p=0.5),
                        dict(
                            type='OneOf',
                            transforms=[
                                dict(
                                    type='RandomBrightnessContrast',
                                    brightness_limit=0.25,
                                    contrast_limit=0.25)
                            ],
                            p=0.5),
                        dict(
                            type='OneOf',
                            transforms=[
                                dict(type='GaussNoise'),
                                dict(
                                    type='ImageCompression', quality_lower=75)
                            ],
                            p=0.3)
                    ],
                    keymap=dict(img='image'),
                    update_pad_shape=False),
                dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
                dict(
                    type='Normalize',
                    mean=[123.675, 116.28, 103.53],
                    std=[58.395, 57.12, 57.375],
                    to_rgb=True),
                dict(type='ImageToTensor', keys=['img']),
                dict(type='ToTensor', keys=['gt_label']),
                dict(type='Collect', keys=['img', 'gt_label'])
            ])),
    val=dict(
        type='CustomDataset',
        data_prefix='/opt/ml/input/Project/data/Validation/image',
        ann_file='/opt/ml/input/Project/data/Validation/validation.csv',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(type='Resize', size=512),
            dict(
                type='Normalize',
                mean=[123.675, 116.28, 103.53],
                std=[58.395, 57.12, 57.375],
                to_rgb=True),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img'])
        ]),
    test=dict(
        type='CustomDataset',
        data_prefix='/opt/ml/input/Project/data/Validation/image',
        ann_file='/opt/ml/input/Project/data/Validation/validation.csv',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(type='Resize', size=512),
            dict(
                type='Normalize',
                mean=[123.675, 116.28, 103.53],
                std=[58.395, 57.12, 57.375],
                to_rgb=True),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img'])
        ]))
evaluation = dict(interval=1, metric='accuracy', save_best='accuracy_top-1')
optimizer = dict(type='AdamW', lr=0.005, weight_decay=0.0005)
optimizer_config = dict(grad_clip=None)
lr_config = dict(
    policy='CosineAnnealing',
    min_lr=0.0001,
    warmup='linear',
    warmup_iters=10,
    warmup_ratio=1e-05)
runner = dict(type='EpochBasedRunner', max_epochs=100)
checkpoint_config = dict(interval=3)
log_config = dict(
    interval=100,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(
            type='WandbLoggerHook',
            interval=1000,
            init_kwargs=dict(
                project='cabbage_classify',
                entity='cv_01-2',
                name='resnext152_augmented'))
    ])
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1), ('val', 1)]
work_dir = './work_dirs/my_resnext152-32x4d_8xb32_in1k'
gpu_ids = [0]

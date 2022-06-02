# checkpoint saving
checkpoint_config = dict(interval=3)
# yapf:disable
log_config = dict(
    interval=100,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='WandbLoggerHook',interval=1000,
            init_kwargs=dict(
                project='cabbage_classify',
                entity = 'cv_01-2',
                name = 'resnext152_augmented_3label'
             )     ),
    ])
# yapf:enable



dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1),('val',1)]

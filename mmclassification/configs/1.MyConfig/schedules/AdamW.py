# optimizer
# In ClassyVision, the lr is set to 0.003 for bs4096.
# In this implementation(bs2048), lr = 0.003 / 4096 * (32bs * 64gpus) = 0.0015
optimizer = dict(type='AdamW', lr=0.005, weight_decay=0.0005)
optimizer_config = dict(grad_clip=None)


# learning policy
lr_config = dict(
    policy='CosineAnnealing',
    min_lr=0.0001,
    warmup='linear',
    warmup_iters=10,
    warmup_ratio=1e-5)
runner = dict(type='EpochBasedRunner', max_epochs=100)

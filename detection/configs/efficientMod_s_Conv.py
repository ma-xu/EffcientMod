_base_ = [
    '_base_/models/mask_rcnn_r50_fpn.py',
    '_base_/datasets/coco_instance.py',
    '_base_/schedules/schedule_1x.py',
    '_base_/default_runtime.py'
]
# optimizer
model = dict(
    backbone=dict(
        type='efficientMod_s_Conv',
        style='pytorch',
        init_cfg=dict(
            type='Pretrained', 
            checkpoint=\
                '{path-to-checkpoint}',
            ),
        ),
    neck=dict(
        type='FPN',
        in_channels=[40,80,160,344],
        out_channels=256,
        num_outs=5))
# optimizer
optimizer = dict(_delete_=True, type='AdamW', lr=0.0002, weight_decay=0.05)
optimizer_config = dict(grad_clip=None)


# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g1ArkFQkfD9b8I7DwF5SO8B2U_emdvTD
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5  # clone
# %cd /content/yolov5
# %pip install -qr requirements.txt  # install

import torch
import utils
display = utils.notebook_init()  # checks

!python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images
# display.Image(filename='runs/detect/exp/zidane.jpg', width=600)

# Commented out IPython magic to ensure Python compatibility.
#   %pip install -q wandb
  import wandb; wandb.login()

# Train YOLOv5s on COCO128 for 3 epochs
!python train.py --img 416 --epochs 1000 --data huge.yaml --weights yolov5s.pt

!python detect.py --weights /content/yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source test/

'''names:
  0: Thicc Bubba
  1: Baerat
  2: Deadbatter
  3: Deadbeat
  4: Disgruntled Employee
  5: Fubuzilla
  6: Hooman
  7: Hungry Takodachi
  8: KFP Employee
  9: Kronie Lad
  10: Light IRyStocrat
  11: Night IRyStocrat
  12: Overgrown Sapling
  13: Q Deadbeat
  14: Q Shrimp
  15: Sanallite
  16: Sapling
  17: Shrimp
  18: Smol Ame
  19: Takodachi
  names:
  0: shimp
  1: booba
  2: chicken
  3: cro ame
  4: deatbeat
  5: fubu black
  6: fubu white
  7: tako
  /content/drive/MyDrive/test ii
  /content/drive/MyDrive/test iii
  /content/drive/MyDrive/test iv
  /content/drive/MyDrive/holocure'''

''' all         81       1195      0.993      0.983      0.991      0.881
                 shimp         81         79      0.997          1      0.995      0.919
                 booba         81         72      0.986      0.975      0.993      0.861
               chicken         81        125      0.995          1      0.995      0.908
               cro ame         81        273      0.995      0.967      0.982       0.84
              deatbeat         81         64          1      0.981      0.985      0.856
            fubu black         81         75      0.987      0.985      0.993      0.887
            fubu white         81        264      0.992      0.985      0.995      0.893
                  tako         81        243      0.992      0.975      0.992      0.886
Results saved to runs/train/exp
wandb: Waiting for W&B process to finish... (success).
wandb:                                                                                
wandb: 
wandb: Run history:
wandb:      metrics/mAP_0.5 ▁▃▄▅▇▆▇▇████████████████████████████████
wandb: metrics/mAP_0.5:0.95 ▁▂▃▄▅▄▆▅▆▆▆▇▇▇▇▇▇▇▇▇▇████▇██████████████
wandb:    metrics/precision ▁▆▆▆▅▄▇▇▇███████████████████████████████
wandb:       metrics/recall ▁▂▄▅▆▇▇▇▇███████████████████████████████
wandb:       train/box_loss █▆▄▄▄▃▃▃▃▃▃▂▃▂▂▂▂▃▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       train/cls_loss █▆▄▃▃▃▂▃▃▂▂▂▂▁▂▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       train/obj_loss █▇▆▇▆▄▃▃▂▄▆▄▆▃▂▅▄▄▃▃▄▂▂▂▂▃▃▃▂▁▁▂▂▁▃▁▁▁▁▁
wandb:         val/box_loss █▆▄▄▃▃▂▃▃▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:         val/cls_loss █▅▄▃▃▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:         val/obj_loss ██▄▄▄▄▃▃▃▃▃▂▂▂▂▂▂▂▂▂▂▂▂▂▁▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁
wandb:                x/lr0 █▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:                x/lr1 ▄███▇▇▇▇▇▇▆▆▆▆▆▅▅▅▅▅▅▄▄▄▄▄▃▃▃▃▃▂▂▂▂▂▂▁▁▁
wandb:                x/lr2 ▄███▇▇▇▇▇▇▆▆▆▆▆▅▅▅▅▅▅▄▄▄▄▄▃▃▃▃▃▂▂▂▂▂▂▁▁▁
wandb: 
wandb: Run summary:
wandb:           best/epoch 966
wandb:         best/mAP_0.5 0.99125
wandb:    best/mAP_0.5:0.95 0.88137
wandb:       best/precision 0.99279
wandb:          best/recall 0.98342
wandb:      metrics/mAP_0.5 0.99125
wandb: metrics/mAP_0.5:0.95 0.88116
wandb:    metrics/precision 0.99283
wandb:       metrics/recall 0.98349
wandb:       train/box_loss 0.01874
wandb:       train/cls_loss 0.00249
wandb:       train/obj_loss 0.03653
wandb:         val/box_loss 0.01707
wandb:         val/cls_loss 0.00184
wandb:         val/obj_loss 0.01925
wandb:                x/lr0 0.00012
wandb:                x/lr1 0.00012
wandb:                x/lr2 0.00012

'''
ลองรันหลายตัว ปรากฎว่าคอมมันพยายามทายรูปครึ่งๆแล้วเอามาเป็นข้อมูลในการแยกหลายตัว
แต่มีข้อผิดผลาดคือมันไม่มีข้อมูลตัวละครพื้นฐานทำให้มันเดาชื่อผิดแต่ความแม่นยำสูงอยู่

Stopping training early as no improvement observed in last 100 epochs. Best results observed at epoch 1098, best model saved as best.pt.
To update EarlyStopping(patience=100) pass a new patience value, i.e. `python train.py --patience 300` or use `--patience 0` to disable EarlyStopping.

1199 epochs completed in 0.440 hours.
Optimizer stripped from runs/train/exp2/weights/last.pt, 14.4MB
Optimizer stripped from runs/train/exp2/weights/best.pt, 14.4MB

Validating runs/train/exp2/weights/best.pt...
Fusing layers... 
Model summary: 213 layers, 7064065 parameters, 0 gradients, 15.9 GFLOPs
                 Class     Images  Instances          P          R     mAP@.5 mAP@.5:.95: 100% 1/1 [00:00<00:00,  4.20it/s]
                   all          6        173      0.567      0.609        0.6      0.326
           Thicc Bubba          6         29       0.45      0.931      0.853      0.319
                Baerat          6         10          1          0      0.132     0.0632
            Deadbatter          6         20      0.404       0.95      0.934      0.481
      Hungry Takodachi          6         30      0.258      0.433      0.262      0.058
          KFP Employee          6          8      0.359      0.625      0.617      0.403
            Kronie Lad          6          5          1      0.463      0.612      0.373
      Light IRyStocrat          6          4          1          0     0.0526     0.0192
               Sapling          6         31      0.331      0.774      0.704      0.375
              Smol Ame          6         12      0.352      0.952      0.887      0.515
             Takodachi          6         24       0.52      0.958      0.941      0.649
Results saved to runs/train/exp2
wandb: Waiting for W&B process to finish... (success).
wandb:                                                                                
wandb: 
wandb: Run history:
wandb:      metrics/mAP_0.5 ▁▁▁▁▁▂▂▂▃▃▃▃▃▃▃▄▄▅▄▅▅▅▅▆▅▆▆▇▇▇▇▇▇▇████▇█
wandb: metrics/mAP_0.5:0.95 ▁▁▁▁▁▁▂▂▂▂▃▃▃▃▂▄▄▄▄▅▄▄▃▅▄▅▅▆▆▆▆▆▆▇████▇█
wandb:    metrics/precision ▁▁▁▁▁▅▁▂▃▄▃▃▄▄▃▄▄▄▃▄▄▅▅▅▅▇▆▇▇▇▇▇▇▇▇▇▅█▆▅
wandb:       metrics/recall ▁▁▁▂▂▂▅▆▅▄▅▅▅▅▅▅▅▅▆▆▅▅▅▆▆▅▅▅▅▅▅▆▆▆▆▆█▅▇█
wandb:       train/box_loss ██▇▇▅▅▄▅▄▅▄▃▃▃▄▃▃▃▃▂▂▃▃▃▂▃▂▂▁▂▂▃▁▁▂▁▂▁▁▂
wandb:       train/cls_loss ██▇▆▆▄▅▆▄▄▄▅▄▃▃▃▄▃▃▃▃▃▃▃▃▃▂▂▂▂▂▂▂▂▁▁▁▂▁▁
wandb:       train/obj_loss ▅█▄▂▅▇▆▃▄▆▄▄▅▄▇▄▂▅▅▄▂▅▄▇▆▄▆▃▂▅▃▇▁▂▅▇▃▄▃▃
wandb:         val/box_loss ██▇▇▅▄▄▄▄▃▃▃▃▃▄▂▂▂▂▂▃▂▂▂▂▂▁▁▁▂▁▁▁▁▁▁▂▁▁▁
wandb:         val/cls_loss ██▇▆▅▅▅▄▄▄▄▄▃▃▃▃▃▃▃▃▃▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁
wandb:         val/obj_loss ▄▅▂▂▄█▅▄▄▄▄▄▄▄▃▃▃▃▃▃▄▃▃▂▂▂▃▂▂▁▂▂▂▂▁▁▁▁▁▁
wandb:                x/lr0 █▇▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:                x/lr1 ▁▂▅███████████▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▆▆▆▆▆▆
wandb:                x/lr2 ▁▂▅███████████▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▆▆▆▆▆▆
wandb: 
wandb: Run summary:
wandb:           best/epoch 1098
wandb:         best/mAP_0.5 0.59964
wandb:    best/mAP_0.5:0.95 0.32612
wandb:       best/precision 0.56793
wandb:          best/recall 0.60899
wandb:      metrics/mAP_0.5 0.59961
wandb: metrics/mAP_0.5:0.95 0.32561
wandb:    metrics/precision 0.56745
wandb:       metrics/recall 0.60864
wandb:       train/box_loss 0.03987
wandb:       train/cls_loss 0.01901
wandb:       train/obj_loss 0.05143
wandb:         val/box_loss 0.04122
wandb:         val/cls_loss 0.01684
wandb:         val/obj_loss 0.06052
wandb:                x/lr0 0.00763
wandb:                x/lr1 0.00763
wandb:                x/lr2 0.00763
'''
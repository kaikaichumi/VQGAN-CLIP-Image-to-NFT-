# VQGAN-CLIP-Image-to-NFT-

## 安裝說明
 ```
    git clone 'https://github.com/nerdyrodent/VQGAN-CLIP'
    cd VQGAN-CLIP
    git clone 'https://github.com/openai/CLIP'
    git clone 'https://github.com/CompVis/taming-transformers'
 ```
## 模型下載
  ```
  mkdir checkpoints
  curl -L -o checkpoints/vqgan_imagenet_f16_16384.yaml -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1' #ImageNet 16384
  curl -L -o checkpoints/vqgan_imagenet_f16_16384.ckpt -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1' #ImageNet 16384 
  ```

## RUN
進入UI界面
 ```
    python main_.py
 ```
 ![image](https://user-images.githubusercontent.com/126358442/228769956-a0e4bfbd-3964-4514-b3c2-7260ea52fd2f.png)

##### 影像生成範例
輸入任意文本，例如：
```
a futuristic city in cyberpunk style
 ```
![image](https://user-images.githubusercontent.com/126358442/228774515-eb76b7d7-6dd9-4d5e-bbe5-29f1b5ec2a10.png)

##### 編輯影像範例

按下Select Image選擇一張影像

![origin](https://user-images.githubusercontent.com/126358442/228777666-a54ccb45-edc1-4dd9-8987-9b4e05fcc36c.png)
<br>
輸入文本描述，如：
```
red sky
 ```

實際輸出結果
<br>
![change to red sky](https://user-images.githubusercontent.com/126358442/228777689-1ca08647-8b2d-418b-a2d3-68e21c2cde72.png)



 
 參考來源：https://github.com/nerdyrodent/VQGAN-CLIP
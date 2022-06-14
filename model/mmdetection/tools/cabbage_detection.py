import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import cv2
import argparse
plt.rcParams['axes.grid'] = False
from mmdet.apis import init_detector, inference_detector


parser = argparse.ArgumentParser()
parser.add_argument('img',help='inference image path')
parser.add_argument('config',help='inference config file path')
parser.add_argument('checkpoint',help='checkpoint file path')
parser.add_argument('save_dir',help='save result directory path')
args = parser.parse_args()


model = init_detector(args.config,args.checkpoint,device='cuda:0')

img = cv2.imread(args.img)
img_arr = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

labels_to_names_seq = {0:'Cabbage' }
labels_to_names = {0:'Cabbage' }

bbox_list = []
# model과 원본 이미지 array, filtering할 기준 class confidence score를 인자로 가지는 inference 시각화용 함수 생성. 
def get_detected_img(model, img_array,  score_threshold=0.3, is_print=True):
  # 인자로 들어온 image_array를 복사. 
  draw_img = img_array.copy()
  bbox_color=(0, 255, 0)
  text_color=(0, 0, 255)

  # model과 image array를 입력 인자로 inference detection 수행하고 결과를 results로 받음. 
  # results는 80개의 2차원 array(shape=(오브젝트갯수, 5))를 가지는 list. 
  results = inference_detector(model, img_array)

  # 80개의 array원소를 가지는 results 리스트를 loop를 돌면서 개별 2차원 array들을 추출하고 이를 기반으로 이미지 시각화 
  # results 리스트의 위치 index가 바로 COCO 매핑된 Class id. 여기서는 result_ind가 class id
  # 개별 2차원 array에 오브젝트별 좌표와 class confidence score 값을 가짐. 
  for result_ind, result in enumerate(results):
    # 개별 2차원 array의 row size가 0 이면 해당 Class id로 값이 없으므로 다음 loop로 진행. 
    if len(result) == 0:
      continue
    
    # 2차원 array에서 5번째 컬럼에 해당하는 값이 score threshold이며 이 값이 함수 인자로 들어온 score_threshold 보다 낮은 경우는 제외. 
    result_filtered = result[np.where(result[:, 4] > score_threshold)]
    
    
    # 해당 클래스 별로 Detect된 여러개의 오브젝트 정보가 2차원 array에 담겨 있으며, 이 2차원 array를 row수만큼 iteration해서 개별 오브젝트의 좌표값 추출. 
    for i in range(len(result_filtered)):
      # 좌상단, 우하단 좌표 추출. 
      left = int(result_filtered[i, 0])
      top = int(result_filtered[i, 1])
      right = int(result_filtered[i, 2])
      bottom = int(result_filtered[i, 3])
      print("left : ",left)
      print("top : ",top)
      print("right : ",right)
      print("bottom : ",bottom)
      #if (right-left)>550 or (bottom-top)>550:
      #  continue
      bbox = {"left" : left,"top" : top, "right" : right, "bottom" : bottom}
      bbox_list.append(bbox)
      caption = "{}: {:.4f}".format(labels_to_names_seq[result_ind], result_filtered[i, 4])
      cv2.rectangle(draw_img, (left, top), (right, bottom), color=bbox_color, thickness=2)
      cv2.putText(draw_img, caption, (int(left), int(top - 7)), cv2.FONT_HERSHEY_SIMPLEX, 0.37, text_color, 1)
      if is_print:
        print(caption)

  return draw_img


img_arr = img
detected_img = get_detected_img(model, img_arr,  score_threshold=0.3, is_print=True)
detected_img = cv2.cvtColor(detected_img, cv2.COLOR_BGR2RGB)

def im_trim(img, x, y, w, h):
    imgtrim = img[y: y + h, x: x + w]
    return imgtrim

id = 1
for box in bbox_list:
  croppedImage = im_trim(img,box["left"],box["top"],abs(box["top"]-box["bottom"]),abs(box["right"]-box["left"]))
  fn = args.save_dir + "/cropped_"+str(id)+".png"
  cv2.imwrite(fn, croppedImage)
  id +=1

print("finish")



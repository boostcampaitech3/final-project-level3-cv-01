from tqdm import tqdm
import os
import cv2

src_path = '/opt/ml/input/Project/bug_data/Training/a' # 원본 이미지 폴더 경로
dst_path = '/opt/ml/input/Project/bug_data/Training/a' # 저장될 폴더 경로

os.makedirs(dst_path, exist_ok=True)


files = os.listdir(src_path)




for file_name in tqdm(files):
    path = os.path.join(src_path,file_name)
    image = cv2.imread(path)
    image = cv2.resize(image, (512,512),interpolation=cv2.INTER_AREA) # Down Scaling 시, 영역보간법이 우수
    cv2.imwrite(os.path.join(dst_path,file_name), image)


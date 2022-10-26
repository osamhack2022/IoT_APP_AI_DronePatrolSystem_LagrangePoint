## darknet git clone
git clone https://github.com/pjreddie/darknet  
or  
git clone https://github.com/AlexeyAB/darknet

## yolov3-tiny weights
wget https://pjreddie.com/media/files/yolov3-tiny.weights

## 라즈베리파이 카메라모듈과 openCV 연동
$ vcgencmd get_camera  
명령어 입력했을 때 supported=1, detected=1 로 둘다 1이 나와야 한다  
나왔다면  

$ sudo modprobe bcm2835-v4l2  
로 modprobe 명령을 이용해서 커널에 bcm2835-v4l2를 로드

## yolov3-tiny Custom Data 사용
**yolov3-tiny trained-weights**  
* epoch 2000
https://drive.google.com/file/d/153SYYBUwF_UHLEMb-U8y61kxWhpdK1mF/view?usp=sharing
* epoch 4000
  https://drive.google.com/file/d/1yN9uWMnToKpMPoT6UgvUBZKpnWND-R1e/view?usp=sharing

## Detection 방법
* /custom/classes.names, /custom/lagrange_yolov3-tiny.cfg, trained weight 파일 필요
* /codes/trained_camera_detection.ipynb 코드에서 위의 세 파일 경로 재지정 후 실행

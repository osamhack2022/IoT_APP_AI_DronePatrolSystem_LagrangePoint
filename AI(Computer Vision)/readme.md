## darknet git clone
git clone https://github.com/pjreddie/darknet

## yolov3-tiny weights
wget https://pjreddie.com/media/files/yolov3-tiny.weights

## 라즈베리파이 카메라모듈과 openCV 연동
$ vcgencmd get_camera  
명령어 입력했을 때 supported=1, detected=1 로 둘다 1이 나와야 한다  
나왔다면  

$ sudo modprobe bcm2835-v4l2  
로 modprobe 명령을 이용해서 커널에 bcm2835-v4l2를 로드

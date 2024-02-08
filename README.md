# Smart-Light-Application-Project (Light-Is-Right Project)
![제목 없는 동영상 - Clipchamp로 제작](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/bb09cbc1-5f28-446b-894d-4335b9bd114f)

"Light-Is-Right" 프로젝트는 Python으로 개발된 소프트웨어와 Raspberry Pi를 활용하여 LED Strip을 제어하는 스마트 조명 시스템입니다. </br>
 이 프로젝트는 코로나19사태로 인해 실내에서 생활하는 시간이 길어지며 ‘코로나 블루’라는 심리적 불안증을 겪고 있는 현대인들을 위해 개발했습니다.</br>
 스마트 감성조명을 이용해 심리적 불안증 치유에 도움이 될 수 있도록 라이트 테라피 제품을 조사, 분석하여 조명을 이용해 어떤 방식으로 심리치유에 도움을 주는지 참고하였고,
기존 스마트 조명 제품들을 조사, 분석하여 사용자가 편리하게 사용할 수 있는 기능들을 벤치마킹하여 개발했습니다.  

<h3> 아래의 프로젝트들을 참고하여 개발했습니다.</h3>

> [Dancy Pi: Audio Reactive LEDs](https://github.com/naztronaut/dancyPi-audio-reactive-led) <br/>
> [Music-Genre-Classification-GTZAN](https://github.com/chittalpatel/Music-Genre-Classification-GTZAN)

# 개발 기간
2020.02 ~ 2020.9 (8개월)

# 기능
제공하는 기능은 다음과 같습니다
1. 사용자 감성 유도 조명 기능
2. 사용자 색 선택 기능
3. 색 온도 조절 기능
4. 음악에 어울리는 조명 기능
5. 장면에 따른 조명 표현 기능
6. WIFI Socket 통신 방식을 통한 조명 무선제어

# 개발 환경
- Python 3
- Raspberry pi 4B
- Anacond - Jupyter Notebook


# 사용 기술

## 조명 제어 Application
- PySide2 (조명 제어를 위한 GUI 제작)
- pyaudio (실시간 오디오 데이터 인식)
- Numpy (수치 계산 및 행렬 연산)
- Librosa (오디오 raw 데이터 분석)
- Threading (음악 장르 분류 및 오디오 데이터 인식 병렬처리)
- Opencv2 (장면 이미지 컬러 히스토그램 분석)
- socket (Raspberry Pi <-> Application 간 WiFi Socket 통신)


## MusicCalssification Model (Convolution Neural Network Model)
- Tensorflow, Keras (음악 장르 분류를 위한 CNN모델 학습)
- Tkinter (음악 장르 분류 시각화)
- Librosa (오디오 raw 데이터 분석)
- Numpy, Pandas, Matplotlib (행렬 연산 및 데이터 전처리, 시각화) 

### Train Music DataSet
> [GTZAN Dataset](http://opihi.cs.uvic.ca/sound/genres.tar.gz)</br>

원본 데이터는 총 1.2GB 크기로, 10개의 장르 폴더에 균등하게 나눠진 1000개의 오디오 파일(.au)로 구성되어 있습니다. 즉, 각 장르마다 100개의 오디오 파일이 있습니다.

## Raspberry Pi 4B
- rpi_ws281x & neopixel (네오픽셀 제어 라이브러리)
- scipy (gaussian_filter1d 활용 데이터를 필터링을 통한 조명 움직임 구현 등 디지털 신호 처리용)
- Numpy (행렬 연산)
- socket (Raspberry Pi <-> Application 간 WiFi Socket 통신)

### Raspberry Pi 회로도

![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/cd10e8df-c2d9-4b2a-852e-c24302d54ac0)

### Raspberry Pi 및 하드웨어 구성 

![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/c4889f3b-c48b-4a72-84f4-17a4167cfd11)|![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/de081321-295d-48e0-bba5-7bc1017b8f2e)|![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/b9fad70c-008e-4cd4-a5a6-1f3843324afa)
|------|---|---|
|Raspberry pi 4B|neopixel WS2812B|SMPS|

# 동작 구조
![졸작 구조](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/4aaaa1a3-e383-4b9e-999a-58638efac6e1)

# 기능 흐름

![졸작 플로우](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/90aa5cd8-1998-498e-a694-c41e9c55b092)


# 기능 시연 

시연 영상은 링크를 클릭하세요
[시연 영상 링크](https://youtu.be/8p6gbbaSfeg)

# GUI

![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/a20dcd07-e7ac-4a98-ab40-233c49edf82e)

# 사용자 감성 유도 조명 기능

- 색채나 조명 색에 따른 감성반응에 관한 연구 자료 8건을 조사, 분석한 결과로 각 색상별 가장 많은 빈도수를 나타낸 감성 키워드를 바탕으로 프리셋 제공

![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/3162edd0-81e0-4f76-ba26-615a06a91c17)


![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/40445472-2a2f-4a4f-aa7d-e6f068f44790)


# 사용자 색 선택 기능
![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/921e8f1d-9966-421a-a437-f6daa06fb63a)

# 색 온도 조절 기능

![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/2fbccc03-998c-46cb-8745-100e9edc1a8f)


# 음악에 어울리는 조명 기능

- 음악 장르 분류 모델(CNN)을 통해 음악 장르 분류 
![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/a7a59e81-514f-49ae-a192-85e41eb47748)

- 분류된 장르에 따라 음악에 어울리는 조명 색상 & 움직임 제공
![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/33dd3ffc-509a-483f-a721-2ac4fc95d391)

# 장면에 따른 조명 표현 기능

- Opencv2 라이브러리를 활용하여 장면 이미지의 컬러 히스토그램을 분석하여 장면 프리셋 제공

![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/21260348-81ac-451b-b176-3cf2e4ddb59a)


![image](https://github.com/XgitalBounce/Smart-Light-Application-Project/assets/60294084/8f8fb482-24d7-4d88-a94c-ffe31882514f)


# 향후 개선안 

- 모듈화하여 가독성을 높이고 유지보수를 용이하게 해야 함
(현재 코드는 모듈화되어있지 않고, 하나의 파일에 대부분의 기능이 집약된 상태로 가독성이 매우 낮고 유지보수가 매우 어려운 상태)
- 자동 네트워크 설정 기능 추가: 현재는 Raspberry Pi(Server)와 Python Application(Client) 간의 IP와 Port를 수동으로 설정해야 하는 번거로움이 있는데, 이를 개선하기 위해 사용 중인 Wi-Fi를 자동으로 인식하고 IP와 Port를 자동으로 배정하는 기능을 추가해야 합.
 이렇게 하면 사용자가 별도로 네트워크 설정을 할 필요 없이 더 편리하게 시스템을 사용할 수 있음 
- 현재 장면에 따른 조명 표현 기능을 고도화시켜 동영상의 움직임에 따라 조명을 표현하는 기능 개발

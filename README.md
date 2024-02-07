# Smart-Light-Application-Project (Light-Is-Right Project)

"Light-Is-Right" 프로젝트는 Python으로 개발된 소프트웨어와 Raspberry Pi를 활용하여 LED Strip을 제어하는 스마트 조명 시스템입니다. </br>
 이 프로젝트는 코로나19사태로 인해 실내에서 생활하는 시간이 길어지며 ‘코로나 블루’라는 심리적 불안증을 겪고 있는 현대인들을 위해 개발했습니다.</br>
 스마트 감성조명을 이용해 심리적 불안증 치유에 도움이 될 수 있도록 라이트 테라피 제품을 조사, 분석하여 조명을 이용해 어떤 방식으로 심리치유에 도움을 주는지 참고하였고,
기존 스마트 조명 제품들을 조사, 분석하여 사용자가 편리하게 사용할 수 있는 기능들을 벤치마킹하여 개발했습니다.  

<h3> 기존의 프로젝트를 참고합니다.</h3>

> [Dancy Pi: Audio Reactive LEDs](https://github.com/naztronaut/dancyPi-audio-reactive-led) <br/>
> [Music-Genre-Classification-GTZAN](https://github.com/chittalpatel/Music-Genre-Classification-GTZAN)

# 개발 기간
2020.02 ~ 2020.9 (8개월)

# 기능
제공하는 기능은 다음과 같습니다
1. 사용자 감성 유도 조명 기능
2. 색 온도에 따른 조명 표현 기능
3. 음악에 어울리는 조명 기능
4. 장면에 따른 조명 표현 기능
5. WIFI Socket 통신 방식을 통한 조명 무선제어

# 개발 환경
- Python 3
- Raspberry Pi
- Anacond - Jupyter Notebook

# 사용 기술

## 조명 제어 Application
- PySide2
- pyaudio
- socket
- Librosa
- Threading
- Numpy

## MusicCalssification Model (Convolution Neural Network Model)
- Tensorflow
- Keras
- Scikit-Learn
- Tkinter
- Librosa
- Numpy, Pandas, Matplotlib

### Train Music DataSet
> [GTZAN Dataset](http://opihi.cs.uvic.ca/sound/genres.tar.gz)</br>

원본 데이터는 총 1.2GB 크기로, 10개의 장르 폴더에 균등하게 나눠진 1000개의 오디오 파일(.au)로 구성되어 있습니다. 즉, 각 장르마다 100개의 오디오 파일이 있습니다.

## RaspBerry Pi
- rpi_ws281x & neopixel
- socket
- scipy
- numpy






Python Raspberry Pi3에서 동작합니다. 

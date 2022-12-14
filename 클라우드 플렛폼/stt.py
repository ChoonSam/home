from ast import expr_context
from numpy import record
import speech_recognition as sr
from sympy import re

#마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
   print('듣고 있어요')
   audio = r.listen(source) # 마이크로부터 음성 듣기

# 파일로부터 음성 듣기 (wav, aiff/aiff-c, flac 가능 mps 는 불가)
#r = sr.Recognizer()
#with sr.AudioFile() as source:
#    print('듣고 있어요')
#    audio = r.record(source)

try:
    # 구글 API로 인식 (하루 50회)
    # 영어 문장
    text = r.recognize_google(audio, language='en-US')
    print(text)

    # 한글 문장
    #text = r.recognize_google(audio, language='ko')
    #print(text)

except sr.UnknownValueError:
    print('인식 실패') # 음성 인식 실패한 경우
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API Key 오류, 네트워크 단절 등
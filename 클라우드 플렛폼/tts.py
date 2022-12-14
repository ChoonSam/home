from winsound import PlaySound
from gtts import gTTS
from playsound import playsound

# 영어문장
#text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.?'
file_name = 'sample.mp3'
#tts_en = gTTS(text=text, lang='en')
#tts_en.save(file_name)

# 한글 문장
#text = '저는 기계입니다. 하지만 괜찮아 보이죠?'
#tts_ko = gTTS(text=text, lang = 'ko')
#tts_ko.save(file_name)
#playsound(file_name) # mp3 파일 재생

# 긴 문장 (파일에서 물러와서 처리)
with open('sample.txt' , 'r', encoding = 'utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang = 'ko')
tts_ko.save(file_name)
playsound(file_name) # mp3 파일 재생
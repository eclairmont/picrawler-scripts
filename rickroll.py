from time import sleep
from robot_hat import Music,TTS

music = Music()
tts = TTS()

manual = '''
Input key to call the function!
    q: Play rickroll
    w: Play crabrave
    t: Text to Speech
'''

def main():
    print(manual)

    flag_bgm = False
    music.music_set_volume(20)
    tts.lang("en-US")


    while True:
        key = input()
        if key == "q" or 'Q' == key:
            flag_bgm = not flag_bgm
            if flag_bgm is True:
                music.background_music('./musics/rickroll.mp3')
            else:
                music.music_stop()

        elif key == "w" or 'W' == key:
            flag_bgm = not flag_bgm
            if flag_bgm is True:
                music.background_music('./musics/crabrave.mp3')
            else:
                music.music_stop()
        elif key == "t" or 'T' == key:
            words = "crab crab crab"
            tts.say(words)

        elif key == "t" or 'T' == key:
            words = "crab crab crab"
            tts.say(words)

if __name__ == "__main__":
    main()

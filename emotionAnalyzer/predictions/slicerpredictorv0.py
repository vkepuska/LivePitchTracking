from pydub import AudioSegment
import predictorv0


# needs ffmpeg installed and in path to run correctly!

# sound = AudioSegment.from_mp3("/path/to/file.mp3")
# sound.export("/output/path/file.wav", format="wav")

song = AudioSegment.from_file("testaudio.wav", "wav")

print (len(song))

#trim 10 sec

trim1 =  song[10000:]

print (len(trim1))

x = int(len(trim1)/1000)

print (x)
y = int(x/10)

for i in range (0, y):
    t1 = i*10000
    t2 = t1+10000
    # print(str(t1) + "  " + str(t2))
    audioslice = trim1[t1:t2]
    fname = 'slice' + str(i) + '.wav'
    print (fname)
    audioslice.export(fname, format="wav")
    print('exported')
    audioemotion = predictorv0.predict_emotion(fname)
    print('at timecode ' + str(t1) + " to " + str(t2))

    print('detected emotion is ' + audioemotion)





import time

import pyaudio
import struct
import math

from reuseable.configs import MobileConfig

INITIAL_TAP_THRESHOLD = 0.010
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
# if we get this many noisy blocks in a row, increase the threshold
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME
# if we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME
# if the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 1.5/INPUT_BLOCK_TIME


def get_rms(block):
    # RMS amplitude is defined as the square root of the
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into
    # a string of 16-bit samples...

    # we will get one short out for each
    # two chars in the string.
    count = len(block)/2
    format = "%dh" % count
    shorts = struct.unpack(format, block)

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768.
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt(sum_squares / count)


class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1
        self.quietcount = 0
        self.errorcount = 0

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None
        for i in range(self.pa.get_device_count()):
            devinfo = self.pa.get_device_info_by_index(i)
            print("Device %d: %s" % (i, devinfo["name"]))

            for keyword in ["mic", "input"]:
                if keyword in devinfo["name"].lower():
                    print("Found an input: device %d - %s" % (i, devinfo["name"]))
                    device_index = i
                    return device_index

        if device_index is None:
            print("No preferred input found; using default input device.")

        return device_index

    def open_mic_stream(self):
        device_index = self.find_input_device()

        stream = self.pa.open(format=FORMAT,
                              channels=CHANNELS, rate=RATE, input=True,
                              input_device_index=device_index,
                              frames_per_buffer=INPUT_FRAMES_PER_BLOCK)

        return stream

    # def tapDetected(self):
    #     print("Tap!")

    def listen(self):
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError as e:
            # dammit.
            self.errorcount += 1
            print("(%d) Error recording: %s" % (self.errorcount, e))
            self.noisycount = 1
            return

        amplitude = get_rms(block)
        if amplitude > self.tap_threshold:
            self.sod=time.time()
            # noisy block
            # print("amplitude", amplitude)

            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:
                # turn down the sensitivity
                self.tap_threshold *= 1.1
        else:
            # quiet block.

            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                # print("tap_threshold", self.tap_threshold)
                tup_audio = (self.noisycount,self.sod)
                MobileConfig.audio_det.append(tup_audio)
                # print("amplitude", amplitude)
                print(self.sod)
                # print("MAX_TAP_BLOCKS", MAX_TAP_BLOCKS, "\n"+"noisycount", self.noisycount)
                # self.tapDetected()
                print("Tap!")

            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                # turn up the sensitivity
                self.tap_threshold *= 0.9
tt=TapTester()
def roy():
    c = time.time()
    # for i in range(1000):
    while True:
        cx = time.time()
        if cx > c + 60:
            break
        tt.listen()
        
f=[(0.9688691232528589, 1685610900.3056705), (0.9904701397712834, 1685610905.3537142), (0.9904701397712834, 1685610910.3821192), (0.9904701397712834, 1685610915.410621), (0.4501270648030495, 1685610919.459599), (0.8227445997458703, 1685610924.5019782), (0.8786531130876747, 1685610929.546773), (0.9161372299872934, 1685610934.5796754), (0.9161372299872934, 1685610939.597017), (0.9377382465057179, 1685610944.6246464), (0.9440914866581956, 1685610949.6584687), (0.9968233799237611, 1685610955.72258), (1.0, 1685610957.7438197), (1.0, 1685610960.7674646)]
a= [(20, 1685610900.531064), (20, 1685610905.541294), (19, 1685610910.4907851), (19, 1685610915.5007818), (19, 1685610920.510703), (20, 1685610925.5105107), (20, 1685610930.5207381), (20, 1685610935.5307488), (20, 1685610940.5318558), (19, 1685610945.490798)]
diff = []
y = 0
while y < min(len(a),len(f)):

    if abs(a[y][1] - f[y][1]) < 50:
        diff.append(abs(a[y][1] - f[y][1]))
        y += 1

    elif abs(a[y][1] - f[y+1][1]) < 50:

        diff.append(abs(a[y][1] - f[y+1][1]))
        # except:
        #     diff.append(abs(a[y][1] - f[y+1][1]))
        y += 1
    elif abs(a[y][1] - f[y][1]) > 50:
        if len(diff) > 5:
            break
        else : pass
    else:
        pass
print(diff)
p=0
for _ in range(len(diff)):
        if diff[_] < 5:
            p += diff[_]
print(p / len(diff))
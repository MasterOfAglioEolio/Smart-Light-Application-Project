# python3
from __future__ import print_function
from __future__ import division
from scipy.ndimage.filters import gaussian_filter1d
import led

import socket
import sys
import neopixel
import config
import numpy as np
import dsp
from rpi_ws281x import *
import time
import queue
HOST = '172.30.1.26'  # all available interfaces
PORT = 1428
# 1. open Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# 2. bind to a address and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind Failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
    sys.exit()

print('Socket bind complete')

strip = neopixel.Adafruit_NeoPixel(config.N_PIXELS, config.LED_PIN,
                                   config.LED_FREQ_HZ, config.LED_DMA,
                                   config.LED_INVERT, config.BRIGHTNESS
                                  )
strip.begin()
print('strip begin')

_gamma = np.load(config.GAMMA_TABLE_PATH)
"""Gamma lookup table used for nonlinear brightness correction"""

_prev_pixels = np.tile(253, (3, config.N_PIXELS))
"""Pixel values that were most recently displayed on the LED strip"""

pixels = np.tile(1, (3, config.N_PIXELS))

# 3. Listen for incoming connections
s.listen(10)
print('Socket now listening')
conn, addr = s.accept()
print('Connected')
# keep talking with the client





_time_prev = time.time() * 1000.0
"""The previous time that the frames_per_second() function was called"""

_fps = dsp.ExpFilter(val=config.FPS, alpha_decay=0.2, alpha_rise=0.2)
"""The low-pass filter used to estimate frames-per-second"""

def colorWipe(strip, color):
    """Wipe color across display a pixel at a time."""
    # for i in range(strip.numPixels()):
    #     strip.setPixelColor(i, color)
    #     strip.show()
    for i in range(config.N_PIXELS):
        # Ignore pixels if they haven't changed (saves bandwidth)
        strip._led_data[i] = int(color)
    strip.show()


def scene_colorWipe(strip, color1,color2,color3):
    """Wipe color across display a pixel at a time."""
    division_scene=int(3)
    print("strip:",strip.numPixels()/division_scene)
    for i in range(int(strip.numPixels()/division_scene)):
        strip._led_data[i] = int(color1)

    for i in range(int(strip.numPixels()/division_scene),int(strip.numPixels()*2/division_scene)):
        strip._led_data[i] = int(color2)

    for i in range(int(strip.numPixels()*2/division_scene),int(strip.numPixels()*3/division_scene)):
        strip._led_data[i] = int(color3)
    strip.show()


def frames_per_second():
    """Return the estimated frames per second

    Returns the current estimate for frames-per-second (FPS).
    FPS is estimated by measured the amount of time that has elapsed since
    this function was previously called. The FPS estimate is low-pass filtered
    to reduce noise.

    This function is intended to be called one time for every iteration of
    the program's main loop.

    Returns
    -------
    fps : float
        Estimated frames-per-second. This value is low-pass filtered
        to reduce noise.
    """
    global _time_prev, _fps
    time_now = time.time() * 1000.0
    dt = time_now - _time_prev
    _time_prev = time_now
    if dt == 0.0:
        return _fps.value
    return _fps.update(1000.0 / dt)


def memoize(function):
    """Provides a decorator for memoizing functions"""
    from functools import wraps
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@memoize
def _normalized_linspace(size):
    return np.linspace(0, 1, size)


def interpolate(y, new_length):
    """Intelligently resizes the array by linearly interpolating the values

    Parameters
    ----------
    y : np.array
        Array that should be resized

    new_length : int
        The length of the new interpolated array

    Returns
    -------
    z : np.array
        New array with length of new_length that contains the interpolated
        values of y.
    """
    if len(y) == new_length:
        return y
    x_old = _normalized_linspace(len(y))
    x_new = _normalized_linspace(new_length)
    z = np.interp(x_new, x_old, y)
    return z

r_filt = dsp.ExpFilter(np.tile(0.01, config.N_PIXELS // 2),
                       alpha_decay=0.2, alpha_rise=0.99)
g_filt = dsp.ExpFilter(np.tile(0.01, config.N_PIXELS // 2),
                       alpha_decay=0.05, alpha_rise=0.3)
b_filt = dsp.ExpFilter(np.tile(0.01, config.N_PIXELS // 2),
                       alpha_decay=0.1, alpha_rise=0.5)
# r_filt = dsp.ExpFilter(np.tile(0.01, config.N_PIXELS // 2),
#                        alpha_decay=0.1, alpha_rise=0.5)
# g_filt = dsp.ExpFilter(np.tile(0.01, config.N_PIXELS // 2),
#                        alpha_decay=0.2, alpha_rise=0.99)
# b_filt = dsp.ExpFilter(np.tile(0.01, config.N_PIXELS // 2),
#                        alpha_decay=0.05, alpha_rise=0.3)
common_mode = dsp.ExpFilter(np.tile(0.5, config.N_PIXELS // 2),
                            alpha_decay=0.99, alpha_rise=0.01)
p_filt = dsp.ExpFilter(np.tile(1, (3, config.N_PIXELS // 2)),
                       alpha_decay=0.1, alpha_rise=0.99)
p = np.tile(1.0, (3, config.N_PIXELS // 2))
gain = dsp.ExpFilter(np.tile(0.01, config.N_FFT_BINS),
                     alpha_decay=0.001, alpha_rise=0.99)

np_data = np.array([])
temp_data=np.array([])
colorWipe(strip, Color(0, 0, 0))

def visualize_scroll(y):
    """Effect that originates in the center and scrolls outwards"""
    global p,rc,gc,bc
    print("scroll",rc,gc,bc)
    y = y ** 2.0
    gain.update(y)
    y /= gain.value
    y *= 255.0
    # print("y:",y)
    # r = int(np.max(y[:len(y) // 3]))
    # g = int(np.max(y[len(y) // 3: 2 * len(y) // 3]))
    # b = int(np.max(y[2 * len(y) // 3:]))
    r = int(np.max(y[:len(y) // 3]))/9
    g = int(np.max(y[len(y) // 3:2*len(y) // 3]))/9
    b = int(np.max(y[2*len(y) // 3:]))/9
    # print("scroll r,g,b:",r,g,b)

    # Scrolling effect window
    p[:, 1:] = p[:, :-1]
    p *= 0.98
    #p = gaussian_filter1d(p, sigma=0.8)#전체적인 느낌
    p = gaussian_filter1d(p, sigma=0.2)
    # Create new color originating at the center
    if r <= 0:
        r = 0.1
    elif r>=1.0:
        r=1.0
    if g <= 0:
        g = 0.1
    elif g>=1.0:
        g=1.0
    if b <= 0:
        b = 0.1
    elif b>=1.0:
        b=1.0
    if rc <= 0:
        rc = 32  # 64~128
    if gc <= 0:
        gc = 32  # 64~128
    if bc <= 0:
        bc = 32  # 64~128
    rc=rc
    gc=gc
    bc=bc

    red=r*rc
    green=g*gc
    blue=b*bc
    if red >=255:
        red=255

    if green >=255:
        green=255

    if blue>=255:
        blue=255



    p[0, 0] = int(red)
    p[1, 0] = int(green)
    p[2, 0] = int(blue)
    # print("p:",red,green,blue)
    # Update the LED strip
    return np.concatenate((p[:, ::-1], p), axis=1)

def visualize_scroll_s(y):
    """Effect that originates in the center and scrolls outwards"""
    global p
    print("scroll")
    y = y ** 2.0
    gain.update(y)
    y /= gain.value
    y *= 255.0
    r = int(np.max(y[:len(y) // 3]))
    g = int(np.max(y[len(y) // 3: 2 * len(y) // 3]))
    b = int(np.max(y[2 * len(y) // 3:]))
    # Scrolling effect window
    p[:, 1:] = p[:, :-1]
    p *= 0.98
    p = gaussian_filter1d(p, sigma=0.2)
    # Create new color originating at the center
    p[0, 0] = r
    p[1, 0] = g
    p[2, 0] = b
    # Update the LED strip
    return np.concatenate((p[:, ::-1], p), axis=1)

def visualize_energy(y):
    """Effect that expands from the center with increasing sound energy"""

    global p,rc,gc,bc
    print("energy",rc,gc,bc)
    y = np.copy(y)
    gain.update(y)
    y /= gain.value
    # Scale by the width of the LED strip
    # y *= float((config.N_PIXELS // 2) - 1)
    y *= float((config.N_PIXELS//2) - 1)
    # Map color channels according to energy in the different freq bands
    scale = 0.9
    r = int(np.mean(y[:len(y) // 3] ** scale))
    g = int(np.mean(y[len(y) // 3: 2 * len(y) // 3] ** scale))
    b = int(np.mean(y[2 * len(y) // 3:] ** scale))
    # Assign color to different frequency regions
    if rc <=0:
        rc = 64 # 64~128
    elif rc>=255:
        rc=200

    if gc <= 0:
        gc =64 #64~128


    if bc <=0:
        bc = 0 #64~128

    p[0, :r] = rc
    p[0, r:] = 0.0
    p[1, :g] = gc
    p[1, g:] = 0.0
    p[2, :b] = bc
    p[2, b:] = 0
    p_filt.update(p)
    p = np.round(p_filt.value)
    # print("p",p)
    # Apply substantial blur to smooth the edges
    p[0, :] = gaussian_filter1d(p[0, :], sigma=4.0)
    p[1, :] = gaussian_filter1d(p[1, :], sigma=4.0)
    p[2, :] = gaussian_filter1d(p[2, :], sigma=4.0)
    # Set the new pixel value
    return np.concatenate((p[:, ::-1], p), axis=1)

def visualize_energy_s(y):
    """Effect that expands from the center with increasing sound energy"""

    global p

    y = np.copy(y)
    gain.update(y)
    y /= gain.value
    # Scale by the width of the LED strip
    # y *= float((config.N_PIXELS // 2) - 1)
    y *= float((config.N_PIXELS) - 1)
    # Map color channels according to energy in the different freq bands
    scale = 0.9
    r = int(np.mean(y[:len(y) // 3] ** scale))
    g = int(np.mean(y[len(y) // 3: 2 * len(y) // 3] ** scale))
    b = int(np.mean(y[2 * len(y) // 3:] ** scale))
    # Assign color to different frequency regions
    p[0, :r] = 255
    p[0, r:] = 0.0
    p[1, :g] = 255
    p[1, g:] = 0.0
    p[2, :b] = 255
    p[2, b:] = 0
    p_filt.update(p)
    p = np.round(p_filt.value)
    # Apply substantial blur to smooth the edges
    p[0, :] = gaussian_filter1d(p[0, :], sigma=4.0)
    p[1, :] = gaussian_filter1d(p[1, :], sigma=4.0)
    p[2, :] = gaussian_filter1d(p[2, :], sigma=4.0)
    # Set the new pixel value
    return np.concatenate((p[:, ::-1], p), axis=1)


_prev_spectrum = np.tile(0.01, config.N_PIXELS // 2)


def visualize_spectrum(y):
    """Effect that maps the Mel filterbank frequencies onto the LED strip"""
    global _prev_spectrum, rc, gc, bc
    print(rc, gc, bc)
    print("spectrum")
    # y = np.copy(interpolate(y, config.N_PIXELS // 2))*2 # 확실히 정신사나움
    y = np.copy(interpolate(y, config.N_PIXELS // 2))
    common_mode.update(y)
    diff = y - _prev_spectrum
    # print("y", y)
    _prev_spectrum = np.copy(y)

    # if rc <= 0:
    #     rc = 1
    #
    # if gc <= 0:
    #     gc = 1
    #
    # if bc <= 0:
    #     bc = 1

    if rc <= 0:
        rc = 64  # 64~128

    if gc <= 0:
        gc = 64  # 64~128

    if bc <= 0:
        bc = 64  # 64~128

    # Color channel mappings
    r = r_filt.update(y - common_mode.value)
    g = np.abs(diff)
    b = b_filt.update(np.copy(y))
    # print("r",r,"g",g,"b",b)

    # Mirror the color channels for symmetric output
    r = np.concatenate((r[::-1], r)) * rc
    g = np.concatenate((g[::-1], g)) * gc
    b = np.concatenate((b[::-1], b)) * bc
    output = np.array([r, g, b])

    return output
def visualize_spectrum_s(y):
    """Effect that maps the Mel filterbank frequencies onto the LED strip"""
    global _prev_spectrum
    print("spectrum")
    y = np.copy(interpolate(y, config.N_PIXELS // 2))
    common_mode.update(y)
    diff = y - _prev_spectrum
    _prev_spectrum = np.copy(y)
    # Color channel mappings
    r = r_filt.update(y - common_mode.value)
    g = np.abs(diff)
    b = b_filt.update(np.copy(y))


    # Mirror the color channels for symmetric output
    r = np.concatenate((r[::-1], r))
    g = np.concatenate((g[::-1], g))
    b = np.concatenate((b[::-1], b))
    output = np.array([r, g, b]) * 255
    return output


fft_plot_filter = dsp.ExpFilter(np.tile(1e-1, config.N_FFT_BINS),
                                alpha_decay=0.5, alpha_rise=0.99)
mel_gain = dsp.ExpFilter(np.tile(1e-1, config.N_FFT_BINS),
                         alpha_decay=0.01, alpha_rise=0.99)
mel_smoothing = dsp.ExpFilter(np.tile(1e-1, config.N_FFT_BINS),
                              alpha_decay=0.5, alpha_rise=0.99)
volume = dsp.ExpFilter(config.MIN_VOLUME_THRESHOLD,
                       alpha_decay=0.02, alpha_rise=0.02)
fft_window = np.hamming(int(config.MIC_RATE / config.FPS) * config.N_ROLLING_HISTORY)
prev_fps_update = time.time()


def microphone_update(audio_samples):
    global y_roll, prev_rms, prev_exp, prev_fps_update, visualization_effect
    # Normalize samples between 0 and 1
    # y = audio_samples / 2.0 ** 15 #####1012수정
    y = audio_samples / 2.0 ** 15

    print("shape",y_roll.shape)
    # Construct a rolling window of audio samples
    y_roll[:-1] = y_roll[1:]
    # y_roll[-1, :] = np.copy(y)

    y_roll[-1, :] = np.copy(y)
    print()
    y_data = np.concatenate(y_roll, axis=0).astype(np.float32)

    vol = np.max(np.abs(y_data))
    if vol < config.MIN_VOLUME_THRESHOLD:
        print('No audio input. Volume below threshold. Volume:', vol)
        led.pixels = np.tile(0, (3, config.N_PIXELS))
        led.update()
    else:
        # Transform audio input into the frequency domain
        N = len(y_data)
        N_zeros = 2 ** int(np.ceil(np.log2(N))) - N
        # Pad with zeros until the next power of two
        y_data *= fft_window
        y_padded = np.pad(y_data, (0, N_zeros), mode='constant')
        YS = np.abs(np.fft.rfft(y_padded)[:N // 2])
        # print(YS.shape)
        # Construct a Mel filterbank from the FFT data
        mel = np.atleast_2d(YS).T * dsp.mel_y.T
        # Scale data to values more suitable for visualization
        # mel = np.sum(mel, axis=0)
        mel = np.sum(mel, axis=0)
        mel = mel ** 2.0
        # Gain normalization
        mel_gain.update(np.max(gaussian_filter1d(mel, sigma=1.0)))
        mel /= mel_gain.value
        mel = mel_smoothing.update(mel)
        # Map filterbank output onto LED strip
        output = visualization_effect(mel)
        led.pixels = output
        led.update()
        # print("led.update()")
        if config.USE_GUI:
            # Plot filterbank output
            x = np.linspace(config.MIN_FREQUENCY, config.MAX_FREQUENCY, len(mel))
            mel_curve.setData(x=x, y=fft_plot_filter.update(mel))
            # Plot the color channels
            r_curve.setData(y=led.pixels[0])
            g_curve.setData(y=led.pixels[1])
            b_curve.setData(y=led.pixels[2])
    if config.USE_GUI:
        app.processEvents()

    if config.DISPLAY_FPS:
        fps = frames_per_second()
        if time.time() - 0.5 > prev_fps_update:
            prev_fps_update = time.time()
            print('FPS {:.0f} / {:.0f}'.format(fps, config.FPS))


# Number of audio samples to read every time frame
samples_per_frame = int(config.MIC_RATE / config.FPS)

# Array containing the rolling audio sample window
y_roll = np.random.rand(config.N_ROLLING_HISTORY, samples_per_frame) / 1e16
print("y_roll",y_roll)

"""Visualization effect to display on the LED strip"""
visualization_effect = visualize_spectrum_s

#genre_list=np.array([3]) 장르 스택은 나중에 생각

def start_stream(callback):
    global visualization_effect,rc,gc,bc
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    overflows = 0
    prev_ovf_time = time.time()
    while True:
        try:
            audio_data = conn.recv(1024)

            conn.sendall(audio_data)
            print("a",len(audio_data))
            if len(audio_data)==10:
                print("@@@@1", audio_data)
                audio_data=audio_data.decode()
                print("@@@@2", audio_data)
                genre=int(audio_data[0])
                print("g",genre)
                if genre == 0:  # Ballad /yellow   #OK
                    print("############", genre,audio_data)
                    visualization_effect = visualize_energy
                    rc = int(audio_data[1:4])
                    rc = int(rc)
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

                if genre == 1:  # Classical / brown  #수정필
                    print("0=", genre,audio_data)
                    visualization_effect = visualize_energy
                    rc = int(audio_data[1:4])
                    rc = int(rc)
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

                if genre == 2:  # Trot/ pink  #OK
                    print("0=", genre,audio_data)
                    visualization_effect = visualize_scroll
                    rc = int(audio_data[1:4])
                    rc = int(rc)
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

                if genre == 3:  # HipHop / blue #OK
                    print("0=", genre,audio_data)
                    visualization_effect = visualize_spectrum
                    rc = int(audio_data[1:4])
                    rc = int(rc)
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

                if genre == 4:  # Jazz / orange #OK
                    print("0=", genre,audio_data)
                    visualization_effect = visualize_energy
                    rc = int(audio_data[1:4])
                    rc = int(rc)-64
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

                if genre == 5:  # Dance / purple   #OK
                    print("0=", genre,audio_data)
                    visualization_effect = visualize_spectrum_s
                    rc = int(audio_data[1:4])
                    rc = int(rc)
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

                if genre == 6:  # Reggae /green      #OK
                    print("0=", genre,audio_data)
                    visualization_effect = visualize_scroll
                    rc = int(audio_data[1:4])
                    rc = int(rc)
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

                if genre == 7:  # Rock/metal           #OK
                    print("0=", genre,audio_data)
                    visualization_effect = visualize_spectrum
                    rc = int(audio_data[1:4])
                    rc = int(rc)
                    gc = int(audio_data[4:7])
                    gc = int(gc)
                    bc = int(audio_data[7:10])
                    bc = int(bc)
                    print("r,g,b:", rc, gc, bc)
                    led.update()

            # print("len",len(audio_data))
            if len(audio_data)==980:

                np_data = np.frombuffer(audio_data, dtype=np.float32)
                print("audio_data len",len(audio_data))
                print("np",np_data.shape)

                callback(np_data)

                print("clear")
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))
    stream.stop_stream()
    stream.close()
    p.terminate()

while True:
    # 4. Accept connection
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    data = np.array([])

    # 5. Read/Send
    data = conn.recv(1024)
    # if len(data)==245:
    #     rgb=data

    rgb=data

    if not data:
        break

    # conn.sendall(rgb)


    print("data rgblen", len(data))

    # print("type",type(rgb))
    if len(data)==9:
        print("len 9 on")
        rgb = rgb.decode()
        print("rgb", rgb)
        r=int(rgb[0:3])/9
        r=int(r)
        g=int(rgb[3:6])/9
        g = int(g)
        b=int(rgb[6:9])/9
        b = int(b)
        print("r,g,b:",r,g,b)

        colorWipe(strip,Color(g,r,b))
        print("color",Color(g,r,b))
        strip.show()
    elif len(data)==10:
        # colorWipe(strip, Color(0, 0, 0))
        # print("color", Color(0, 0, 0))
        print("len 10 on")
        rgb = rgb.decode()
        print("rgb", rgb)
        r = int(rgb[1:4]) / 9
        r = int(r)
        g = int(rgb[4:7]) / 9
        g = int(g)
        b = int(rgb[7:10]) / 9
        b = int(b)
        print("r,g,b:", r, g, b)


        if int(rgb[0])==0:  # Ballad /yellow
            print("0=",rgb[0])

            # colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))
            # strip.show()
            # visualization_effect = 0
            #visualization_effect = visualize_spectrum
            # led.update()
            start_stream(microphone_update)

        if int(rgb[0]) == 1: #Classical / brown
            print("0=", rgb[0])

            # colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))

            #visualization_effect = visualize_scroll
            start_stream(microphone_update)
        if int(rgb[0]) == 2: # Trot/ pink
            print("0=", rgb[0])

            # colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))

            #visualization_effect = visualize_scroll
            start_stream(microphone_update)

        if int(rgb[0]) == 3: #HipHop / blue
            print("0=", rgb[0])

            #colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))
            #visualization_effect = visualize_spectrum
            start_stream(microphone_update)

        if int(rgb[0]) == 4: # Jazz / orange
            print("0=", rgb[0])

            #colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))
            #visualization_effect = visualize_energy
            start_stream(microphone_update)

        if int(rgb[0]) == 5: #Dance / purple
            print("0=", rgb[0])
            #colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))
            #visualization_effect = visualize_energy
            start_stream(microphone_update)

        if int(rgb[0]) == 6: #Reggae /green
            print("0=", rgb[0])
            genre = rgb[0]
            #colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))
            #visualization_effect = visualize_spectrum
            start_stream(microphone_update)

        if int(rgb[0]) == 7: #Rock/metal
            print("0=", rgb[0])
            #colorWipe(strip, Color(g, r, b))
            print("color", Color(g, r, b))
            #visualization_effect = visualize_energy
            start_stream(microphone_update)
    elif len(data)==27:
        print("len 27 on")
        rgb = rgb.decode()
        print("rgb", rgb)
        rgb1=rgb[0:9]
        rgb2=rgb[9:18]
        rgb3=rgb[18:27]
        print("rgb1",rgb1,"rgb2",rgb2,"rgb3",rgb3)

        r1 = int(rgb1[0:3]) / 9
        r1 = int(r1)
        g1= int(rgb1[3:6]) / 9
        g1 = int(g1)
        b1 = int(rgb1[6:9]) / 9
        b1 = int(b1)

        r2 = int(rgb2[0:3]) / 9
        r2 = int(r2)
        g2 = int(rgb2[3:6]) / 9
        g2 = int(g2)
        b2 = int(rgb2[6:9]) / 9
        b2 = int(b2)

        r3 = int(rgb3[0:3]) / 9
        r3 = int(r3)
        g3 = int(rgb3[3:6]) / 9
        g3 = int(g3)
        b3 = int(rgb3[6:9]) / 9
        b3 = int(b3)


        scene_colorWipe(strip,  Color(g1, r1, b1),Color(g2,r2,b2),Color(g3,r3,b3))
        print("color",  Color(g1, r1, b1),Color(g2,r2,b2),Color(g3,r3,b3))
        strip.show()




    print('Starting LED strand test')


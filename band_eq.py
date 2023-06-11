# Heavily built upon what was done in the 2nd homework assignment.
from wav_io import args, rate, data
from numpy import transpose, multiply
from scipy.signal import firwin, lfilter

# calculates a gain coefficient based on the knob value, 
# knob offset, and a 3 db per volume set increase.
def knob_to_gain(knob_val, knob_offset):
    if knob_val < 0.1:
        return 0
    db = 3.0 * (knob_val - knob_offset)
    return pow(10.0, db / 20.0)

def filter(rate, data):
    # scipy cookbook documentation for making a low pass filter, adapted for band and highpass filters
    # https://scipy-cookbook.readthedocs.io/items/FIRFilter.html
    # also used firwin documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html

    # kaiser windowing will be used along with filtering, makes things less harsh when applying filters 
    # and allows for some rolloff between bands - may want to adjust beta value?
    lowpass_taps = firwin(255, 300, pass_zero = 'lowpass', fs = rate, window = ('kaiser', 13.5))
    bandpass_taps = firwin(255, [300, 4000], pass_zero = 'bandpass', fs = rate, window = ('kaiser', 13.5))
    highpass_taps = firwin(255, 4000, pass_zero = 'highpass', fs = rate, window = ('kaiser', 13.5))

    # now applying the filter using the lfilter function
    # lfilter documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html
    lowpass = lfilter(lowpass_taps, 1, data)
    bandpass = lfilter(bandpass_taps, 1, data)
    highpass = lfilter(highpass_taps, 1, data)

    # producing the weighted bands and summing to make the altered file
    # https://numpy.org/doc/stable/reference/generated/numpy.multiply.html
    data = multiply(knob_to_gain(args.volume, 9), 
                    (multiply(knob_to_gain(args.bass, 5), lowpass) 
                    + multiply(knob_to_gain(args.midrange, 5), bandpass) 
                    + multiply(knob_to_gain(args.treble, 5), highpass)))
    return data


# a 2D array indicates a stereo file, so it must be transposed, and the channels processed independently
# https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
if(data.ndim == 2):
    transposed = transpose(data)
    left_channel = transposed[0]
    right_channel = transposed[1]
    left_filtered = filter(rate, left_channel)
    right_filtered = filter(rate, right_channel)
    # putting the channels back together once they've been filtered, and transposing back
    stereo_data = (left_filtered + right_filtered)
    transpose(stereo_data)
    filtered = stereo_data

# otherwise, the file is mono and can be processed normally.
else:    
    filtered = filter(rate, data)

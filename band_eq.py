# Heavily built upon what was done in the 2nd homework assignment.
from wav_io import args, rate, knob_to_gain
from distort import distorted
from numpy import transpose, multiply, column_stack
from scipy.signal import firwin, lfilter

def filter(rate, data):
    # Scipy cookbook documentation for making a low pass filter, adapted for band and highpass filters
    # https://scipy-cookbook.readthedocs.io/items/FIRFilter.html
    # Also used firwin documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html

    # Kaiser windowing will be used along with filtering, makes things less harsh when applying filters 
    # and allows for some rolloff between bands - may want to adjust beta value?
    lowpass_taps = firwin(255, 300, pass_zero = 'lowpass', fs = rate, window = ('kaiser', 13.5))
    bandpass_taps = firwin(255, [300, 4000], pass_zero = 'bandpass', fs = rate, window = ('kaiser', 13.5))
    highpass_taps = firwin(255, 4000, pass_zero = 'highpass', fs = rate, window = ('kaiser', 13.5))

    # Now applying the filter using lfilter: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html
    lowpass = lfilter(lowpass_taps, 1, data)
    bandpass = lfilter(bandpass_taps, 1, data)
    highpass = lfilter(highpass_taps, 1, data)

    # Producing the weighted bands and summing to make the altered file
    # https://numpy.org/doc/stable/reference/generated/numpy.multiply.html
    data = multiply(knob_to_gain(args.volume, 9), 
                    (multiply(knob_to_gain(args.bass, 5), lowpass) 
                    + multiply(knob_to_gain(args.midrange, 5), bandpass) 
                    + multiply(knob_to_gain(args.treble, 5), highpass)))
    return data


# A 2D array indicates a stereo file, so it must be transposed, and the channels processed independently
# https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
if (distorted.ndim == 2):
    transposed = transpose(distorted)
    left_channel = transposed[0]
    right_channel = transposed[1]
    left_filtered = filter(rate, left_channel)
    right_filtered = filter(rate, right_channel)
    
    # Putting the channels back together once they've been filtered
    stereo_data = column_stack((left_filtered, right_filtered))
    filtered = stereo_data

# Otherwise, the file is mono and can be processed normally.
else:    
    filtered = filter(rate, distorted)

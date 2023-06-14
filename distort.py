# Applying the distortion effects
from wav_io import args, data, rate, knob_to_gain
from numpy import column_stack, transpose, clip, multiply
from scipy.signal import firwin, lfilter

# Amplitude at which to clip waveforms (will reduce volume as side effect at high levels)
clip_amplitude = .5 * (.6309573445 ** args.distortion)
# Factor to put audio volume roughly back to pre-distortion levels before further processing
normalize_factor = (1.88 ** (args.distortion - 8.3)) + 1
# Both these equations were found by finding an equation of best fit
# to input/output value pairs chosen by trial and error

# Tone control filter, cuts off around C4
# used firwin documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html
# kaiser window was kept for a cleaner-sounding cutoff
taps = firwin(255, 265, pass_zero = False, fs = rate, window=('kaiser', 13.5))
tone_input = knob_to_gain(args.tone, 5)

# a 2D array indicates a stereo file, so it must be transposed, and the channels processed independently
# https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
if (data.ndim == 2):
	transposed = transpose(data)
	left_channel = transposed[0]
	right_channel = transposed[1]

	# Clipping for basic fuzz-like distortion, understanding of pedal effects largely from this article
	# https://mynewmicrophone.com/guitar-pedals-boost-vs-overdrive-vs-distortion-vs-fuzz/
	left_channel = clip(left_channel, -clip_amplitude, clip_amplitude) * normalize_factor
	right_channel = clip(right_channel, -clip_amplitude, clip_amplitude) * normalize_factor

	# Apply tone control to shape distortion sound
	# intended shape was something like the screenshots roughly halfway down this blog post:
	# https://digilent.com/blog/sine-waves-and-guitar-effects-pedals/
	left_channel = multiply(tone_input, lfilter(taps, 1, left_channel))
	right_channel = multiply(tone_input, lfilter(taps, 1, right_channel))
    
	# putting the channels back together once they've been filtered
	stereo_data = column_stack((left_channel, right_channel))
	distorted = stereo_data

# otherwise, the file is mono and can be processed normally.
else:
	distorted = clip(data, -clip_amplitude, clip_amplitude) * normalize_factor
	distorted = multiply(tone_input, lfilter(taps, 1, distorted))

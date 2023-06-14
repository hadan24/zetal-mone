# The Zetal Mone Distortion Pedal
Created by Thomas Brooks and Dan Ha

## Project functionality
This project is built to be a mock-up of a guitar distortion pedal, featuring distortion, tone, and gain control, along with a 3-band EQ to control bass, 
midrange, and treble. The pedal takes in `.wav` files as input, applies the selected distortion, tone, and EQ manipulation onto the file. The output
files created after this manipulation can either be played to the device's selected sound device, or written to a new `.wav` file. 
Un-distorted guitar riffs are already provided in the `.\wav_files\` directory for testing purposes. Both mono and stereo `.wav` files are provided.
Of course, the program can manipulate any type of `.wav` file, but it will work best with a file that contains guitar music.  

The program can be run via the standard python execution command, as follows --  
`python3 zetal_mone.py .\wav_files\[wav file name].wav`  
The only required argument is a wav file for input. With no arguments selected, each emphasis for distortion, EQ, etc will be applied with their standard
values. An example of running the project with all possible arguments (specifically adding heavy distortion and bass emphasis) would be as follows --  
`python3 zetal_mone.py --distortion 8 --tone 7 --bass 8 --midrange 4 --treble 4 .\wav_files\[wav file name].wav`  
The manipulated `.wav` file defaults to playing to the default sound device, but will write to a new file with the argument `--out [filename].wav`  

## Example of code operation
A short video of code operation can be found in the presentation video created for the project, linked [here.](/PRESENTATION.mp4)

## What worked, what didn't, and needed improvements
Making the 3-band EQ functionality was probably the easiest part of the project. We were able to just directly implement and use the code previously written for
the second assingment, as most distortion pedals with EQ features use a 3-band to control bass, midrange, and treble levels. The tone level control also seemed to
work quite well.  
  
The main difficulty came with the distortion. In the end, we are both satisfied with the distortion effect we were able to achieve along with the 3-band EQ, as it
modestly mimics a pedal. With that said, it's not exactly matching the tone created by the distortion pedal bought for the project. It turned out to be a lot more difficult
than anticipated creating the distortion effect. With more time, we would definitely try to hone in the distortion effect to create a sound more akin to an actual pedal.  

## License
The license for this project can be found [here.](/LICENSE.txt)
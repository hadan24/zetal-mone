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
`python3 zetal_mone.py --distortion 8 --tone 7 --bass 8 --midrange 4 -- treble 4 .\wav_files\[wav file name].wav`
The manipulated `.wav` file defaults to playing to the default sound device, but will write to a new file with the argument `--out [filename].wav`

## Example of code operation
Will add a link to a short video showing an example of code operation once complete.

## What worked, what didn't, and needed improvements
TBD, need to fully implement distortion functionality to finish project before we can go into detail about what worked/didn't work

## License
The license for this project can be found [here.](/LICENSE.txt)
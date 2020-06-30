# USRC Drone Racing Competition 2020

This is the repo for Group 4's submission in the USRC Drone Racing Competition for 2020

## Implementation Details

This implementation uses Canny edge detection to first detect the yellow and blue tape in a hsv filtered image of the drones FPV. Then, a Hough line transform creates a guide lane on either side of the drone representing the yellow and blue tape in the drone's simulated environment. Finally, the drone calculates a heading that keeps it equidistant from the guide lanes on either side if both are detected. If only one guide lane is detected, the drone adjusts it heading such that it travels parallel to the detected guide lane until it detects both again.

## Usage

The file `cannyCar.py` is intended to be copied into the root folder of the [USRC simulator repo](https://github.com/usydroboticsclub/DRCSimulator) and run in the same fashion as `sampleCar.py` from the terminal. The utils folder just contains bits and pieces that were useful during the development of the final script, nothing in there is necessary for running `cannyCar.py` 


## Future Work

Intended future work includes:
- Adding more comments to improve readability and coherency of the program
- Modularizing the script so that others may work on or implement parts of this project, particularly the line and heading calculations
- Implementing a debugging feature to help with future modifications  

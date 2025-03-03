# RoboDK UR script -> Pulse python code

## Installing

    pip install URScriptToPulseConverters

Allows you to generate a program for Pulse robots using the program generated by the Universal_Robots.py postprocessor. To work correctly, you need to make some changes to the code of the script Universal_Robots.py.

RoboDK UR postprocessor path example: ***'C:\RoboDK\Posts\Universal_Robots.py'***

***Changes***

![screenshot of sample](screenshots/122116.png)
![screenshot of sample](screenshots/124519.png)

## Console Interface

***Arguments***

Path to save pulse program

    "-s", "--save_path", default='processedPrograms', "save program in special folder"

Pulse program program name

    "-n", "--name", default="path", help="program name"

Path to the original program generated from Universal_Robots.py postprocessor

    "-i", "--initial_program", help="program name"

Pulse robot IP, port

    "-o", "--host_name", default="127.0.0.1:8081", help="robot host name"

## Launch

    URToPulse -o='192.168.1.33:8081' -i='RoboDKPrograms/Path1.script'

    >>> SAVED: processedPrograms\path.py

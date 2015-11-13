# F15LTA
Each semester the AerE 160 class does a Lighter Than Air vehicle competition.  Each year a new theme is picked that guides the students in the design of their aircraft and also the design of the obstacle course.  This year the theme is retro-video games with some "Wreck-it Ralph" thrown in there for good measure.  The files in this repo are the programs and some other files used.  The details of the files are explained below.

## Diet-Coke and Mentos Jump
The first major obstacle the students will encounter is the Diet-Coke and Mentos Jump.  Students must land their aircraft on a platform, then wait for the green light.  They then have 60 seconds to "Jump" to the next platform.  Of course we do not make this easy so fans are placed pointed up that try to push them off course.  The timing is predictable for the fans.

The arduino code for this reads a force sensor that determines when they have landed.  Once landed it waits 5 seconds then triggers a green light.  It then starts a timer for 60 seconds.  If the student lands before the 60 seconds is up, then a "winner" sign is lighted.  If not, the light turns red and the system resets.

## Niceland Apartments
For this task students were broken into two groups.  The Honors section was tasked to fixing the window.  This was done by using an IR sensor to transmit a code to each one.  The rest of the class was to "break" the windows.  This was done by pushing a large button in front of the display.  A raspberry pi is used to read the IR sensor and button and will then display either a broken window or a fixed window.  Python is used to read the sensors and display the image.  

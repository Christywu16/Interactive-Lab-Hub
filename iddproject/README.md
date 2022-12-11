Christy Wu, Jane Wang

Interaction video: https://youtu.be/cfKcqcfuPkg


Project Plan: https://docs.google.com/document/d/1tY0dgCaez3t-gsv-lJSgg6SQf8FUCPhlGfKZ0m2dYyw/edit?usp=sharing

Slides: https://docs.google.com/presentation/d/1il5nJV2FVKNd_7D5PSS36YFSi_BLxcFjOCkexU8aIdo/edit?usp=sharing

Function Check-off: https://youtu.be/9GMC1wE6zsY

Project Reflection: https://docs.google.com/document/d/194lsdhRObo3M87lPoVFc20oKGndOnBeBeQU28u12rzE/edit?usp=sharing


Christmas Advent Calendar

 building a Christmas Advent calendar to count the days of advent to Christmas from December 1st to Christmas Eve. Users could open a “calendar door” every day to reveal a different Christmas song. We would use two touch sensors to detect the day user’s trying to see and use the webcam to play the song. We will also use an OLED display to display the days left until Christmas. 
 
Timeline

Nov 18th: Confirm project idea
Nov 25th: Assemble and order needed parts/sensor, foundational coding parts 
Dec 2th: Furthur coding parts for essential functions, e.g. reading data from sensors, showing data on raspberry pi screen interface 
Dec 9th: 1) Testing; 2) Adding button, Joystick, LED and interaction of them 
Dec 16th: Finalize documents and coding, final Project Deadline 

Parts needed

1 x Raspberry Pi 4 Computer Kit
1 x Adafruit MPR121 Capacitive Touch Sensor QT
1 x Adafruit Mini PiTFT
1 x SparkFun Qwiic OLED Display
1 x Copper Foil Tape
1 x Raspberry Pi 4 Power Supply with USB C
1 x 32GB MicroSD Cards w/ Card Reader

Risks/contingencies
We may need two to three touch sensors to have each calendar day match to an individual hole on the touch sensor. There’s the risk that the Raspberry Pi couldn’t detect multiple touch sensors at the same time, or give inaccurate touch results.
The copper foil tape may need to be sticked on the back of the cardboard sticker in a certain way to be conductive and readable to the whole calendar.
The joystick may not give accurate results with the user's manipulation on the time, ex. The users may accidentally push up or down when they want to adjust the appointment time that would result in logging a wrong time. 

Fall-back plan
If the interaction has some unexpected difficulty or if the Joystick part function couldn’t run as we expected, we will simplify the device to only play the Christmas song once so that we will have the MVP product to allow raspberry pi read the date from users’ mark on the deadline. 

Documentation: 

Design process:
In the beginning, we prioritized working on the playing of songs when the user touches the touch sensor. We had a function on play_song.py to assign each touch sensor point a different Christmas song. One challenge here was how to design the touch interaction and how to arrange the copper tape on the physical cardboard calendar. The initial idea was it will play the song when the user takes out of one of the boxes, while this is hard to achieve since the program will be based on while there is no data received on the touch sensor. Then we convert the copper tape to the jointer point between box and cardboard so that the user would touch the copper when they take out the box. However, when we ran the user test, we found that users took out the box in many different ways and they usually don’t touch the copper while taking the box. Finally, we decided to have the interaction with the user opening the box instead of taking out the box. In this way, we can connect the copper tape through the inside of the box with the back of the cardboard. And tape the copper tape on the back of the bottom clip on the box, so that the user will touch it when they open the box.  


After we had this feature on our interaction for the MVP of the product, we then added a few other essential features. Since the usage scenario will be user waiting for the day of Christmas coming, we added the feature of fetching the date and playing how many dates there are left until Christmas. While users check calendars, it’s always useful to inform the user of the weather to help them make plans for the day. So, we did research on some different weather APIs. After investigating and comparing them, we decided to use OpenWeatherMap for our project. We used it to fetch the weather according to New York City’s longitude and latitude. Then we used the part we learned from the lab to show date, weather, and temperature on the raspberry pi screen. Afterwards, we added the joystick interaction to control the play of the song. 

Reflections on process (What have you learned or wish you knew at the start?)




Group work distribution 


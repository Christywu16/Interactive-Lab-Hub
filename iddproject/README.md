# Final Project
Chirsty Wu, Jane Wang

Final Interaction video: https://youtu.be/cfKcqcfuPkg

[Project Plan](#project-plan) 

[Documentation of Design Process](#documentation-of-design-process)

[Reflection](#reflection)

[Group work distribution](#group-work-distribution)

## Project Plan

### Big Idea

Our idea is building a Advent calendar to count down the days to Christmas by revealing a Christmas song every day from December 1st. We will use cardboard to make 24 mini "CD" with copper tape on the back. User could pick a "CD" everyday, and put it into a drawer of the calendar. When the "CD" is detected by the touch sensor, the calendar will play a Christmas song through the music player. We will also use a Mini PiTFT to display the days left until Christmas and the name of the playing song. We would also use the joystick for users to play/pause/replay the song.

<img width="462" alt="image" src="https://user-images.githubusercontent.com/46438303/207719499-fd3fb820-3316-401a-81b8-e9d626168214.png">

<img width="507" alt="image" src="https://user-images.githubusercontent.com/46438303/207719550-371c1b84-c4db-4234-b280-e1954b850012.png">

<img width="480" alt="image" src="https://user-images.githubusercontent.com/46438303/207719601-945a719e-33a5-487f-b15d-005c27548ff5.png">

*Calender picture credit to Amazon.com
### Timeline
Nov 18th: Confirm project idea   
Nov 25th: Assemble and order needed parts/sensor, foundational coding parts    
Dec 2th: Furthur coding parts for essential functions, e.g. reading data from sensors, showing data on raspberry pi screen interface     
Dec 9th: 1) Testing; 2) Adding button, Joystick, LED and interaction of them      
Dec 16th: Finalize documents and coding, final Project Deadline


### Parts Needed
1 x Raspberry Pi 4 Computer Kit 
1 x Adafruit MPR121 Capacitive Touch Sensor QT      
1 x Adafruit Mini PiTFT    
1 x SparkFun Qwiic OLED Display    
1 x Copper Foil Tape       
1 x Raspberry Pi 4 Power Supply with USB C      
1 x 32GB MicroSD Cards w/ Card Reader   

### Risks/ Contingencies
We need two to two touch sensors to have each calendar day match to an individual hole on the touch sensor. There’s the risk that the Raspberry Pi couldn’t detect multiple touch sensors at the same time, or give inaccurate touch results.
The copper foil tape may need to be sticked on the back of the cardboard sticker in a certain way to be conductive and readable to the whole calendar.
The joystick may not give accurate results with the user's manipulation or not intuitive to users. 

### Fall-back Plan
If the interaction has some unexpected difficulty or if the Joystick part function couldn’t run as we expected, we will simplify the device to finish playing the Christmas song once the user revealing the calendar door, so that we will have the MVP product to allow raspberry pi play a different song everyday in countdown to Christmas.

Slides: https://docs.google.com/presentation/d/1il5nJV2FVKNd_7D5PSS36YFSi_BLxcFjOCkexU8aIdo/edit?usp=sharing

## Documentation of Design Process
### Task 1: Playing Song
![IMG_7452](https://user-images.githubusercontent.com/46438303/207715010-e333e0c4-ab5b-4206-b934-b117fabe80dc.JPG)

In the beginning, we prioritized working on the playing of songs when the user touches the touch sensor. We had a function on play_song.py to assign each touch sensor point a different Christmas song. When user pressing on the sensor, the music player would play the corresponding song. 

### Task 2: Counting Down to Christmas
After we had music playing on our interaction for the MVP of the product, we then added a few other essential features. Since the usage scenario will be user waiting for the day of Christmas coming, we added the feature of fetching the date and playing how many dates there are left until Christmas. As the counting down starting from December 1st, we use 25 - today's day to calculate how many days left to Christmas.

### Task 3: Announcing and Displaying Today's Weather and Temperature
While users check calendars, it’s always useful to inform the user of the weather to help them make plans for the day. So, we did research on some different weather APIs. After investigating and comparing them, we decided to use OpenWeatherMap for our project. We used it to fetch the weather according to New York City’s longitude and latitude. Then we used the part we learned from the lab to show date, weather, and temperature on the raspberry pi screen. 

<img width="303" alt="image" src="https://user-images.githubusercontent.com/46438303/207718513-60b1b3ff-0b70-46d2-a500-9f6555b54948.png">

### Task 4: Using joystick to control the music player
Afterwards, we added the joystick interaction to control the play of the song. The user could push the joystick backword to pause a playing song. 
[![Watch the video](https://img.youtube.com/vi/PZrnbkUqFIo/maxresdefault.jpg)](https://youtu.be/PZrnbkUqFIo)

### Task 5: Deployment on the actual calendar
One challenge here was how to design the touch interaction and how to arrange the copper tape on the physical cardboard calendar. The initial idea was it will play the song when the user takes out of one of the boxes, while this is hard to achieve since the program will be based on while there is no data received on the touch sensor. Then we convert the copper tape to the jointer point between box and cardboard so that the user would touch the copper when they take out the box. 

<img width="965" alt="image" src="https://user-images.githubusercontent.com/46438303/207716593-f540a062-1647-40dc-88cc-4ada4f73e259.png">

However, when we ran the user test, we found that users took out the box in many different ways and they usually don’t touch the copper while taking the box.

<img width="546" alt="image" src="https://user-images.githubusercontent.com/46438303/207716107-17558a2c-9f65-4349-b4ec-f8c1dd1d442e.png">

After we observed how would the user naturally interact with the calendar, we decided to have the interaction with the user opening the box instead of taking out the box. In this way, we can connect the copper tape through the inside of the box with the back of the cardboard. And tape the copper tape on the back of the bottom clip on the box, so that the user will touch it when they open the box.  

<img width="327" alt="image" src="https://user-images.githubusercontent.com/46438303/207710059-6033ce9b-49e6-493f-8b5b-e71a85785e47.png">

### Final Product Video
[![Watch the video](https://img.youtube.com/vi/cfKcqcfuPkg/maxresdefault.jpg)](https://youtu.be/cfKcqcfuPkg)

## Reflection
We were able to investigate the different sensors/parts of the raspberry kit and practiced how to incorporate them together from design and development aspects. We also learned the Agile methodology while implementing our project by developing the MVP first and building the various features incrementally to make the product more integrated and adapted to change. We constantly iterated and trimmed our product to make it usable and useful with the essential functionalities. In this process, we have more and more clear pictures of what we want our final calendar to be like.
We wish that we could also distribute the usability testing in the earlier prototype stage and observe how the users intuitively interact with the actual calendar before generating the final product so that we could develop the device accordingly.

## Group Work Distribution
We worked together for ideation and planning process. For developing, Christy is responsible fore the weather fetching, pi screen, and assemble phisical interaction. Jane is responsible for speech to text, joystick interaction, combine and debug the code.

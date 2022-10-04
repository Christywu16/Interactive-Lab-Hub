# Chatterboxes
**Jane Wang, Sylvia Ding, Christy Wu**
https://github.com/Sylv1011/Interactive-Lab-Hub/blob/2f8c025ff7a85982e50dde950cb06bba605f6a9c/Lab%203/README.md
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

<picture>
  <img alt="Storyboard 1" src="https://github.com/Sylv1011/Interactive-Lab-Hub/blob/Fall2022/Lab%203/Storyboard1.jpg">
</picture>

<picture>
  <img alt="Storyboard 2" src="https://github.com/Sylv1011/Interactive-Lab-Hub/blob/Fall2022/Lab%203/Storyboard2.jpg">
</picture>

We developed 2 ideas initially, and after discussion with many people, the second idea is much more preferred. Therefore, I decided to keep the the second idea and expand on that. 

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

For this part of the lab, I expanded on only 5 colors and created some logic flows. I used Voiceflow as my prototyping tool and added different utterances for each variable and response that we entered. Also we ideated for the case when the voice assistant did not catch the speaker's response. 

<picture>
  <img alt="VA1" src="https://github.com/Sylv1011/Interactive-Lab-Hub/blob/Fall2022/Lab%203/VA1.png">
</picture>


<picture>
  <img alt="VA2" src="=https://github.com/Sylv1011/Interactive-Lab-Hub/blob/Fall2022/Lab%203/VA2.png">
</picture>


<picture>
  <img alt="VA3" src="https://github.com/Sylv1011/Interactive-Lab-Hub/blob/Fall2022/Lab%203/VA3.png">
</picture>


<picture>
  <img alt="VA4" src="https://github.com/Sylv1011/Interactive-Lab-Hub/blob/Fall2022/Lab%203/VA4.png">
</picture>

\*\***Please describe and document your process.**\*\*

We want to design a tool to assist people with visual impairment to learn color. We have discussed several ways to provide feedback such as temperature and vibration to help people feel that color. After analyzing the pros and cons of different methods, we decided to use voice feedback with the description of each color to assist them. 

We developed the script based on people's understanding and feelings of the color, e.x. feeling embarrassed makes people think of red, to inform users of the color they are thinking about. Then the assistant will ask users if they want to feel the color, and it'll direct the user to put their finger on the sensor to feel the color through a haptic sensor to convey various colors. 


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).




https://user-images.githubusercontent.com/38329866/192392188-fbaf7f44-8961-416c-beaa-28eeed61dd10.mov


\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*
![DeviceFlow](https://user-images.githubusercontent.com/71368796/193726859-8fcf5a6b-c322-4474-b1c0-ec334c8c0397.png)

![colorScheme](https://user-images.githubusercontent.com/71368796/193726846-e04d02ae-c641-4aae-96e3-c66267cdfa92.jpg)


![PurpleLight](https://user-images.githubusercontent.com/71368796/193726792-c7bdd719-e1dd-4704-89bb-a84b16a653d6.jpeg)



https://user-images.githubusercontent.com/71368796/193726801-1d219555-9451-4126-bab2-85953a396325.mp4


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Chrsity Wu & Jane Wang: Utilized the given Speech2Text and Text2Speech files to achieve the designed voice flow as initial approach to build the virtual assistant, tested the code, and discussed the ideas that could be researched further.

https://user-images.githubusercontent.com/71368796/193724794-14d9f5bb-3062-4744-a3c1-40de9f62343f.mp4


https://user-images.githubusercontent.com/71368796/193724803-7e51a943-bd13-4546-a277-27c42a316ade.mp4


Answer the following:

### What worked well about the system and what didn't?

Initially we had designed a haptic system to aid the user to understand. Due to lack of hardware we transitioned to implementing a temperature sensor. The connection between temperature and colour is possibly rather weak. We implemented the intent to the best of our ability, and are happy with the result. In the end we still hope and intend to use the temperature feature as an addition to the original haptic design. The speech-to-text and text-to-speech portions of this device worked well, especially augmented by the cloud abilities of the Google cloud API. This engine for TTS and STT proved much more robust and faster than that of the on-board engines we originally demoed in part one (Vosk… etc.)

### What worked well about the controller and what didn't?

We were able to catch utterances in most of the cases and counted in no-match situations. However, sometimes when the intent of the voice assistant has long phrases, users tend to speak when the assistant has not finished its sentence. Also, in our design, we want to include secondary users (friends/families of the blind user), so we added LED light blub. But we did face the question from testing sessions that asked us when a device designed for blind people has a visual color code.


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

We can add various style of intrepretations for the the same color and form a dataset accordingly. For exmaple, we can collect one version for feelings relating to each color, one version for the senarios, and another one of a quote from poetry. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?


To extend the interaction, we can make a remote controller with bluetooth adding to the system, which allow uses to interact with the assistant while they are exploring around.

We are also interested in using computer vision to detect facial expressions of the speaker. In this instance the additional data (if available) can be used to augment the processing to see if our user understands or needs further clarification. It is possible that a user can endure a conversation, receive the information, and yet remain confused. Using CV is an additional dataset that we can possibly use to fulfill our intention as best we can.

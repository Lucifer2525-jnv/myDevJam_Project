# myDevJam_Project
This is a project based on Automation of IoT devices and day to day tasks using PythonScripts, Django, Proteus, Ajax

Issues Related to Project.......
Currently we are able to send command to our Proteus software as COMPIM TX blinks when command to trigger any node(Led_Light) is send via our pythonScript but execution is not reflected by turning led on.(We are still working over it.)
Reason what we are thinking is probably there is an issue regarding code sended by script may contain some specialcharacter(\r\n etc..) which is not recognised by our simulator....we tried to .encode() and .decode() it in ascii and bytes but it didnt worked. Since we couldnt get Physical Arduino board at present so our debugging totlly depends over this simulation(which itself have some unknown constraints since it simulates to real but can't be real)....but still we are working to get solution.


Also we have made a Sensors reading plotter using Django over local browser to link it with our automation pythonScript inorder to make it a complete system where vital senors(like medical) can be linked and monitored by user.

Note:
Apology for recording video via phone camera...since laptop mic was used by our project...so to avoid interferce we were compelled to record via phone camera


Here is a demo video of our project
(https://drive.google.com/file/d/1EycLQMWLEypgM3KqHYJoM7w1nOSABWM3/view?usp=drivesdk)

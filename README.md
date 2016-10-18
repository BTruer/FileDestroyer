# FileScrambler
Destroy a text file by iterativly writing over it. Have you ever save'd your passwords any important information in a textdocument? This simple program will write over it a few times. Then go ahead and use your system's delete to send it to a trashbin or recyclingbin. Then remove the file from the bin. This is not a graunteed way of making something unreadble and unrecoverable, but it is a quick solution if you have sensitive information that is unencrypted. 
## How to use it
1. Download zip from this page (https://github.com/BTruer/FileScrambler/)
2. Drag the txt file you want to destroy into the folder which contains scramble.py
3. Open bash/cmd and move into the folder
4. Run `python scramble.py <filename> <number of iterations to run (int)>`

Example use case `python scramble.py passwords.txt 15`

Make sure you have python2.7 installed

# dreamlands
A CoC TRPG game table project.
 
A chatroom-like game table both KP and PL can use together.  Should be deployed on a server with ease.

## Components

- Playground
- Multi-channel chatroom
- PC/NPC management
- Dice
- Log
- Battlefield

#### Playground 
Display background picture and BGM uploaded by KP.  
Show avatars of PC and NPC, and anything necessary for the game. 
Players mainly use this part during gaming.   
The display of the room（部屋） can be saved in a config file, which will make it easy to share completed room with other KP.  

#### Multi-channel chatroom
Chatroom, used by KP and PL to communication.  
Should be multi-channel as some message should not be displayed to everyone in the game. 

#### PC/NPC management  
PC and NPC can be create in this part. Parameter, job, story and other status can be saved. Status like HP and Sanity can be update during game play.

#### Dice  
A dice for the game. Can automatically judge the result of a check (san check, pow check, skill check, etc.). 

#### Log
Keep the game history in the log. Can be export in some usual format (consider in txt or xml). Maybe can import external log?

#### Battlefield  
Normal: a chessboard like battlefield, size can be assigned by KP.    
Chasing: a battlefield with dynamic size and edge, edge will change during chasing to simulate a road or something.

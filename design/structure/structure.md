# 总体架构

## 组件
- Playground 
    - Multi-channel Chat
    - Log
    - Battlefield
        - normal battle
        - chasing
- Charactor Management
    - Card Creator
    - Card Import/Export
- Dice


## 细节构想
导入的卡或者车出来的卡通过xml存放  
聊天室功能用WebSocket实现  
多频道聊天可以开很多连接，也可以只开一个连接，之后用filter来实现多频道的效果，每个人的消息前带上身份标识，也便于后期整理log  
考虑到可能有很多人使用，可能需要进行登录来进行身份识别，但是车出来的卡作为私有还是公有，可能需要后续讨论，先做公有，私有化作为后续功能  
先不做完整的车卡，仅做属性导入  
骰子可以直接进行检定，且可以检定出成功等级
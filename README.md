# Some automation files for my HightechPet door


## Files
* opendoor and closedoor is decorated for Home Assitant pyscript
* statusdoor is normal python

## Message format
* cmd or config is important based on what getting config vs opening door
* msgId can change and is not that important
* dir not sure what it does but leave as is



## commands and message format

To CANCEL_FIRMWARE_UPDATE --> {"cmd":"CANCEL_FIRMWARE_UPDATE","msgId":797,"dir":"p2d"}
To DISABLE_INSIDE --> {"config":"DISABLE_INSIDE","msgId":759,"dir":"p2d"}
To ENABLE_INSIDE --> {"config":"ENABLE_INSIDE","msgId":806,"dir":"p2d"}
To DISABLE_OUTSIDE --> {"config":"DISABLE_OUTSIDE","msgId":809,"dir":"p2d"}
To ENABLE_OUTSIDE --> {"config":"ENABLE_OUTSIDE","msgId":810,"dir":"p2d"}
To OPEN_AND_HOLD --> {"cmd":"OPEN_AND_HOLD","msgId":812,"dir":"p2d"}
To OPEN --> {"cmd":"OPEN","msgId":799,"dir":"p2d"}
To CLOSE --> {"cmd":"CLOSE","msgId":815,"dir":"p2d"}
To POWER_ON --> {"config":"POWER_ON","msgId":820,"dir":"p2d"}
To POWER_OFF --> {"config":"POWER_OFF","msgId":818,"dir":"p2d"}
To GET_DOOR_STATUS --> {"config":"GET_DOOR_STATUS","msgId":754,"dir":"p2d"}
To GET_SETTINGS --> {"config":"GET_SETTINGS","msgId":752,"dir":"p2d"}
To get HW and forimare --> {"config":"GET_HW_INFO","msgId":752,"dir":"p2d"}
CMD_GET_HW_INFO --> 


There is also a Ping command that would look something like the below (it is calculated based on the epoch time) and responds back with a JSON response called PONG :) 

'{"PING":"'+str(round(time.time()*1000))+'","msgId":764,"dir":"p2d"}'

## Possible other commands, not tested yet
CMD_ENABLE_AUTO = "ENABLE_TIMERS"
CMD_GET_DOOR_BATTERY = "GET_DOOR_BATTERY"
CMD_HAS_REMOTE_ID = "HAS_REMOTE_ID"
CMD_HAS_REMOTE_KEY = "HAS_REMOTE_KEY"
CMD_CHECK_RESET_REASON = "CHECK_RESET_REASON"

# Desktop Notifier project in Python

import time 
from winotify import notification, audio

toast = notification(app_id = "Project",
                     title = "Rest",
                     msg = "You need some rest"
                     duration = "long",
                     icon = "D:\SYNC INTERN\notification-bell.png")
        
toast.set_audio(audio.LoopingAlarm, loop = true)

toast.show()
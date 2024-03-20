from plyer import notification
import ctypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def send(number, msg):
    if notification:
        # Get the default audio playback device
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)

        # Mute the sound
        volume.SetMute(True, None)

        notification.notify(
            title=number,
            message=msg,
            app_name="",
            timeout=10,  # notification will disappear after 10 seconds
        )


send("1", "you name")

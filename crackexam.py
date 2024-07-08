import pyperclip
import time
from PIL import Image

from PIL import ImageGrab
import clipboard
import re
import google.generativeai as genai
import requests
import json
from plyer import notification
import ctypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import re

genai.configure(api_key="add your api here (gemmine api)")

model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat()


def send(number, msg):
    if notification:
        # Get the default audio playback device
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)

        # Mute the sound
        volume.SetMute(True, None)

        notification.notify(
            title=str(number),
            message=str(msg),
            app_name="",
            timeout=18,  # notification will disappear after 10 seconds
        )


def clean(input_string):

    string = re.sub(r"\s{3,}", " ", input_string)
    string = string.replace("\n", " ")
    string = string.replace("\r", " ")
    return string


def is_question(text):
    text = clean(text)
    if re.search(r"[\.\?]\s*", text):
        return True, text
    else:
        return False, None


def etract(text):
    pattern = r"\{(.*?)\}"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        extracted_text = "".join(match.group(1))
        if len(extracted_text) > 256:
            extracted_text = extracted_text[: -(len(extracted_text) - 255)]
        return extracted_text


def cp_str(data, num):

    value = is_question(data)
    if value[0]:

        stor_response, stor_response_error = api(value[1])
        if stor_response != "":
            vlu = etract(stor_response)
            send(num, vlu)
        else:
            send(num, str(stor_response_error))
    num = num + 1
    pyperclip.copy("")


def is_image(data, num):
    send("crackexam", "started")
    data.save("R", "jpg")
    api_url = "https://api.api-ninjas.com/v1/imagetotext"

    image_file_descriptor = open("R.jpg", "rb")
    files = {"image": image_file_descriptor}
    headers = {
        "X-Api-Key": "yZ6uvRhVlOBUIxXvgIJh8w==rpiwYJUGQzyAixjt"
    }  # Replace with your actual API key
    r = requests.post(api_url, files=files, headers=headers)

    text_values = [item["text"] for item in r.json()]
    cp_str(" ".join(text_values), num)


def api(questionandchoices):
    stor_response_error = ""
    stor_response = ""

    try:
        message = (
            "context = {answer:'',expanlination:''},question and choices:'"
            + questionandchoices
            + "'getAnswer:true and getExplaination:true in form of context"
        )

        response = chat.send_message(message)
        stor_response = response.text
    except Exception as e:
        stor_response_error = f"something went wrong : {e}"

    return stor_response, stor_response_error


def main():
    num = 1
    send(
        " warring : you have 15 second notification to be cleared",
        "crackexam.py is stared",
    )
    ti = time.time()
    duration = 3 * 60 * 60
    counter = 0

    while time.time() - ti < duration:

        if isinstance(pyperclip.paste(), str) and len(pyperclip.paste()) > 0:
            cp_str(pyperclip.paste(), num)
        elif ImageGrab.grabclipboard() != None:
            is_image(ImageGrab.grabclipboard(), num)
        elif (
            isinstance(pyperclip.paste(), str)
            and len(pyperclip.paste()) > 0
            and ImageGrab.grabclipboard() != None
        ):
            print(
                "both are there............"
            )  ## both are there...............................
        print("wating ... ", counter)
        counter += 1
        time.sleep(1)


main()

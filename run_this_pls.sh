#!/bin/bash

 sudo apt update
pip install pyttsx3
sudo apt install espeak
sudo apt install python3-pyaudio
sudo apt-get install alsa-utils
sudo apt install pulseaudio-equalizer
python3 dominik_message.py
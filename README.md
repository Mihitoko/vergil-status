# <img src="extension/public/icons/icon_48.png" width="45" align="left"> Vergil Status

This extension summons Vergil everytime you are horny and want to watch porn.

## Features

- It uses a Machine Learning model to detect horny videos and prevents you from being horny by summoning Vergil

## Install

- Go to the release tab
- Download the zip and extract it 
- Start the server/main.exe
- Go into Chrome extensions and enable developer mode, press load unpacked and choose the path to /extension/
- Done


## Development

### Setup
- Clone repository
- Install the python requirements with `pip install -r requirements.txt` (venv setup recommended)
- Install node packages with `npm install`

### Commands
|        Command         |                      Description                       |
|:----------------------:|:------------------------------------------------------:|
|    `npm run watch`     |        Build extension and watches for changes         |
|    `npm run build`     |          Builds the extension for production           |
|    `npm run format`    |                   Format the js code                   |
| `npm run build_server` | Builds the server into an executable using pyinstaller |


## Contribution

- Suggestions and pull requests are welcomed!.

## Thanks
This fun little project was made possible because of the people at [nsfw_model](https://github.com/GantMan/nsfw_model).  
They serve a pre-trained classifier model which is free to use ❤️


---

This project was bootstrapped with [Chrome Extension CLI](https://github.com/dutiyesh/chrome-extension-cli)


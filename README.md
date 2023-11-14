# QR Code Generator (QRGen)

<img src="img/logo.png" width="200" height="200">

QRGen is a simple desktop application to generate and save QR codes. It's built with Python, using the tkinter and customtkinter libraries for the graphical user interface, and qrcode for generating QR codes.

## Features

- Generate QR codes from user input.
- Save QR codes as PNG files.
- Simple and minimalistic interface.
> To view what is encoded in the QR Code, point your phone camera to the QR Code.

## Prerequisites

Before running the application, ensure you have Python installed on your system. You also need to install the following Python libraries:

- PIL (Pillow)
- qrcode
- customtkinter

You can install these packages using pip or pip3 on mac:

```
pip install Pillow qrcode customtkinter
```

## Running the Application

To run the application, follow these steps:

1. Ensure you have Python and the required libraries installed.
2. Save the provided Python script to a file, for example, qrgen.py.
3. Run the script from your command line:

```
python qrgen.py
```    

The application window will open. Enter the text you want to convert into a QR code.

Click the **Save QR** button to save the generated QR code as a PNG file.

## Notes
Ensure the script qrgen.py and its resources (like images) are in the same directory, or adjust the paths in the script accordingly.
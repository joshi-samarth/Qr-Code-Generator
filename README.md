# Qr-Code-Generator
 <b>Created by samarth joshi</b> <br>
 
1. Importing Necessary Libraries : The script begins by importing the required libraries. 
   - `tkinter` is imported for creating the graphical user interface (GUI).
   - `qrcode` is imported for generating QR codes.
   - `PIL` (Python Imaging Library), known as `Pillow`, is imported for handling images.

2. Defining `generate_qr_code` Function: This function is defined to generate a QR code based on user input. Here's a step-by-step breakdown of what it does:
   - Getting User Input: It retrieves the text to be encoded from an entry widget.
   - Creating QR Code Object: It creates a QR code object with specific parameters such as version, box size, and border.
   - Adding Text and Generating QR Code: The function adds the user input text to the QR code object and generates the QR code.
   - Creating Image from QR Code: It creates an image from the generated QR code with specified fill and background colors.
   - Resizing Image: The image is resized to 200x200 pixels using the ANTIALIAS filter to maintain quality.
   - Saving Image: The generated image is saved as "qrcode.png".
   - Displaying Image: It creates a PhotoImage object from the image and configures the label widget to display the image.

3. Creating GUI Components: 
   - Window Object: An instance of the `Tk` class is created, representing the main window of the application. It's configured with a title and size.
   - Entry Widget: An entry widget is created to allow users to input text. It's packed with a padding of 10 pixels on the y-axis.
   - Button Widget: A button widget is created to trigger the `generate_qr_code` function when clicked. It's packed with a padding of 30 pixels on the y-axis.
   - Label Widget: A label widget is created to display the generated QR code. It's packed with a padding of 40 pixels on the y-axis.

4. Starting GUI Main Loop: The `mainloop()` method of the window object is called, which starts the GUI application and waits for user interactions.

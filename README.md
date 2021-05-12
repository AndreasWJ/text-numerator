## About
A simple Blender addon written to numerate text objects from 0 to 9.

## Usecases
Primarily intended to serve as an alternative to render 1000 images to represent an interval of numbers from 0 to 999. For example, you want a third party app to display 3D numbers in a certain range. You can by numerating numbers individually avoid hundreds of renders, and instead assemble numbers in the third party app. A three digit output looks like:
```
col1_0.png
col1_1.png
...

col2_0.png
col2_1.png
...

col3_0.png
col3_1.png
...
```
To display 999 in your app you can layer `col1_9.png`, `col2_9.png`, `col3_9.png` together.

## How to use
* Digits in Blender can be a single or multiple text objects. Therefore, you should place all objects related to a digit in the same collection.
* Collections can be named arbitrarily, however, I do recommend naming them col1, col2, col3, for the sake of simplicity.
* Select a digit's collection, navigate to its "Output Properties" in the right panel, expand "Render Numerated Text" panel.
* Enter an output directory.
* Press "Render"

## Setup
* Go to Edit->Preferences.
* Find the "Addons" tab.
* Press "Install", navigate to this repository's main.py file.
* Check Text Numerator's checkbox to activate it, in the addon list.

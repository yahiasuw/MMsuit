# MMsuit
A user-friendly web-based application for studying enzyme kinetics using Michaelis Menten equation by importing experimental data. 

# Installation
You can use **pip** to download the package from terminal
```angular2html
pip install MMsuit
```
It is best downloaded in a colab or Jupyter notebook as in the following [tutorial](https://drive.google.com/file/d/1crjh07c4tjrRlu1yZ9f-gt3eGoXYSX5U/view?usp=sharing).
```angular2html
!pip install MMsuit
```
# Initiate GUI
Run from python console or a Jupyter notebook
```angular2html
from MMsuit import MMgui
MMgui()
```
If you are running from python console you should find a message containing the following link which should initiate a browser and run the application.
```angular2html
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'MMsuit.MMapp'
 * Debug mode: on
```
You can find a usage example 
# CUI application
There is a documented tutorial for integrating MMsuit in a python script in [Tutorials](https://github.com/yahiasuw/MMsuit/blob/main/Tutorials/MMsuit_CUI_tutorial.ipynb)

*CUI is better in giving more statistics for the user*

Ram
=======
A command line sprite tool and friend of the Yak.

Includes [pypacker](http://jwezorek.com/2013/01/sprite-packing-in-python/), written by Joe Wezorek.

## Features
* Automatic support for multiple sprite resolutions (based on folder names)
* pngcrush for a low-fat diet
* Produces an HTML test page so can preview your sprites
* Python, so it's blazing fast

## Installation
Unzip the package into the root of your project, ie:

	project/
		tools/
		www/
	
	Run: chmod 777 tools/*
	
	Edit the config in `tools/config.sh` to look like your project

	Edit Line 26 of `tools/config.sh` to support your OS. Linux and Mac OSX order files differently.


## Install PIL

	Ram needs the [Python Image Library](https://developers.google.com/appengine/docs/python/images/installingPIL). 

	If you're on linux, run:
	---

	`sudo apt-get install python-imaging`


	To install PIL on Mac OS X 10.4 and higher:
	---

	* Download the PIL .dmg file. For example, you can download the PIL 1.1.6 .dmg file from http://pythonmac.org/packages/py25-fat/index.html.
	* Double-click on the installer to start the installation process.
	* Choose the correct directory.
	* Finish the installation.


## Install PNGCrush

PNGCRUSH will make your files smaller. It is good. Ram will
try to use this if it finds it installed.

[PngCrush](http://www.hmug.org/pub/MacOS_X/BSD/Applications/Graphics/pngcrush/)


## Set up your images

You'll need to drop your sprite images in a sub-folder for each pixel aspect ratio."

Eg, sprites/
	    foo/           (the 1x has no prefix. Your sprite will be called this.)
	    foo-0.75x/     (smaller than 1x for poxy androids. Use the same base-name [foo] for all these)
	    foo-1.5x/      (android pseudo-retina)
	    foo-2x/        (true retina)
	    bar/
	    bar-2x/

## Usage
Call `tools/sprites.sh` from your project root.


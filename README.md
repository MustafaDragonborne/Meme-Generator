# Meme Generator

## Overview

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

### What can it do?

The application can interact with a variety of files with complex filetypes like pdf, docx, csv and txt files using third party applications written in another programming language. These files contain the quotes with a body and an author in a specific format. It can load, manipulate and save images using third party libraries. In this application, we make use of the Pillow library to work with images. It can also accept user input through a command-line tool and a web service.

## Instructions to set up and run the program

### Command Line Interface (CLI) Tool

The CLI tool is developed inside the meme.py file and can be run on Anaconda Prompt using the command:

```python meme.py```

This command generates a random meme by taking a random image from "./_data/photos/dog/" and a random quote from "./_data/DogQuotes/" and overlays the quote on the image.
Furthermore, it can take in three optional arguments. These are --body, --author and --path which correspond to a user-specified quote body, quote author and image path.
For example, if the original image path intended by the user is "./_data/photos/dog/xander_1.jpg", the quote body is "My Quote Body" and the quote author is "My Quote Author", then meme.py can be run on the command line using the following command:

```python meme.py --body "My Quote Body" --author "My Quote Author" --path "./_data/photos/dog/xander_1.jpg"```

If the --body argument is specified, then an --author argument has to be specified too, otherwise an Exception is raised.

The CLI interface returns the path of the new manipulated image. 

### Flask App
A basic flask server is designed in app.py that will consume the modules and make them usable through a web interface. This enables the user to generate memes through the web browser. In order to setup the server on a machine running Windows, use the following commands on the command line:

```set FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload```

The server allows the user to generate memes using two options:
- Generate memes using random images in "./_data/photos/dog/" and random quotes in "./_data/DogQuotes/"
- Generate memes using custom user-specific image URLs from the internet, a quote body and a quote author.

## Custom Modules and Libraries used

QuoteEngine
MemeEngine

## Python standard libraries used

os
random
ArgParse
requests
Flask
Pillow
numpy
pandas
typing
python-docx
subprocess

## QuoteEngine

The QuoteEngine library contains all the modules and submodules required to ingest and parse a variety of files that contain quotes with complex filetypes like pdf, docx, csv and txt files using third party applications written in another programming language. It is a highly modular library designed using advanced Object-Oriented modelling techniques such as making use of Abstract Base Classes and Strategy Objects. 

The QuoteModel module implements the QuoteModel class to encapsulate the body and the author of a particular quote from a file

The IngestorInterface.py module implements an Abstract base class that can check if a particular file type can be imported by an Importer or not and parse them. Separate strategy objects realize the IngestorInterface abstract base class. These strategy objects are defined in:
- csvIngestor.py 
	Subclass of IngestorInterface. Checks if the file extension is csv and parses csv files containing quotes.
- docxIngestor.py 
	Subclass of IngestorInterface. Checks if the file extension is docs and parses docx files containing quotes.
- txtIngestor.py 
	Subclass of IngestorInterface. Checks if the file extension is txt and parses txt files containing quotes.
- pdfIngestor.py 
	Subclass of IngestorInterface. Checks if the file extension is pdf and parses pdf files containing quotes. This module parses the pdf files using the pdftotext function of Xpdf. Xpdf is called as a subprocess.

All of these strategy objects are encapsulated within the Ingestor.py module. This module implements the Ingestor class which is also a sublcass of IngestorInterface. It implements all the different Ingestors together, thus enabling multiple file types to be parsed simultaneously and a list of QuoteModel objects to be created.

## MemeEngine
The MemeEngine module is responsible for manipulating and drawing text onto images using the Pillow library. It implements the MemeEngine class which is called by meme.py and app.py.



























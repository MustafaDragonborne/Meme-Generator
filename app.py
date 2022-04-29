"""Implement a basic flask server to generate memes through a web interface."""

import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


# %%
def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the quote_files variable
    quotes = []
    for path in quote_files:
        quotes_list = Ingestor.parse(path)
        for q in quotes_list:
            quotes.append(q)

    images_path = "./_data/photos/dog/"

    # Find all images within the images_path directory
    imgs = [images_path + img for img in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


# %%
@app.route('/')
def meme_rand():
    """Generate a random meme.

    The random meme is generated by selecting a random image and random quote
    from the imgs and quotes array respectively.
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author, width=500)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    path_tmp_image = './tmp/mytempIMG.jpg'

    image_url = request.form['image_url']
    print(image_url)
    img_content = requests.get(image_url, stream=True).content
    with open(path_tmp_image, 'wb') as f:
        f.write(img_content)

    body = request.form['body']
    author = request.form['author']

    path = meme.make_meme(path_tmp_image, body, author, width=200)
    print(path)
    os.remove(path_tmp_image)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

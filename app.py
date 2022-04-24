import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')

#%%
def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for path in quote_files:
        quotes_list = Ingestor.parse(path)
        for q in quotes_list:
            quotes.append(q)

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    
    imgs = [images_path + img for img in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()

#%%
@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author, width=500)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path_tmp_image = './tmp/mytempIMG.jpg'
    
    # with app.test_request_context():
    #      image_url = request.form['Image URL']   
        
    image_url = request.form['image_url']
    # image_url = 'https://cdn.gettotext.com/deutsch/wp-content/uploads/2021/09/Wie-Jiraiya-in-Naruto-Shippuden-stirbt-und-welche-Episode-es.jpg'
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

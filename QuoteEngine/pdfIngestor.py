"""Strategy Object to parse pdf files."""

from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class pdfIngestor(IngestorInterface):
    """Strategy Object to parse pdf files.

    pdfIngestor is a subclass of the IngestorInterface abstract base class and
    implements a single parse method to create a list of QuoteModel objects
    given a pdf file containing a quote and an author. The parse method
    firstly checks if the file has a .pdf extension and raises an Exception
    otherwise.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse pdf file to create list of QuoteModel objects.

        Given a path to a pdf file, the method firstly checks if the file has a
        .pdf extension and raises an Exception otherwise.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        with open(tmp, "r") as f:
            quotes = []
            file_contents = f.read().split('"')[1::]
            for i, cont in enumerate(file_contents):
                if i % 2 == 0:
                    file_contents[i] = file_contents[i] + file_contents[i+1]
                    body, author = file_contents[i].split(' - ')
                    author = author.strip('\n\n\x0c')
                    quote = QuoteModel(body, author)
                    quotes.append(quote)

        os.remove(tmp)
        return quotes

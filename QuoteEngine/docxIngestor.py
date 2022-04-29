"""Strategy Object to parse docx files."""

import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class docxIngestor(IngestorInterface):
    """Strategy Object to parse docx files.

    docxIngestor is a subclass of the IngestorInterface abstract base class and
    implements a single parse method to create a list of QuoteModel objects
    given a docx file containing a quote and an author. The parse method
    firstly checks if the file has a .docx extension and raises an Exception
    otherwise.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx file to create list of QuoteModel objects.

        Given a path to a docx file, the method firstly checks if the file has
        a .docx extension and raises an Exception otherwise.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split(' - ')  # list containing the body as
                # the first element and author and the second element
                body = parse[0]
                author = parse[1]
                quote = QuoteModel(body, author)
                quotes.append(quote)

        return quotes

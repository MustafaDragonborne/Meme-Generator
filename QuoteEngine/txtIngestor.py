"""Strategy Object to parse txt files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class txtIngestor(IngestorInterface):
    """Strategy Object to parse txt files.

    txtIngestor is a subclass of the IngestorInterface abstract base class and
    implements a single parse method to create a list of QuoteModel objects
    given a txt file containing a quote and an author. The parse method
    firstly checks if the file has a .txt extension and raises an Exception
    otherwise.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file to create list of QuoteModel objects.

        Given a path to a txt file, the method firstly checks if the file has a
        .txt extension and raises an Exception otherwise.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as f:
            file_contents = f.read()
            lines = file_contents.splitlines()
            for line in lines:
                body, author = line.split(' - ')
                quote = QuoteModel(body, author)
                quotes.append(quote)

        return quotes

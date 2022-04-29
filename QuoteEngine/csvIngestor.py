"""Strategy Object to parse csv files."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class csvIngestor(IngestorInterface):
    """Strategy Object to parse csv files.

    csvIngestor is a subclass of the IngestorInterface abstract base class and
    implements a single parse method to create a list of QuoteModel objects
    given a csv file containing a quote and an author. The parse method
    firstly checks if the file has a .csv extension and raises an Exception
    otherwise.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv file to create list of QuoteModel objects.

        Given a path to a csv file, the method firstly checks if the file has a
        .csv extension and raises an Exception otherwise.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        df = pd.read_csv(path)
        return [QuoteModel(body, author) for body, author in
                zip(df['body'], df['author'])]

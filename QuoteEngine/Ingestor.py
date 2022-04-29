"""Subclass of IngestorInterface abstract base class to parse a file."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .docxIngestor import docxIngestor
from .csvIngestor import csvIngestor
from .pdfIngestor import pdfIngestor
from .txtIngestor import txtIngestor


class Ingestor(IngestorInterface):
    """Subclass of IngestorInterface abstract base class to parse a file.

    This class realizes the IngestorInterface abstract base class and
    encapsulates the helper classes namely docxIngestor, csvIngestor etc.
    """

    ingestors = [docxIngestor, csvIngestor, pdfIngestor, txtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of QuoteModel objects.

        This class method takes in the path of a file which needs to be
        ingested and parses it to create a list of QuoteModel objects from
        its contents.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

"""Abstract Base Class that can check file extensions and parse files."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract Base Class that can check file extensions and parse files.

    This class is an abstract base class with a single abstract method for
    importing files and producing a list of QuoteModel objects. This class is
    realized by the different Strategy Objects (Ingestor classes) that inherit
    from this class and implement the abstract method, thus effectively
    creating a link between them.

    Moreover, it implements a class method "can_ingest" which decides if a file
    is compatible with the importer or not.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file can be ingested by Importer or not.

        This class method is called by the parse method. It takes in the path
        of a file which needs to be ingested and checks if the file can be
        ingested by the Importer or not.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take a file and return a list of QuoteModel objects.

        This class method takes in the path of a file which needs to be
        ingested and parses it to create a list of QuoteModel objects from
        its contents.
        """
        pass

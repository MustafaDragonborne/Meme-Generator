# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:42:38 2022

@author: MARS
"""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    ''' This class is an abstract base class with a single abstract method for 
    importing files and producing a list of QuoteModel objects. This class is 
    realized by the different Strategy Objects (Ingestor classes) that inherit 
    from this class and implement the abstract method, thus effectively 
    creating a link between them.
    
    Moreover, it implements a class method "can_ingest" which decides if a file
    is compatible with the importer.
    '''
    
    allowed_extensions = []
    
    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
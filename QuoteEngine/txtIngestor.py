# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:31:57 2022

@author: MARS
"""

# import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class txtIngestor(IngestorInterface):
    allowed_extensions = ['txt']
    
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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

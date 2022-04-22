# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:30:45 2022

@author: MARS
"""

import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class docxIngestor(IngestorInterface):
    allowed_extensions = ['docx']
    
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
            
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split(' - ')  # list containing the body as the
                # first element and author and the second element
                body = parse[0]
                author = parse[1]            
                quote = QuoteModel(body, author)
                quotes.append(quote)
        
        return quotes
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:31:02 2022

@author: MARS
"""

from typing import List
import subprocess
import os 
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class pdfIngestor(IngestorInterface):
    allowed_extensions = ['pdf']
    
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
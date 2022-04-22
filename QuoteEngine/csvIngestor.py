# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:30:52 2022

@author: MARS
"""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class csvIngestor(IngestorInterface):
    allowed_extensions = ['csv']
    
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        
        df = pd.read_csv(path)
        return [QuoteModel(body, author) for body, author in zip(df['body'], df['author'])]

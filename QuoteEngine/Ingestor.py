# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:49:00 2022

@author: MARS
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .docxIngestor import docxIngestor
from .csvIngestor import csvIngestor
from .pdfIngestor import pdfIngestor
from .txtIngestor import txtIngestor

class Ingestor(IngestorInterface):
    ingestors = [docxIngestor, csvIngestor, pdfIngestor, txtIngestor]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
    
"""Class to encapsulate the body and the author."""


class QuoteModel():
    """Class to encapsulate the body and the author.

    Consists of just the constructor method and __repr__ method.
    """

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent the class as a string when it is printed."""
        return f'<{self.body} -- {self.author}>'

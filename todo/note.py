class Note:

    def __init__(self, memo):
        self.message = memo

    @property
    def note(self):
        return self.message

    @note.setter
    def note(self, new_memo):
        self.message= new_memo

    def __repr__(self):
        return f'{self.message}'

    def __str__(self):
        return f'{self.message}'

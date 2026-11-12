class Libro:
    def __init__(self, titolo, autore, anno, editore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def reading_time(self):
        if self.pagine < 100:
            return "1 ora"
        if self.pagine <= 200:
            return "2 ore"
        return "più di 2 ore"

    def __str__(self):
        return f"{self.titolo} - {self.autore} ({self.anno}), {self.pagine} pagine"


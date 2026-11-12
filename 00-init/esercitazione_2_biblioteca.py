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


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []

    def aggiungi_libro(self, libro: Libro) -> None:
        self.libri.append(libro)

    def cerca_per_titolo(self, testo: str):
        testo = testo.lower()
        
        for libro in self.libri:
            if testo in libro.titolo.lower():
                return libro
        return None
            
        
        
        #return [libro for libro in self.libri if testo in libro.titolo.lower()]

    def cerca_per_autore(self, autore):
        autore = autore.lower()

        libri_con_autore_uguale = []
        for libro in self.libri:
            if autore == libro.autore.lower():
                libri_con_autore_uguale.append(libro)
        return libri_con_autore_uguale

        #return [libro for libro in self.libri if autore in libro.autore.lower()]

    def conta_libri(self):
        return len(self.libri)

    def __len__(self):
        return self.conta_libri()


class Prestito:
    def __init__(self, libro, utente):
        self.libro = libro
        self.utente = utente

    def __str__(self):
        return f"{self.utente} ha preso in prestito: {self.libro.titolo}"

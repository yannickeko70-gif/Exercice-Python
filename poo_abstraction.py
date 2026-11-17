import json
from abc import ABC, abstractmethod
from typing import Protocol


#==========================
# Question 1 
#==========================
class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def crier(self):
        """Retourne le cri de l'animal."""

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et je fais : {self.crier()}")


class Chien(Animal):
    def crier(self):
        return "Wouf !"


class Chat(Animal):
    def crier(self):
        return "Miaou !"


#==========================
# Question 2
#==========================
class Stockage(ABC):
    @abstractmethod
    def sauvegarder(self, cle, valeur): ...

    @abstractmethod
    def charger(self, cle): ...


class StockageMemoire(Stockage):
    def __init__(self):
        self.__donnees = {}

    def sauvegarder(self, cle, valeur):
        self.__donnees[cle] = valeur

    def charger(self, cle):
        return self.__donnees.get(cle)


class StockageFichier(Stockage):
    def __init__(self, chemin="stockage.json"):
        self.__chemin = chemin

    def __lire(self):
        try:
            with open(self.__chemin, encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def sauvegarder(self, cle, valeur):
        donnees = self.__lire()
        donnees[cle] = valeur
        with open(self.__chemin, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)

    def charger(self, cle):
        return self.__lire().get(cle)


#==========================
# Question 3
#==========================
class Comparable(Protocol):
    def comparer(self, autre) -> int: ...


class Note:
    def __init__(self, valeur):
        self.valeur = valeur

    def comparer(self, autre):
        return (self.valeur > autre.valeur) - (self.valeur < autre.valeur)


def plus_grand(a: Comparable, b: Comparable):
    return a if a.comparer(b) >= 0 else b


#==========================
# Question 4
#==========================

# Interface : le contrat que voit le reste du site
class Payable(ABC):
    @abstractmethod
    def payer(self, montant) -> bool: ...

    @abstractmethod
    def rembourser(self, montant) -> bool: ...


# Classe abstraite : code et état communs aux moyens de paiement
class Paiement(Payable):
    def __init__(self, montant):
        self._montant = montant
        self._journal = []

    @abstractmethod
    def _valider(self) -> bool: ...        # propre à chaque moyen

    def payer(self, montant=None):         # algorithme commun
        montant = self._montant if montant is None else montant
        if montant <= 0 or not self._valider():
            self._journal.append(("refus", montant))
            return False
        self._journal.append(("paiement", montant))
        return True

    def rembourser(self, montant):
        self._journal.append(("remboursement", montant))
        return True


class MobileMoney(Paiement):
    def __init__(self, montant, numero):
        super().__init__(montant)
        self.__numero = numero

    def _valider(self):
        return len(self.__numero) == 9 and self.__numero.isdigit()


class CarteBancaire(Paiement):
    def __init__(self, montant, numero_carte):
        super().__init__(montant)
        self.__numero = numero_carte

    def _valider(self):
        return len(self.__numero) == 16 and self.__numero.isdigit()


class CashLivraison(Paiement):
    def _valider(self):
        return True

    def rembourser(self, montant):
        return False                       # pas de remboursement automatique

# Justification : l'interface Payable est le contrat unique connu du panier/de la
# commande ; on peut ajouter un moyen de paiement sans les modifier. La classe
# abstraite Paiement évite de dupliquer le montant, le journal et l'algorithme
# payer() ; seule la validation change d'un moyen à l'autre.


#==========================
# Question 5
#==========================
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.__notes = []

    def ajouter_note(self, note):
        if not 0 <= note <= 20:
            raise ValueError("La note doit être comprise entre 0 et 20")
        self.__notes.append(note)

    @property
    def moyenne(self):                     # lecture seule : pas de setter
        if not self.__notes:
            return 0.0
        return sum(self.__notes) / len(self.__notes)


# ───── Tests ─────
if __name__ == "__main__":
    Chien("Rex").se_presenter()
    Chat("Tom").se_presenter()

    for s in (StockageMemoire(), StockageFichier()):
        s.sauvegarder("langage", "Python")
        print(type(s).__name__, "->", s.charger("langage"))

    print(plus_grand(Note(12), Note(15)).valeur)          # 15

    for m in (MobileMoney(5000, "677123456"), CarteBancaire(5000, "1234567812345678"),
              CashLivraison(5000), MobileMoney(5000, "123")):
        print(type(m).__name__, m.payer())

    e = Etudiant("Amina")
    for n in (12, 15, 18):
        e.ajouter_note(n)
    print("Moyenne :", e.moyenne)                         # 15.0
    try:
        e.moyenne = 15                                    # doit lever une erreur
    except AttributeError as err:
        print("Erreur :", err)
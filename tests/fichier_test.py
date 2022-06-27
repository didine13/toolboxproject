# fichier de test à créer pour la validation des fonctions du package qui seront exécutées
# par github lors du CI/CD


import string

def test_try_me():
    assert type("toto" == string)
    print("test ok")

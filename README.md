# Algorithme-CYK

Implémentation en python de la version standard de l'algorithme de CKY (Cocke-Kasami-Younger) dans le but de reconnaître
si chaque mot est accepté ou rejeté d'après des règles de production données (rules.txt) en forme normale de Chomsky.


# Exemple

Dans le script, la phrase que je veux vérifier est : "a a a b b". Elle est contenu dans la variable <code>seq</code> qui est ma séquence de mots.
L'algorithme va alors remplir la matrice en fonction des règles satisfaites ou non par les mots contenus dans ma séquence.

![image](https://user-images.githubusercontent.com/76498479/190861480-2b007775-7449-40f7-b03f-3b6bb9af17e5.png)

Etant donné que la dernière règle satisfaite ne comporte pas l'élément de commencement S, la phrase est refusée.

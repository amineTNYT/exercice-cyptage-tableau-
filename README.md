Algorithme de Cryptage par Clé Automatique
Principe du Cryptage
Cet algorithme transforme un tableau de mots en versions cryptées en utilisant une technique de chiffrement symétrique où le premier caractère de chaque mot sert de clé pour crypter l'ensemble du mot.

Algorithme Détaillé
Entrée :
Un tableau t contenant n mots (2 ≤ n ≤ 100)

Chaque mot a une longueur entre 1 et 19 caractères

Processus de Cryptage :
Pour chaque mot t[i] dans le tableau :

Clé = premier caractère du mot (t[i][0])

Pour chaque caractère t[i][j] dans le mot :

Calculer : code = ASCII(clé) + ASCII(t[i][j])

Si code > 127 alors code = code - 127

Convertir code en caractère

Construire le mot crypté caractère par caractère

Exemple Complet
Tableau Original :
Index	Mot
0	"alerte"
1	"secours"
2	"ennemis"
3	"armes"
4	"avions"
Processus de Calcul :
1. "alerte" → "CNGTVG"

Clé = 'a' (ASCII 97)

'a' + 'a' = 97+97=194 → 194-127=67 → 'C'

'a' + 'l' = 97+108=205 → 205-127=78 → 'N'

'a' + 'e' = 97+101=198 → 198-127=71 → 'G'

'a' + 'r' = 97+114=211 → 211-127=84 → 'T'

'a' + 't' = 97+116=213 → 213-127=86 → 'V'

'a' + 'e' = 97+101=198 → 198-127=71 → 'G'

2. "secours" → "gYWcifg"

Clé = 's' (ASCII 115)

's' + 's' = 115+115=230 → 230-127=103 → 'g'

's' + 'e' = 115+101=216 → 216-127=89 → 'Y'

's' + 'c' = 115+99=214 → 214-127=87 → 'W'

etc.

Résultat Final :
text
Les messages cryptés sont :
"CNGTVG" "gYWcifg" "KTTKSOY" "CTOGU" "CXKQPU"
Caractéristiques du Cryptage
Propriétés :
✅ Longueur conservée : chaque mot crypté a même longueur que l'original

✅ Déterministe : un même mot produira toujours le même résultat crypté

✅ Clé intégrée : pas besoin de clé externe

✅ Réversible : possible de décrypter avec le même algorithme




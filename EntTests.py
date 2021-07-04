from PIL import Image
import random

dir1 = '../Images (Import here pictures)/IMG01.jpg'
dir2 = '../Images (Import here pictures)/IMG02.jpg'
dir3 = '../Images (Import here pictures)/IMG03.jpg'
dir4 = '../Images (Import here pictures)/IMG03.jpg'

im1 = Image.open(dir1)
im2 = Image.open(dir2)
im3 = Image.open(dir3)
im4 = Image.open(dir4)

L = [im1.size, im2.size, im3.size, im4.size]

LL=str(sorted(L))
LL1 = LL.replace(str(im1.size), str(dir1))
LL2 = LL1.replace(str(im2.size), str(dir2))
LL3 = LL2.replace(str(im3.size), str(dir3))
LL4 = LL3.replace(str(im4.size), str(dir4))
LL5=sorted(L)

print(LL4)
print(LL5)

print("Rédaction du texte d'intention")
nature = input("Quel est le type d'oeuvre ?")

if (nature=="film d'animation"):
    terme = "film d'animation"
    domaine = "animation"
    verbe = "animer"
    verbe2 = "dessiner"
    verbe3 = "peindre"
    verbe4 = "déplacer"
    verbe5 = "photographier"
    verbe6 = "monter"
    verbe7 = "stabiliser"
    logiciel1 = "Movie Maker"
    logiciel2 = "iMovie"
elif (nature=="collage"):
    terme = "collage"
    terme2 = "découpage"
    domaine = "collage"
    domaine2 = "découpage"
    verbe = "coller"
    verbe2 = "découper"
    verbe3 = "dessiner"
    verbe4 = "annoter"
elif (nature=="dessin"):
    terme = "dessin"
    domaine = "dessin"
    verbe = "dessiner"
    verbe2 = "colorier"
elif (nature=="coloriage"):
    terme = "coloriage"
    terme2 = "mettre en couleur"
    domaine = "coloriage"
    verbe = "colorier"
    verbe2 = "mettre en couleur"
elif (nature=="sculpture"):
    terme = "sculpture"
    terme2 = "agencement"
    terme3 = "positionnement"
    terme4 = "supperposition"
    domaine = "sculpture"
    domaine2 = "agencement"

theme = input("Quel est le thême de l'oeuvre ?")

if (theme=="tristesse"):
    det = "la"
    terme = "tristesse"
    suffixe = ["ment triste", "qui pleure", "qui se déchire", "ment blessé"]
elif (theme=="joie"):
    det = "la"
    terme = "joie"
    suffixe = [" heureuse", " rieuse"]
elif (theme=="amour"):
    det = "l'"
    terme = "amour"
    suffixe = ["amoureuse", "amoureux", "tourteraux"]
elif (theme=="colère"):
    det = "la"
    terme = "colère"
    suffixe = ["coléreux", "grincheux", "colèreuse", "grincheuse"]

titre = input("Quel est le titre de l'oeuvre ?")

suffixe1 = random.choice(suffixe)
titre_ameliore = titre, suffixe1
titre_inter = str(titre_ameliore)
titre_alpha1 = titre_inter.replace("(", "")
titre_alpha2 = titre_alpha1.replace("'", "")
titre_alpha3 = titre_alpha2.replace(")", "")
titre_alpha = titre_alpha3.replace(",", "")

if (suffixe1=="ment triste") or (suffixe1=="ment blessé"):
    titre_alpha = titre_alpha.replace("e ", "e")

support = input("Quel support a été utilisé ?")
couleur = input("Quel est la couleur principale de l'oeuvre ?")
couleur_ask = input("Y a-t-il une autre couleur ?")
if (couleur_ask=="oui"):
    couleur2 = input("Quelle est cette couleur ?")
    couleur_ask2 = input("Y a-t-il une autre couleur ?")
    if (couleur_ask2=="oui"):
        couleur2 = input("Quelle est la troisième couleur ?")
        couleur_ask3 = input("Y a-t-il une quatrième couleur ?")
        if (couleur_ask3=="oui"):
            couleur3 = input("Quelle est la quatrième couleur ?")
            couleur_ask4 = input("Y a-t-il une dernière couleur ?")
            if (couleur_ask4=="oui"):
                couleur4 = input("Quelle est la dernière couleur ?")
            else : 
                couleur5 = ""
        else :
            couleur4 = ""
            couleur5 = ""
    else :
        couleur3 = ""
        couleur4 = ""
        couleur5 = ""
else :
    couleur2 = ""
    couleur3 = ""
    couleur4 = ""
    couleur5 = ""

if (couleur=="rouge") and (theme=="tristesse"):
    couleur_intent1 = "la tristesse et le sang"
elif (couleur=="rouge") and (theme=="joie") or (couleur=="rouge") and (theme=="amour"):
    couleur_intent1 = "la chaleur"
elif (couleur=="rouge") and (theme=="colère"):
    couleur_intent1 = "la colère et en quelque sorte aussi la violence"
elif (couleur=="vert") and (theme=="tristesse") or (couleur=="verte") and (theme=="joie"):
    couleur_intent1 = "la végétation"
elif (couleur=="vert") and (theme=="colère") or (couleur=="vert") and (theme=="amour"):
    couleur_intent1 = "le dégoût"
if (couleur=="bleu") and (theme=="tristesse"):
    couleur_intent1 = "le froid"
elif (couleur=="bleu") and (theme=="joie"):
    couleur_intent1 = "la beauté de l'eau"
elif (couleur=="bleu") and (theme=="colère") or (couleur=="bleu") and (theme=="amour"):
    couleur_intent1 = "le froid"
if (couleur=="rose") and (theme=="tristesse"):
    couleur_intent1 = "les souvenirs d'avant"
elif (couleur=="rose") and (theme=="joie") or (couleur=="rose") and (theme=="amour"):
    couleur_intent1 = "l'amour"
elif (couleur=="rose") and (theme=="colère"):
    couleur_intent1 = "le froid"
elif (couleur=="jaune"):
    couleur_intent1 = "la joie et les blagues"

if (couleur2=="rouge") and (theme=="tristesse"):
    couleur_intent2 = "la tristesse et le sang"
elif (couleur2=="rouge") and (theme=="joie") or (couleur2=="rouge") and (theme=="amour"):
    couleur_intent2 = "la chaleur"
elif (couleur2=="rouge") and (theme=="colère"):
    couleur_intent2 = "la colère et en quelque sorte aussi la violence"
elif (couleur2=="vert") and (theme=="tristesse") or (couleur2=="verte") and (theme=="joie"):
    couleur_intent2 = "la végétation"
elif (couleur2=="vert") and (theme=="colère") or (couleur2=="vert") and (theme=="amour"):
    couleur_intent2 = "le dégoût"
elif (couleur2=="bleu") and (theme=="tristesse"):
    couleur_intent2 = "le froid"
elif (couleur2=="bleu") and (theme=="joie"):
    couleur_intent2 = "la beauté de l'eau"
elif (couleur2=="bleu") and (theme=="colère") or (couleur2=="bleu") and (theme=="amour"):
    couleur_intent2 = "le froid"
elif (couleur2=="rose") and (theme=="tristesse"):
    couleur_intent2 = "les souvenirs d'avant"
elif (couleur2=="rose") and (theme=="joie") or (couleur2=="rose") and (theme=="amour"):
    couleur_intent2 = "l'amour"
elif (couleur2=="rose") and (theme=="colère"):
    couleur_intent1 = "le froid"
elif (couleur2=="jaune"):
    couleur_intent2 = "la joie et les blagues"
else :
    couleur_intent2 = ""

if (couleur3=="rouge") and (theme=="tristesse"):
    couleur_intent3 = "la tristesse et le sang"
elif (couleur3=="rouge") and (theme=="joie") or (couleur3=="rouge") and (theme=="amour"):
    couleur_intent3 = "la chaleur"
elif (couleur3=="rouge") and (theme=="colère"):
    couleur_intent3 = "la colère et en quelque sorte aussi la violence"
elif (couleur3=="vert") and (theme=="tristesse") or (couleur3=="verte") and (theme=="joie"):
    couleur_intent3 = "la végétation"
elif (couleur3=="vert") and (theme=="colère") or (couleur3=="vert") and (theme=="amour"):
    couleur_intent3 = "le dégoût"
elif (couleur3=="bleu") and (theme=="tristesse"):
    couleur_intent3 = "le froid"
elif (couleur3=="bleu") and (theme=="joie"):
    couleur_intent3 = "la beauté de l'eau"
elif (couleur3=="bleu") and (theme=="colère") or (couleur3=="bleu") and (theme=="amour"):
    couleur_intent3 = "le froid"
elif (couleur3=="rose") and (theme=="tristesse"):
    couleur_intent3 = "les souvenirs d'avant"
elif (couleur3=="rose") and (theme=="joie") or (couleur3=="rose") and (theme=="amour"):
    couleur_intent3 = "l'amour"
elif (couleur3=="rose") and (theme=="colère"):
    couleur_intent3 = "le froid"
elif (couleur=="jaune"):
    couleur_intent3 = "la joie et les blagues"
else :
    couleur_intent3 = ""

if (couleur4=="rouge") and (theme=="tristesse"):
    couleur_intent4 = "la tristesse et le sang"
elif (couleur4=="rouge") and (theme=="joie") or (couleur4=="rouge") and (theme=="amour"):
    couleur_intent4 = "la chaleur"
elif (couleur4=="rouge") and (theme=="colère"):
    couleur_intent4 = "la colère et en quelque sorte aussi la violence"
elif (couleur4=="vert") and (theme=="tristesse") or (couleur4=="verte") and (theme=="joie"):
    couleur_intent4 = "la végétation"
elif (couleur4=="vert") and (theme=="colère") or (couleur4=="vert") and (theme=="amour"):
    couleur_intent4 = "le dégoût"
elif (couleur4=="bleu") and (theme=="tristesse"):
    couleur_intent4 = "le froid"
elif (couleur4=="bleu") and (theme=="joie"):
    couleur_intent4 = "la beauté de l'eau"
elif (couleur4=="bleu") and (theme=="colère") or (couleur4=="bleu") and (theme=="amour"):
    couleur_intent4 = "le froid"
elif (couleur4=="rose") and (theme=="tristesse"):
    couleur_intent4 = "les souvenirs d'avant"
elif (couleur4=="rose") and (theme=="joie") or (couleur4=="rose") and (theme=="amour"):
    couleur_intent4 = "l'amour"
elif (couleur4=="rose") and (theme=="colère"):
    couleur_intent4 = "le froid"
elif (couleur4=="jaune"):
    couleur_intent4 = "la joie et les blagues"
else :
    couleur_intent4 = ""

if (couleur5=="rouge") and (theme=="tristesse"):
    couleur_intent5 = "la tristesse et le sang"
elif (couleur5=="rouge") and (theme=="joie") or (couleur5=="rouge") and (theme=="amour"):
    couleur_intent5 = "la chaleur"
elif (couleur5=="rouge") and (theme=="colère"):
    couleur_intent5 = "la colère et en quelque sorte aussi la violence"
elif (couleur5=="vert") and (theme=="tristesse") or (couleur5=="verte") and (theme=="joie"):
    couleur_intent5 = "la végétation"
elif (couleur5=="vert") and (theme=="colère") or (couleur5=="vert") and (theme=="amour"):
    couleur_intent5 = "le dégoût"
if (couleur5=="bleu") and (theme=="tristesse"):
    couleur_intent5 = "le froid"
elif (couleur5=="bleu") and (theme=="joie"):
    couleur_intent5 = "la beauté de l'eau"
elif (couleur5=="bleu") and (theme=="colère") or (couleur5=="bleu") and (theme=="amour"):
    couleur_intent5 = "le froid"
if (couleur5=="rose") and (theme=="tristesse"):
    couleur_intent5 = "les souvenirs d'avant"
elif (couleur5=="rose") and (theme=="joie") or (couleur5=="rose") and (theme=="amour"):
    couleur_intent5 = "l'amour"
elif (couleur5=="rose") and (theme=="colère"):
    couleur_intent5 = "le froid"
elif (couleur5=="jaune"):
    couleur_intent5 = "la joie et les blagues"
else :
    couleur_intent5 = ""

materiel = input("Quel a été le matériel nécessaire (un seul) ?")
if (materiel=="colle"):
    verbe1 = "coller"
elif (materiel=="ciseaux"):
    verbe1 = "découper"
elif (materiel=="feutres") or (materiel=="crayons") or (materiel=="crayons de couleurs") or (materiel=="pastels") or (materiel=="craies"):
    verbe1 = "colorier"
elif (materiel=="crayon de papier"):
    verbe1 = "dessiner"
elif (materiel=="peinture"):
    verbe1 = "peindre"

materiel2 = input("Quel a été le deuxième matériel nécessaire ?")
if (materiel2=="colle"):
    verbe2 = "coller"
elif (materiel2=="ciseaux"):
    verbe2 = "découper"
elif (materiel2=="feutres") or (materiel=="crayons") or (materiel=="crayons de couleurs") or (materiel=="pastels") or (materiel=="craies"):
    verbe2 = "colorier"
elif (materiel2=="crayon de papier"):
    verbe2 = "dessiner"
elif (materiel2=="peinture"):
    verbe2 = "peindre"

materiel3 = input("Quel a été le troisième matériel nécessaire ? (optionnel)")
if (materiel3=="colle"):
    verbe3 = "coller"
elif (materiel3=="ciseaux"):
    verbe3 = "découper"
elif (materiel3=="feutres") or (materiel=="crayons") or (materiel=="crayons de couleurs") or (materiel=="pastels") or (materiel=="craies"):
    verbe3 = "colorier"
elif (materiel3=="crayon de papier"):
    verbe3 = "dessiner"
elif (materiel3=="peinture"):
    verbe3 = "peindre"
else :
    verbe3 = ""

if (verbe1=="découper"):
    destination = input("Pour découper quoi ?")
elif (verbe2=="découper"):
    destination2 = input("Pour découper quoi ?")
elif (verbe3=="découper"):
    destination3 = input("Pour découper quoi ?")

if (verbe1=="coller"):
    destination = input("Pour coller quoi ?")
elif (verbe2=="coller"):
    destination2 = input("Pour coller quoi ?")
elif (verbe3=="coller"):
    destination3 = input("Pour coller quoi ?")

if (verbe1=="colorier"):
    destination = input("Pour colorier quoi ?")
elif (verbe2=="colorier"):
    destination2 = input("Pour colorier quoi ?")
elif (verbe3=="colorier"):
    destination3 = input("Pour colorier quoi ?")

if (verbe1=="peindre"):
    destination = input("Pour peindre quoi ?")
elif (verbe2=="peindre"):
    destination2 = input("Pour peindre quoi ?")
elif (verbe3=="peindre"):
    destination3 = input("Pour peindre quoi ?")

if (verbe1=="dessiner"):
    destination = input("Pour dessiner quoi ?")
elif (verbe2=="dessiner"):
    destination2 = input("Pour dessiner quoi ?")
elif (verbe3=="dessiner"):
    destination3 = input("Pour dessiner quoi ?")

difficulté = input("Quelle a été la principale difficulté ?")
titre_raison = input("Pourquoi ce titre ?")

redac1 = "Pour réaliser ce ", nature, "nous avons eu besoin de ", materiel, materiel2, "et de ", materiel3,". Nous avons utilisé ", support, "comme support", ". Nous avons commencé par ", verbe1, destination, "puis par ", verbe2, destination2, "et enfin nous avons ", verbe3, destination3, ". Nous avons choisi la couleur", couleur, "afin de symboliser", couleur_intent1, ". La principale difficulté a été de", difficulté, "Enfin, nous avons choisi le titre ", titre_alpha, "car", titre_raison, "." 
redac_inter = str(redac1)
redac2 = redac_inter.replace("(", "")
redac3 = redac2.replace("'", "")
redac4 = redac3.replace(")", "")
redac = redac4.replace(",", "")


from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties
from odf.text import H, P, Span

textdoc = OpenDocumentText()
# Styles
s = textdoc.styles
h1style = Style(name="Heading 1", family="paragraph")
h1style.addElement(TextProperties(attributes={'fontsize':"24pt",'fontweight':"bold" }))
s.addElement(h1style)
# An automatic style
boldstyle = Style(name="Bold", family="text")
boldprop = TextProperties(fontweight="bold")
boldstyle.addElement(boldprop)
textdoc.automaticstyles.addElement(boldstyle)
# Text
h=H(outlinelevel=1, stylename=h1style, text=str(titre_alpha))
textdoc.text.addElement(h)
p = P(text=nature)
p.addText("\t")
textdoc.text.addElement(p)
boldpart = Span(stylename=boldstyle, text=theme)
p.addElement(boldpart)
p.addText("\t")
textdoc.text.addElement(p)
p.addText(redac)
textdoc.text.addElement(p)
textdoc.save("fiche_info.odt")
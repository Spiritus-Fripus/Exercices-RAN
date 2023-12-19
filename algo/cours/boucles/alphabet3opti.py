text = "Chers étudiants de la classe RAN2,Aujourd'hui, nous voulons vous rappeler à quel point vous êtes exceptionnels. Vous avez entrepris un voyage passionnant vers le monde de la programmation, et vous avez déjà parcouru une grande partie du chemin. Les défis qui se présentent à vous peuvent sembler intimidants, mais n'oubliez jamais que vous avez le pouvoir de les surmonter.La programmation n'est pas seulement un ensemble de compétences techniques, c'est une forme d'art. Chaque ligne de code que vous écrivez est une œuvre d'art en soi, une expression de votre créativité et de votre ingéniosité. Vous avez le potentiel de créer des applications, des sites Web et des logiciels qui changeront le monde.N'ayez pas peur des erreurs, car ce sont les erreurs qui vous font grandir. Chaque bug que vous corrigez, chaque problème que vous résolvez, vous rapproche de la maîtrise de cette discipline complexe. Les difficultés ne sont que des opportunités déguisées pour apprendre et grandir.N'oubliez pas non plus que vous n'êtes pas seuls dans cette aventure. Votre classe est une équipe, une communauté de personnes partageant la même passion et les mêmes défis. En travaillant ensemble, en partageant vos connaissances et en vous soutenant mutuellement, vous pouvez accomplir des choses incroyables.Vous avez choisi un chemin exigeant, mais aussi incroyablement gratifiant. Vous êtes les créateurs de demain, les constructeurs du futur. Ne perdez jamais de vue vos rêves et vos aspirations. Continuez à travailler dur, à rester curieux et à repousser vos limites.Nous croyons en vous, et nous sommes impatients de voir les merveilles que vous créerez. Alors, en avant, développeurs RAN2 ! Le monde a besoin de votre talent, de votre passion et de votre détermination. Vous êtes capables de tout, et nous sommes fiers de vous accompagner dans cette aventure extraordinaire.Bon courage, et que le code soit avec vous !Avec tout notre soutien, l'équipe MNS."

text=text.lower().replace(" ","")
cpt_max = 0
letter_max = ""
deja_vue = []
for i in range(0,len(text)):
    if text[i] not in deja_vue:
        cpt=0
        for j in range(0,len(text)):
            if text[i] == text[j]:
                cpt+=1
        if cpt > cpt_max:
            cpt_max=cpt
            letter_max = text[i]
        deja_vue = deja_vue +[text[i]]

print(f"\nle caractère qui revient le souvent est {letter_max} avec {cpt_max} occurences.\n")

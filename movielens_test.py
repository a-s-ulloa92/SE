# -*- coding: cp1252 -*-
import recommendations

#Importa MovieLens
prefs = recommendations.loadMovieLens()

#Se generan ratings para 2 personas diferentes
prefs["user1"]={
"Toy Story (1995)":5.0,
"GoldenEye (1995)":5.0,
"Four Rooms (1995)":3.0,
"Get Shorty (1995)":3.5,
"Copycat (1995)":3.5,
"Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)":3.0,
"Twelve Monkeys (1995)":3.0,
"Babe (1995)":4.0,
"Dead Man Walking (1995)":3.5,
"Richard III (1995)":4.0,
"Seven (Se7en) (1995)":3.0,
"Usual Suspects, The (1995)":3.5,
"Mighty Aphrodite (1995)":3.0,
"Postino, Il (1994)":3.0,
"Mr. Holland's Opus (1995)":3.5,
"French Twist (Gazon maudit) (1995)":3.5,
"From Dusk Till Dawn (1996)":3.0,
"White Balloon, The (1995)":3.5,
"Antonia's Line (1995)":4.0,
"Angels and Insects (1995)":3.5
}


prefs["user2"]={
"Toy Story (1995)":4.5,
"Muppet Treasure Island (1996)":4.0,
"Forrest Gump (1994)":3.0,
"Lion King, The (1994)":5.0,
"Nightmare Before Christmas, The (1993)":3.5,
"All Dogs Go to Heaven 2 (1996)":4.0,
"Akira (1988)":3.0,
"Babe (1995)":3.5,
"Lost World: Jurassic Park, The (1997)":4.0,
"Men in Black (1997)":4.0,
"Titanic (1997)":3.5,
"Super Mario Bros. (1993)":2.5,
"Balto (1995)":5.0,
"Fox and the Hound, The (1981)":4.5,
"George of the Jungle (1997)":4.0,
"Mary Poppins (1964)":3.5
}

def userRec(user):
    """
    Regresa las recomendaciones para "user", basándose en la información de
    MovieLens guardada en prefs
    """
    return recommendations.getRecommendations(prefs, user)[0:20]
    

print "Recomendaciones para el primer usuario: "
print userRec("user1")

print "\nRecomendaciones para el segundo usuario: "
print userRec("user2")

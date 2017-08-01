#  1 = no damage, 1.5 = 1/4 damage, 2 = 1/2 damage, 3 = neutral damage, 4 = 2x damage, 4.5 = 4x damage
from math import sqrt
from tkinter import *
from tkinter import ttk

Pokemon = {"Rattata": {"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		    "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Raticate": {"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		     "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		     "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Meowth": {"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		   "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		   "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Persian": {"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		    "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Lickitung": {"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		      "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		      "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Chansey":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		   "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		   "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Kangaskhan":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		      "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		      "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Tauros":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		  "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		  "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Ditto":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		 "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		 "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Eevee":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		 "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		 "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Porygon":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		   "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		   "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Snorlax":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		   "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		   "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},

#NORMAL/FLYING
"Pidgey":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		  "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		  "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Pidgeotto":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
			 "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
			 "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Pidgeot":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		   "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		   "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Spearow":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		   "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		   "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Fearow":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		  "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		  "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Farfetch'd":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		      "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
			  "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Doduo":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		 "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		 "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
"Dodrio":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
		  "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 1,
		  "Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},

#NORMAL/FAIRY
"Jigglypuff":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			  "Poison": 4, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 3, "Ghost": 1,
			  "Dragon": 1, "Dark": 2, "Steel": 4, "Fairy": 3},
"Wigglytuff":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			  "Poison": 4, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 3, "Ghost": 1,
			  "Dragon": 1, "Dark": 2, "Steel": 4, "Fairy": 3},
#____________________________________________________________________________________________________
#FIRE
#			:{"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
#			    "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},

		   "Charmander": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			              "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				          "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
           "Charmeleon": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			              "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				          "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Vulpix": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			              "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				          "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Ninetales": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			              "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				          "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Growlithe": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			             "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				         "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Arcanine": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			            "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				        "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Ponyta": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			          "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				      "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Rapidash": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			            "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				        "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Magmar": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			          "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				      "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Flareon": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 3,
			           "Poison": 3, "Ground": 4, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				       "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
#FIRE/FLYING
		   "Charizard": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 4, "Grass": 1.5, "Ice": 3, "Fighting": 2,
			             "Poison": 3, "Ground": 1, "Flying": 3, "Psychic": 3, "Bug": 1.5, "Rock": 4.5, "Ghost": 3,
				         "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Moltres": {"Normal": 3, "Fire": 2, "Water": 4, "Electric": 4, "Grass": 1.5, "Ice": 3, "Fighting": 2,
			           "Poison": 3, "Ground": 1, "Flying": 3, "Psychic": 3, "Bug": 1.5, "Rock": 4.5, "Ghost": 3,
				       "Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
#____________________________________________________________________________________________________
#WATER
#			"":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
#			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Squirtle":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Wartortle": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Blastoise": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Psyduck": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Golduck": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Poliwag": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Poliwhirl":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Seel": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Shellder": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Krabby": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Kingler": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Horsea":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Seadra": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Goldeen": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Seaking": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Staryu": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Magikarp": {"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
		   "Vaporeon":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
#WATER/FIGHTING
		   "Poliwraph":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 4},
#WATER/POISON
		   "Tentacool":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 3, "Ice": 2, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
		   "Tentacruel":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 3, "Ice": 2, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 2},
#WATER/PSYCHIC
		   "Slowpoke":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel": 2, "Fairy": 3},
		   "Slowbro":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel": 2, "Fairy": 3},
		   "Starmie":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 2, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel": 2, "Fairy": 3},
#WATER/ICE
		   "Dewgong":{"Normal": 3, "Fire": 3, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 1.5, "Fighting": 4,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
		   "Cloyster":{"Normal": 3, "Fire": 3, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 1.5, "Fighting": 4,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
		   "Lapras": {"Normal": 3, "Fire": 3, "Water": 2, "Electric": 4, "Grass": 4, "Ice": 1.5, "Fighting": 4,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
#WATER/FLYING
		   "Gyarados":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 4.5, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 1, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
#____________________________________________________________________________________________________
#ELECTRIC
#			"":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 2, "Grass": 3, "Ice": 3, "Fighting": 3,
#			    "Poison": 3, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
			"Pikachu":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 2, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
			"Raichu":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 2, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
			"Voltorb":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 2, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
			"Electrode":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 2, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
			"Electabuzz":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 2, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
			"Jolteon":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 2, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
#ELECTRIC/STEEL
			"Magnemite":{"Normal": 2, "Fire": 4, "Water": 3, "Electric": 2, "Grass": 2, "Ice": 2, "Fighting": 4,
			    "Poison": 1, "Ground": 4, "Flying": 1.5, "Psychic": 2, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 2, "Dark": 3, "Steel": 1.5, "Fairy": 2},
			"Magneton":{"Normal": 2, "Fire": 4, "Water": 3, "Electric": 2, "Grass": 2, "Ice": 2, "Fighting": 4,
			    "Poison": 1, "Ground": 4, "Flying": 1.5, "Psychic": 2, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 2, "Dark": 3, "Steel": 1.5, "Fairy": 2},
#ELECTRIC/FLYING
			"Zapdos":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 1, "Flying": 2, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 2, "Fairy": 3},
#____________________________________________________________________________________________________
#GRASS
#			"":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 2, "Ice": 4, "Fighting": 3,
#			    "Poison": 4, "Ground": 2, "Flying": 4, "Psychic": 3, "Bug": 4, "Rock": 3, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Tangela":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 2, "Ice": 4, "Fighting": 3,
			    "Poison": 4, "Ground": 2, "Flying": 4, "Psychic": 3, "Bug": 4, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
#GRASS/POISON
			"Bulbasaur":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Ivysaur":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Venusaur":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Oddish":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Gloom":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Vileplume":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Bellsprout":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Weepinbell":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Victreebel":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
#GRASS/PSYCHIC
			"Exeggcute":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 2, "Ice": 4, "Fighting": 2,
			    "Poison": 4, "Ground": 2, "Flying": 4, "Psychic": 2, "Bug": 4.5, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel": 3, "Fairy": 3},
			"Exeggutor":{"Normal": 3, "Fire": 4, "Water": 2, "Electric": 2, "Grass": 2, "Ice": 4, "Fighting": 2,
			    "Poison": 4, "Ground": 2, "Flying": 4, "Psychic": 2, "Bug": 4.5, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel": 3, "Fairy": 3},
#____________________________________________________________________________________________________
#ICE
#			:{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 2, "Fighting": 4,
#			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
#ICE/PSYCHIC
			"Jynx":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 2, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 4, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel": 4, "Fairy": 3},
#ICE/FLYING
			"Articuno":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 4, "Grass": 2, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 1, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4.5, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
#____________________________________________________________________________________________________
#FIGHTING
#			:{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
#			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
#				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
			"Mankey":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
			"Primeape":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
			"Machop":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
			"Machoke":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
			"Machamp":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
			"Hitmonlee":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
			"Hitmonchan":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 3},
#____________________________________________________________________________________________________
#POISON
#			:{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
#			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Ekans":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Arbok":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"NidoranG":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Nidorina":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"NidoranB":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Nidorino":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Grimer":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Muk":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Koffing":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Weezing":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 2, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
#POISON/GROUND
			"Nidoqueen":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 3, "Ice": 4, "Fighting": 2,
			    "Poison": 1.5, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Nidoking":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 3, "Ice": 4, "Fighting": 2,
			    "Poison": 1.5, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 2, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
#POISON/FLYING
			"Zubat":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 4, "Grass": 1.5, "Ice": 4, "Fighting": 1.5,
			    "Poison": 2, "Ground": 1, "Flying": 3, "Psychic": 4, "Bug": 1.5, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Golbat":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 4, "Grass": 1.5, "Ice": 4, "Fighting": 1.5,
			    "Poison": 2, "Ground": 1, "Flying": 3, "Psychic": 4, "Bug": 1.5, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
#____________________________________________________________________________________________________
#GROUND
#			:{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 4, "Ice": 4, "Fighting": 3,
#			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Sandshrew":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 4, "Ice": 4, "Fighting": 3,
			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Sandslash":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 4, "Ice": 4, "Fighting": 3,
			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Diglett":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 4, "Ice": 4, "Fighting": 3,
			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Dugtrio":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 4, "Ice": 4, "Fighting": 3,
			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Cubone":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 4, "Ice": 4, "Fighting": 3,
			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Marowak":{"Normal": 3, "Fire": 3, "Water": 4, "Electric": 1, "Grass": 4, "Ice": 4, "Fighting": 3,
			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
#GROUND/ROCK
			"Rhyhorn":{"Normal": 2, "Fire": 2, "Water": 4.5, "Electric": 0, "Grass": 4.5, "Ice": 4, "Fighting": 4,
			    "Poison": 1.5, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
			"Rhydon":{"Normal": 2, "Fire": 2, "Water": 4.5, "Electric": 0, "Grass": 4.5, "Ice": 4, "Fighting": 4,
			    "Poison": 1.5, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
#____________________________________________________________________________________________________
#FLYING
#			:{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 4, "Grass": 2, "Ice": 4, "Fighting": 2,
#			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
#____________________________________________________________________________________________________
#PSYCHIC
#			:{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
#			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
#				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Abra":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Kadabra":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Alakazam":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Drowzee":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Hypno":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Mewtwo":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 2, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Mew":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 4, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
#PSYCHIC/FAIRY
			"Mr. Mime":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 1.5,
			    "Poison": 4, "Ground": 3, "Flying": 3, "Psychic": 2, "Bug": 3, "Rock": 3, "Ghost": 4,
				"Dragon": 0, "Dark": 3, "Steel": 4, "Fairy": 3},
#____________________________________________________________________________________________________
#BUG
#			:{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
#			    "Poison": 3, "Ground": 2, "Flying": 4, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Caterpie":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 2, "Flying": 4, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Metapod":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 2, "Flying": 4, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Pinsir":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 2,
			    "Poison": 3, "Ground": 2, "Flying": 4, "Psychic": 3, "Bug": 3, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
#BUG/FLYING
			"Butterfree":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 4, "Grass": 1.5, "Ice": 2, "Fighting": 1.5,
			    "Poison": 3, "Ground": 1, "Flying": 4, "Psychic": 3, "Bug": 2, "Rock": 4.5, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Scyther":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 4, "Grass": 1.5, "Ice": 2, "Fighting": 1.5,
			    "Poison": 3, "Ground": 1, "Flying": 4, "Psychic": 3, "Bug": 2, "Rock": 4.5, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
#BUG/POISON
			"Weedle":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 1.5, "Ice": 3, "Fighting": 1.5,
			    "Poison": 2, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Kakuna":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 1.5, "Ice": 3, "Fighting": 1.5,
			    "Poison": 2, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Beedril":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 1.5, "Ice": 3, "Fighting": 1.5,
			    "Poison": 2, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Venonat":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 1.5, "Ice": 3, "Fighting": 1.5,
			    "Poison": 2, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
			"Venomoth":{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 1.5, "Ice": 3, "Fighting": 1.5,
			    "Poison": 2, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
#BUG/GRASS
			"Paras":{"Normal": 3, "Fire": 4.5, "Water": 2, "Electric": 2, "Grass": 1.5, "Ice": 4, "Fighting": 2,
			    "Poison": 4, "Ground": 4, "Flying": 4.5, "Psychic": 3, "Bug": 4, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 3},
			"Parasect":	{"Normal": 3, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 1.5, "Ice": 3, "Fighting": 1.5,
			    "Poison": 2, "Ground": 3, "Flying": 4, "Psychic": 4, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 3, "Fairy": 2},
#____________________________________________________________________________________________________
#ROCK
#			:{"Normal": 2, "Fire": 2, "Water": 4, "Electric": 3, "Grass": 4, "Ice": 3, "Fighting": 4,
#			    "Poison": 2, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
#				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
#ROCK/GROUND
			"Geodude":{"Normal": 2, "Fire": 2, "Water": 4.5, "Electric": 0, "Grass": 4.5, "Ice": 4, "Fighting": 4,
			    "Poison": 1.5, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
			"Graveler":{"Normal": 2, "Fire": 2, "Water": 4.5, "Electric": 0, "Grass": 4.5, "Ice": 4, "Fighting": 4,
			    "Poison": 1.5, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
			"Golem":{"Normal": 2, "Fire": 2, "Water": 4.5, "Electric": 0, "Grass": 4.5, "Ice": 4, "Fighting": 4,
			    "Poison": 1.5, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
			"Onix":{"Normal": 2, "Fire": 2, "Water": 4.5, "Electric": 0, "Grass": 4.5, "Ice": 4, "Fighting": 4,
			    "Poison": 1.5, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 2, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
#ROCK/WATER
			"Omanyte":{"Normal": 2, "Fire": 1.5, "Water": 3, "Electric": 4, "Grass": 4.5, "Ice": 2, "Fighting": 4,
			    "Poison": 2, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
			"Omastar":{"Normal": 2, "Fire": 1.5, "Water": 3, "Electric": 4, "Grass": 4.5, "Ice": 2, "Fighting": 4,
			    "Poison": 2, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
			"Kabuto":{"Normal": 2, "Fire": 1.5, "Water": 3, "Electric": 4, "Grass": 4.5, "Ice": 2, "Fighting": 4,
			    "Poison": 2, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
			"Kabutops":{"Normal": 2, "Fire": 1.5, "Water": 3, "Electric": 4, "Grass": 4.5, "Ice": 2, "Fighting": 4,
			    "Poison": 2, "Ground": 4, "Flying": 2, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
#ROCK/FLYING
			"Aerodactyl":{"Normal": 2, "Fire": 2, "Water": 4, "Electric": 4, "Grass": 3, "Ice": 4, "Fighting": 3,
			    "Poison": 2, "Ground": 1, "Flying": 2, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 3, "Dark": 3, "Steel": 4, "Fairy": 3},
#____________________________________________________________________________________________________
#GHOST
#			:{"Normal": 1, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 1,
#			    "Poison": 2, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 3, "Ghost": 4,
#				"Dragon": 3, "Dark": 4, "Steel" : 3, "Fairy": 3},
#GHOST/POISON
			"Gastly":{"Normal": 1, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 1,
			    "Poison": 1.5, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 1.5, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel" : 3, "Fairy": 1.5},
			"Haunter":{"Normal": 1, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 1,
			    "Poison": 1.5, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 1.5, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel" : 3, "Fairy": 1.5},
			"Gengar":{"Normal": 1, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 3, "Fighting": 1,
			    "Poison": 1.5, "Ground": 4, "Flying": 3, "Psychic": 4, "Bug": 1.5, "Rock": 3, "Ghost": 4,
				"Dragon": 3, "Dark": 4, "Steel" : 3, "Fairy": 1.5},
#____________________________________________________________________________________________________
#DRAGON
#			:{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 2, "Grass": 2, "Ice": 4, "Fighting": 3,
#			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
#				"Dragon": 4, "Dark": 3, "Steel": 3, "Fairy": 4},
			"Dratini":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 2, "Grass": 2, "Ice": 4, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 4, "Dark": 3, "Steel": 3, "Fairy": 4},
			"Dragonair":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 2, "Grass": 2, "Ice": 4, "Fighting": 3,
			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 3, "Rock": 3, "Ghost": 3,
				"Dragon": 4, "Dark": 3, "Steel": 3, "Fairy": 4},
#DRAGON/FLYING
			"Dragonite":{"Normal": 3, "Fire": 2, "Water": 2, "Electric": 3, "Grass": 1.5, "Ice": 4.5, "Fighting": 2,
			    "Poison": 3, "Ground": 0, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 4, "Ghost": 3,
				"Dragon": 4, "Dark": 3, "Steel": 3, "Fairy": 4},
#____________________________________________________________________________________________________
#DARK
#			:{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 4,
#			    "Poison": 3, "Ground": 3, "Flying": 3, "Psychic": 0, "Bug": 4, "Rock": 3, "Ghost": 2,
#				"Dragon": 3, "Dark": 2, "Steel": 3, "Fairy": 4},
#____________________________________________________________________________________________________
#STEEL
#			:{"Normal": 2, "Fire": 4, "Water": 3, "Electric": 3, "Grass": 2, "Ice": 2, "Fighting": 4,
#			    "Poison": 1, "Ground": 4, "Flying": 2, "Psychic": 2, "Bug": 2, "Rock": 2, "Ghost": 3,
#				"Dragon": 2, "Dark": 3, "Steel": 2, "Fairy": 2},
#____________________________________________________________________________________________________
#FAIRY
#			:{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
#			    "Poison": 4, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 3, "Ghost": 3,
#				"Dragon": 1, "Dark": 2, "Steel": 4, "Fairy": 3},
"Clefairy":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			"Poison": 4, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 3, "Ghost": 3,
			"Dragon": 1, "Dark": 2, "Steel": 4, "Fairy": 3},
"Clefable":{"Normal": 3, "Fire": 3, "Water": 3, "Electric": 3, "Grass": 3, "Ice": 3, "Fighting": 2,
			"Poison": 4, "Ground": 3, "Flying": 3, "Psychic": 3, "Bug": 2, "Rock": 3, "Ghost": 3,
			"Dragon": 1, "Dark": 2, "Steel": 4, "Fairy": 3},}
#____________________________________________________________________________________________________

#computes manhattan distance by using pkmIterator and the pkmName, and values associates with it in dictionary
def manhattanDist(typeInfo1, typeInfo2):
    distance = 0
    for item in typeInfo1:
        if item in typeInfo2:
		#calculate distance based on dictionary information provided
            distance += abs(typeInfo1[item] - typeInfo2[item])
    return distance

#determines recommended Pokemon to populate pokeListRec
def determineRecommended(pkmName, pkmDict):
    distances = []
	#for each item in the dictionary
    for pkmIterator in pkmDict:
        #compute the distance if the iterator value is not
		#the same as the Pokemon name(pkmName).
        if pkmIterator != pkmName:
            distance = manhattanDist(pkmDict[pkmIterator], pkmDict[pkmName])
			#only add this Pokemon into the recommended list if
			#its distance value is greater than 12
            if distance > 12:
                distances.append((pkmIterator, "\n"))
	#sort the list in reverse for dissimilarity instead of similarity.
    distances.sort(reverse=True)
    return distances

#determines not recommended Pokemon to populate pokeListNRec
def determineNotRecommended(pkmName, pkmDict):
    distances = []
	#for each item in the dictionary
    for pkmIterator in pkmDict:
        #compute the distance if the iterator value is not
		#the same as the Pokemon name(pkmName).
        if pkmIterator != pkmName:
            distance = manhattanDist(pkmDict[pkmIterator], pkmDict[pkmName])
			#only add this Pokemon into the recommended list if
			#its distance value is less than or equal to 12
            if distance <= 12:
                distances.append((pkmIterator, "\n"))
	#sort the list in reverse for dissimilarity instead of similarity.
    distances.sort(reverse=True)
    return distances

#gets name of Pokemon from user and creates appropriate lists from it	
def getPokemon(*args):
    try:
		#get name entered into PokeVal_entry box
        pokeName = str(PokeVal.get())
        validEntry = False
        while validEntry == False:
			#if the name entered matches something in the dictionary...
            if pokeName in Pokemon:
                validEntry = True
				#populate the list boxes using the determine(Not)Recommended functions
                pokeListRec = (determineRecommended(pokeName, Pokemon))
                pokeListNRec = (determineNotRecommended(pokeName, Pokemon))
                #Populate listbox
                i=0
                recListBox.insert(END, "RECOMMENDED")
                while i < pokeListRec.__len__():
					#enters each list item into the GUI box
                    recListBox.insert(END, pokeListRec[i])
                    i+=1

                nRecListBox.insert(END, "NOT RECOMMENDED")
                i=0
                while i < pokeListNRec.__len__():
					#enters each list item into the GUI box
                    nRecListBox.insert(END, pokeListNRec[i])
                    i+=1
            else:
				#terminates if bad name is entered
                resetPokemon()
                print("Unidentified Pokemon entered.")
                exit()

    except ValueError:
        pass
		
#resets recommended and not recommened lists when button is clicked
def resetPokemon(*args):
    try:
        recListBox.delete(0, END)
        nRecListBox.delete(0, END)
    except ValueError:
        pass

root = Tk()
root.title("Pokemon Recommendation")

mainframe = ttk.Frame(root, padding="3 3 30 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

PokeVal = StringVar()

PokeVal_entry = ttk.Entry(mainframe, width=15, textvariable=PokeVal)
PokeVal_entry.grid(column=2, row=1, sticky=(W, E))

recListBox = Listbox(root, height=4)
recListBox.grid(column=0, row=1, sticky=(N,W,E,S))
s1 = ttk.Scrollbar(root, orient=VERTICAL, command=recListBox.yview)
s1.grid(column=1, row=1, sticky=(N,S))
recListBox['yscrollcommand'] = s1.set
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

nRecListBox = Listbox(root, height=4)
nRecListBox.grid(column=0, row=2, sticky=(N,W,E,S))
s2 = ttk.Scrollbar(root, orient=VERTICAL, command=nRecListBox.yview)
s2.grid(column=1, row=2, sticky=(N,S))
nRecListBox['yscrollcommand'] = s2.set
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Recommend", command=getPokemon).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="Reset", command=resetPokemon).grid(column=3, row=2, sticky=W)

ttk.Label(mainframe, text="Enter Pokemon:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Options:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Recommendations:").grid(column=1, row=3, sticky=W)

ttk.Label(mainframe, textvariable=PokeVal_entry).grid(column=2, row=3, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

PokeVal_entry.focus()
root.bind('<Return>', getPokemon)

root.mainloop()
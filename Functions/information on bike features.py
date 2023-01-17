#%% # information on bike features

def get_column_infos(data):
    column_infos = data.columns
    return column_infos

#%%   


#%%

bike_vocabulary = {
    "ERD": "effective rim diameter", #wheel size - has to do with the length of spokes 
    "BSD": "bead seat diameter", #wheel size - a bit bigger than ERD
    "RD": "rear derailleur" # hinterer Umwerfer
    "FD": "front derailler" # vorderer Umwerfer
    } 


bike_translations = {
    "rim": "Felge",
    "rim break": "Felgenbremse",
    "disc break": "Scheibenbremse",
    "hub": "Fahrradnabe",
    "rear hub": "hintere Radnabe",
    "front hub": "vordere Radnabe",
    "sprocket": "das Kettenrad, die Ritzel", 
    "spokes": "Speichen",
    "spoke holes for rim and hub": "Löcher für die Speichen in Felge und Radnabe"
    





    }

# common shifters and derailleurs on the bicycle: Shimano, SRAM, or Campagnolo
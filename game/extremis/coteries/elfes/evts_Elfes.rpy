init -5 python:
    import random
    from extremis.coteries.elfes import elfes

label testElfitude:
    menu:
        "TestElfitude"
        "youpi":
            pass
    $ testElfitude = random.randint(1,10)

    if testElfitude >=7:
        jump ascensionElfique
    else:
        "Le temps passe et vous n'êtes toujours pas accepté comme un elfe à part entière."
        jump effetVieillir

label ascensionElfique:
    menu:
        "ascensionElfique"
        "youpi":
            pass
    jump fin_cycle

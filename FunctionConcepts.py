def multipleInputs(*nums):  # This * can take multiple inputs when we call the teh function.
    print("Inputs given: ", nums)


multipleInputs("Amardeep", "Lokare", 1)


def keyvaluePair(**details):  # by ** we can give arguments in key-value paire.
    print(details.values())
    print(details.keys())
    print(details)


keyvaluePair(name="Amardeep", surname="Lokare", number=1)
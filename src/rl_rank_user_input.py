def getTrainingPack(rank):
    #codes by rank
    if rank == "Bronze":
        code= "ABC"
        return code
    elif rank == "Silver":
        code= "BCD"
        return code
    elif rank == "Gold":
        code= "CDE"
        return code
    elif rank == "Platinum":
        code= "DEF"
        return code
    elif rank == "Diamond":
        code= "EFG"
        return code
    elif rank == "Champion":
        code= "FGH"
        return code
    else:
        return -1

rank= input("Please input in your Rocket League Rank: ")
print(getTrainingPack(rank))

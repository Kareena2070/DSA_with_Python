# 14. Dictionary Comprehension: Given a list of words, create a dictionary where keys are words and values are their lengths using
# dictionary comprehension.

furits = {"banana", "apple", "grapes", "lichi", "watermalina"}

lenDicComprehensive = {furit:len(furits) for furit in furits }
print(lenDicComprehensive)



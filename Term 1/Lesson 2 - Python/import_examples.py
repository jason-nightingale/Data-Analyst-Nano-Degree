#always import scripts at the top. this creates a module object
#this imports a script as an alias of 'eh' for short
#to access objects inside the module use

"""this is going to show __name__ == '__main__'"""
import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)

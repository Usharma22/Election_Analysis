from pytest import Item


myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)


counties_dict ={}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

len(counties_dict)
print(len)
counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
print(Item)

counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
print(dist_keys)
counties_dict.values()
dict_values([422829, 463353, 432438])
counties_dict.get("Denver")
print(counties_dict)

my_dictionary = {"key":"value_pair"}

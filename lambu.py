models=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("original dictionary: ")
print(models)
sorted_models= sorted(models ,key=lambda x : x['color'])
print("sorted list")
print(sorted_models)
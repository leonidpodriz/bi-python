with open('data.txt', 'a') as file:
    for number in range(100):
        file.write(f'Line {number}\n')

with open('data.txt', 'r') as file:
    print(file.read())
# {
# 	“name”: “Arthur Conan Doyle”,
# 	“title”: “Sir”,
# 	“books”: [
# 	{
# 		“name”: “The Hound of the Baskervilles”,
# 		“publication_date”: “August 1901”,
# 		...
# 	},
# 	{
# 		“name”: “The Leather Funnel”,
# 		“publication_date”: “June 1903”,
# 		...
#
# 	},
# 	...
# 	]
# }

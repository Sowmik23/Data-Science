'''Dictionaries – like lists – are collections of objects. 
Unlike lists, dictionaries are unordered collections. 
They are not indexed by sequential numbers, but by keys:'''


mydict = {"apples": 42, "oranges": 999}

print(mydict['apples'])

newdict = {} #new empty dictionary declaration


mydict  = {"message": {"hello": 12345678}}

print(mydict)
print(mydict['message']['hello'])

# https://www.instagram.com/developer/endpoints/users/#get_users


instagram = {
    "data": {
        "id": "1574083",
        "username": "snoopdogg",
        "full_name": "Snoop Dogg",
        "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
        "bio": "This is my bio",
        "website": "http://snoopdogg.com",
        "counts": {
            "media": 1320,
            "follows": 420,
            "followed_by": 3410
        }
	}
}

print(instagram)


# If we pass a dict object into a for-loop, 
# by default, only the key will be yielded

mydict = {'a': 'Sowmik', 'b': 'Sarker'}
for x in mydict:
	val = mydict[x]
	mydict[x] = val.upper()   #this converts the texts into uppercase letter
	print('Changed what', x, 'points to: from', val, 'to', mydict[x])


# for only print the dict keys
for x in mydict.keys():
	print(x)

# for only print the dict values
for x in mydict.values():
	print(x)


# items() returns a sequence of tuples.

for key, val in mydict.items():
    print("Key", key, 'points to', val)


# accessing a non-existent key of a dictionary will raise a KeyError
mydict = {'z': 999}
print(mydict.get('z'))
print(mydict.get('sssss'))


names = []
names.append({'first': 'Dan', 'last': 'Nguyen', 'suffix': 'III'})
names.append({'first': 'Jane'})

#just see the behaviours
for name in names:
    x = name.get('first')
    y = name.get('last')
    z = name.get('suffix')
    print(x, y, z)

#just see the behaviours
for name in names:
    x = name.get('first')
    y = name.get('last')
    z = name.get('suffix')
    if not x:
        x = ""
    if not y:
        y = "Doe"
    if not z:
        z = ""
    print(x, y, z)


#update dictionary
a = {'first': 'Dan', 'last': 'Nguyen'}
b = {'last': 'Smith', 'suffix': 'Jr.'}
print(a)
a.update(b)
print(a)


# list\\LIST comparison with dictionary

mylist = []
mylist.append('a')
mylist.append('b')
mylist.append('c')


# dictionaries are unordered collections of objects, 
# we're allowed to set values with any key we like
# but in list we can not set key random 


# mylist[999] = 'Hey'
# IndexError: list assignment index out of range

mydict = {}
mydict[99999999] = "hello"

# ************************************************************
# Anything that can be represented in a list
# also can be represented as a dictionary, and vice versa


# Instagram user
# The Instagram API allows us to look up an 
# [individual user]((https://www.instagram.com/developer/endpoints/users/#get_users):

datathing = {
      "data": {
          "id": "1574083",
          "username": "snoopdogg",
          "full_name": "Snoop Dogg",
          "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
          "bio": "This is my bio",
          "website": "http://snoopdogg.com",
          "counts": {
              "media": 1320,
              "follows": 420,
              "followed_by": 3410
          }
  }
}


# The End
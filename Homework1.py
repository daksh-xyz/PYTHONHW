y = [{
    'personalInfo': {
        'name': 'Daksh',
        'age': 18,
        'email': {
            'official':'dakshuklal@gmail.com',
            'alt':'daksh-xyz-github@noreply.com',
        },
    },
},
    {'\n''proInfo':{
        'school': 'BBPSGR',
        'college': 'MUJ',
    }},
    {'\n''aboutUs': {'We\'re learning a programming laguage called Python and it\'s really fun except for all the errors :)'}},
    {'\n''Hobbies': {
        'Indoor': ['Reading', 'Coding','Cooking','Binge-watching TV series'],
        'Outdoor': ['Gym', 'Badminton','Shopping']
    }
}]

#print(y[1])

x = tuple(y)
print(x)
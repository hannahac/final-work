


usage = '''
    Office Space Allocation

    Usage:


        dojo.py  Office Space Allocation create_room (<room_type> <room_name> ...) 
        dojo.py  Office Space Allocation add_person (<person_name> <FELLOW|STAFF>[wants_accomodation])


'''
from docopt import docopt
args = docopt(usage)

def output_rooms_created(room_type, room_name):
    if room_type == 'office':
        print('An {} called {} has been created'.format(room_type, room_name))
    else:
        print('A {} called {} has been created'.format(room_type, room_name))    

if args['create_room']:
    allowed_room_types = ['office', 'livingspace']
    room_type = args['<room_type>']
    room_name = args['<room_name>']
    if room_type in allowed_room_types == 'office':
       output_rooms_created(room_type, room_name)
    elif room_type in allowed_room_types == 'livingspace':
        output_rooms_created(room_type, room_name)   
    else:
        print('{} is not a recognised room type'.format(room_type))

def people_added(person_name, role):
    if role == 'fellow':
        print('{} {} has been successfuly added'.format(person_name, role))
    else:
        print('{} {} has been successfuly added'.format(person_name, role))

if args['add_person']:
    allowed_roles = ['fellow', 'staff']
    person_name = args['<person_name>'].capitalize()
    role = args['<role>'].capitalize()
    if role != allowed_roles:
        people_added(person_name, role)
    else:
        print('{} is not a recognised role'.format(role))    



hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'sMorpheus']
  }
}

# check in function
# def check_in(floor_number, room_number):
#     if hotel[floor_number][room_number]:
#         print('This room is occupied. Please choose another room\n')
#         new_floor = input('New floor number: ')
#         new_room = input('New room number: ')
#         check_in(new_floor, new_room)
#     else:
#         number_of_guests  = int(input('Number of guests: '))
#         guests = input('Guest: ') * number_of_guests
    # hotel[floor_number][room_number] = 'test'
# checking out-remove the occupants
def check_out(floor_number, room_number):
    pass

# display menu
is_looking_up = True
while is_looking_up:
    # floor number, room number prompt

    choice = input('Check in (1) or check out (2) ? ')
    floor_number = input('Floor number: ')
    room_number = input('Room number: ')
    if choice == '1':
        check_in(floor_number, room_number)
        # check_in()
    if choice == '2':
        pass
    
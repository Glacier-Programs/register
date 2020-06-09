#these are the functions for the main file
this function checks if screen should be changed
old_screen = 0
cur_screen = 0
def change():
  global old_screen, cur_screen
  if old_screen == new_screen:
    return False
   else:
    return True

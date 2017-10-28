from time import sleep
import os

def game_type():
  print "\n"

  print "Welcome to a game of Tic Tac Toe!"
  print "Would you like to play:"
  print "a) Human vs. Human"
  print "b) Human vs. Computer"
  print "c) Computer vs. Computer"
  print "\n"
  play = raw_input("Play: ")
  if play == "a":
    human_game()
  elif play == "b":
    comp_vs_human()
  elif play == "c":
      computer_vs_computer
  else:
    os.system("clear")
    print "Not an option. Choose: a,b or c"
    game_type()

def intro():
  playing = True
  board = [""," "," "," "," "," "," "," "," "," "]
  b = board


  print """
  Instructions: Choose any number, 1-9, that has
  not yet been used by the other player.
  Player 1 will choose their letter first.
  In order to win the game, your letter
  (X or O) must be three times in a row either
  horizontally, vertically or diagonally.
  \n"""

  def example_board():

      board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9"
      return board

  sleep(1)


  def game_board():
      return " "+b[1]+" | "+b[2]+" | "+b[3]+" \n-----------\n "+b[4]+" | "+ b[5] +" | "+b[6]+"\n-----------\n "+b[7]+" | "+b[8]+" | "+b[9]+" "

  def players():
    answer = raw_input()
    if answer.upper() == "X":
      player1 = 'X'
      player2 = "O"
      return player1, player2
    elif answer.upper() == "O":
      player1 = 'O'
      print player1
      player2 = "X"
      print player2
      return player1, player2
    else:
      raise ValueError("X or O please.")

  def check_full_x():

      if b[choice] == " ":
          b[choice] = "X"
          return True
      else:
          print "Sorry, space full. Try again."
          return False


  def check_full_o():

      if b[choice] == " ":
          b[choice] = "O"
          return True
      else:
          print "Sorry, space taken. Try again."
          return False
  def play_again():
      print "Do you want to play again? (y/n)"
      answer = raw_input()
      if answer == "y":
          os.system("clear")
          game_type()
      elif answer == "n":
          exit()
      else:
          print "Not WURKING"
          play_again()


  def win(b,p):

      if (b[1] == p and b[2] == p and b[3] == p) or \
          (b[4] == p and b[5] == p and b[6] == p) or \
  	(b[7] == p and b[8] == p and b[9] == p) or \
  	(b[1] == p and b[4] == p and b[7] == p) or \
  	(b[2] == p and b[5] == p and b[8] == p) or \
  	(b[3] == p and b[6] == p and b[9] == p) or \
  	(b[3] == p and b[5] == p and b[7] == p) or \
  	(b[1] == p and b[5] == p and b[9] == p):
          return True
      else:
          return False
  return players, play_again#, win, example_board, game_board, check_full_x, check_full_o



def human_game():

  playing = True
  board = [""," "," "," "," "," "," "," "," "," "]
  b = board

  #example_board, game_board = intro()
  def example_board():

      board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9"
      return board

  sleep(1)


  def game_board():
      return " "+b[1]+" | "+b[2]+" | "+b[3]+" \n-----------\n "+b[4]+" | "+ b[5] +" | "+b[6]+"\n-----------\n "+b[7]+" | "+b[8]+" | "+b[9]+" "


  #players, win, example_board, game_board, check_full_x, check_full_o = intro()
  players, play_again = intro()

  print "\n"
  print "Quick! You  two have 5 seconds to decide who will be Player 1"
  sleep(1)
  print "\n"
  print "Player 1, would you like to be X or O? "
  print "\n"
  player1, player2 = players()


  def check_full_x():

      if b[choice] == " ":
          b[choice] = "X"
          return True
      else:
          print "Sorry, space full. Try again."
          return False


  def check_full_o():

      if b[choice] == " ":
          b[choice] = "O"
          return True
      else:
          print "Sorry, space taken. Try again."
          return False
  def win(b,p):

      if (b[1] == p and b[2] == p and b[3] == p) or \
          (b[4] == p and b[5] == p and b[6] == p) or \
  	(b[7] == p and b[8] == p and b[9] == p) or \
  	(b[1] == p and b[4] == p and b[7] == p) or \
  	(b[2] == p and b[5] == p and b[8] == p) or \
  	(b[3] == p and b[6] == p and b[9] == p) or \
  	(b[3] == p and b[5] == p and b[7] == p) or \
  	(b[1] == p and b[5] == p and b[9] == p):
          return True
      else:
          return False



  while playing:
      os.system("clear")

      print "\n"
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board()
      print "Player 1"
      choice = int(raw_input("What is your number 1-9?"))
      if player1 == "X":
        while not check_full_x():
            choice = int(raw_input("Please choose an empty space for X. "))
            #print choice
      else:
        while not check_full_o():
          choice = int(raw_input("Please choose an empty space for O. "))



      os.system("clear")
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board()

      #X's win
      if win(b, "X"):
  	    os.system("clear")
  	    print game_board()
  	    print "X won the game! Too bad O."
  	    play_again()

      # If there is a tie
      full = True
      if " " in b:
        full = False

      if full:
          print "Both of you lost -_-"
          break


      print "Player 2's turn."
      choice = int(raw_input("What is your number 1-9?"))
      if player2 == "X":
        while not check_full_x():
            choice = int(raw_input("Please choose an empty space for X. "))
            #print choice
      else:
        while not check_full_o():
          choice = int(raw_input("Please choose an empty space for O. "))



      if win(b, "O"):
          os.system("clear")
          print game_board()
          print "O wins! Congratulations! Sorry X."
          #print "GAME OVER."
          break


def comp_vs_human():

  playing = True
  board = [""," "," "," "," "," "," "," "," "," "]
  b = board
  players,play_again = intro()

  #example_board, game_board = intro()
  def example_board():

      board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9"
      return board

  sleep(1)


  def game_board():
      return " "+b[1]+" | "+b[2]+" | "+b[3]+" \n-----------\n "+b[4]+" | "+ b[5] +" | "+b[6]+"\n-----------\n "+b[7]+" | "+b[8]+" | "+b[9]+" "
  def check_full_x():

      if b[choice] == " ":
          b[choice] = "X"
          return True
      else:
          print "Sorry, space full. Try again."
          return False


  def check_full_o():

      if b[choice] == " ":
          b[choice] = "O"
          return True
      else:
          print "Sorry, space taken. Try again."
          return False
  def win(b,p):

      if (b[1] == p and b[2] == p and b[3] == p) or \
          (b[4] == p and b[5] == p and b[6] == p) or \
  	(b[7] == p and b[8] == p and b[9] == p) or \
  	(b[1] == p and b[4] == p and b[7] == p) or \
  	(b[2] == p and b[5] == p and b[8] == p) or \
  	(b[3] == p and b[6] == p and b[9] == p) or \
  	(b[3] == p and b[5] == p and b[7] == p) or \
  	(b[1] == p and b[5] == p and b[9] == p):
          return True
      else:
          return False

  def test_win(b,p,v):
      old_val = b[v]
      b[v] = p
      is_win = win(b,p)
      b[v] = old_val
      return is_win


  def computer_turn(b,p):
    #check computer win move
    for v in range(1,10):
         if b[v] == " " and test_win(b, player2, v):
            #b[v] = p
            return v

    # Check player win moves
    for i in range(1,10):
        if b[i] == ' ' and test_win(b,player1, i):
            return i
    # Play a corner
    for i in [1, 3, 7, 9]:
        if b[i] == ' ':
            return i
    # Play center
    if b[5] == ' ':
        return 5
    #Play a side
    for i in [4, 2, 8, 6]:
        if b[i] == ' ':
            return i

  print "Human, would you like to go first or second? (1/2)"

  if raw_input() == "1":
    print "Would you like to be X or O?"
    player1, player2 = players()
    while playing:
      os.system("clear")

      print "\n"
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board()
      print "Human"
      choice = int(raw_input("What is your number 1-9?"))
      if player1 == "X":
        while not check_full_x():
            choice = int(raw_input("Please choose an empty space for X. "))
            #print choice
      else:
        while not check_full_o():
          choice = int(raw_input("Please choose an empty space for O. "))



      os.system("clear")
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board()

      #X's win
      if win(b, "X"):
  	    os.system("clear")
  	    print game_board()
  	    print "X won the game! Too bad O."
        #print "A place holder"
        print play_again()
      # If there is a tie
      full = True
      if " " in b:
        full = False

      if full:
          print "Both of you lost -_-"
          play_again()
          break


      print "Computer's turn."
      computer = player2
      if computer == "X":
        while not check_full_x():
            choice = computer_turn(b,"X")
        print choice
        if win(b,"X"):
            break
            #print choice
      else:
        while not check_full_o():
          choice = computer_turn(b,"O")
        print choice
        if win(b,"O"):
            break



      if win(b, "O"):
          os.system("clear")
          print game_board()
          print "O wins! Congratulations! Sorry X."
          play_again()
          #print "GAME OVER."
          break

  if raw_input() == "2":

    print "Would you like to be X or O?"
    player1, player2 = players()

  else:
    print "Not option"
    comp_vs_human()

def computer_vs_computer():
    intro()

game_type()

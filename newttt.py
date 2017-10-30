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
      computer_vs_computer()
  else:
    os.system("clear")
    print "Not an option. Choose: a,b or c"
    game_type()

def example_board():

  board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9"
  return board

def game_board(board):
  return " "+board[1]+" | "+board[2]+" | "+board[3]+" \n-----------\n "+board[4]+" | "+ board[5] +" | "+board[6]+"\n-----------\n "+board[7]+" | "+board[8]+" | "+board[9]+" "

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

def play_again():
    print "Do you want to play again? (y/n)"
    answer = raw_input()
    if answer == "y":
        os.system("clear")
        game_type()
    elif answer == "n":
        exit()
    else:
        print "NOT WORKING"
        play_again()

def win(b,p):
    # All possible wins
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

def check_full_x(b,choice):

    if b[choice] == " ":
        sleep(1)
        b[choice] = "X"
        return True
    else:
        print "Sorry, space full. Try again."
        return False


def check_full_o(b,choice):

    if b[choice] == " ":
        sleep(1)
        b[choice] = "O"
        return True
    else:
        print "Sorry, space taken. Try again."
        return False

def test_win(b,p,v):
    # Checks to see if a win is possible
    old_val = b[v]
    b[v] = p
    is_win = win(b,p)
    b[v] = old_val
    return is_win

def test_fork(b,p,v):
    # checks if a move opens up a fork
    winningMoves = 0
    for v in range(0, 9):
        if test_win(b, p, v) and b[v] == ' ':
            winningMoves += 1
    return winningMoves >= 2


def intro():
  print """
  Instructions: Choose any number, 1-9, that has
  not yet been used by the other player.
  Player 1 will choose their letter first.
  In order to win the game, your letter
  (X or O) must be three times in a row either
  horizontally, vertically or diagonally.
  \n"""

  sleep(1)

def human_game():

  playing = True
  board = [""," "," "," "," "," "," "," "," "," "]
  b = board
  sleep(1)
  intro()

  print "\n"
  print "Quick! You  two have 5 seconds to decide who will be Player 1"
  sleep(5)
  print "\n"
  print "Player 1, would you like to be X or O? "
  print "\n"
  player1, player2 = players()


  while playing:
      os.system("clear")

      print "\n"
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)
      print "Player 1"
      choice = int(raw_input("What is your number 1-9?"))
      if player1 == "X":
        while not check_full_x(b, choice):
            choice = int(raw_input("Please choose an empty space for X. "))

      else:
        while not check_full_o(b,choice):
          choice = int(raw_input("Please choose an empty space for O. "))



      os.system("clear")
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)

      #X's win
      if win(b, "X"):
        os.system("clear")
        print game_board(b)
        print "X won the game! Too bad O."
        play_again()

      # If there is a tie
      full = True
      if " " in b:
        full = False

      if full:
          print "Both of you lost -_-"
          play_again()


      print "Player 2's turn."
      choice = int(raw_input("What is your number 1-9?"))
      if player2 == "X":
        while not check_full_x(b,choice):
            choice = int(raw_input("Please choose an empty space for X. "))
            print choice
      else:
        while not check_full_o(b,choice):
          choice = int(raw_input("Please choose an empty space for O. "))
          print choice



      if win(b, "O"):
          os.system("clear")
          print game_board(b)
          print "O wins! Congratulations! Sorry X."
          print "GAME OVER."
          play_again()


def comp_vs_human():

  playing = True
  board = [""," "," "," "," "," "," "," "," "," "]
  b = board
  intro()
  sleep(1)

  def computer_turn(b,p):
    #check computer win move
    for v in range(1,10):
         if b[v] == " " and test_win(b, player2, v):
            print "Choosing space ", v
            sleep(1)
            return v

    # Check player win moves
    for i in range(1,10):
        if b[i] == ' ' and test_win(b,player1, i):
            print "Choosing space ", i
            sleep(1)
            return i
    # Check computer fork opportunities
    for i in range(1, 10):
        if b[i] == ' ' and test_fork(b, player2, i):
            print "Choosing space ", i
            sleep(1)
            return i
    #  Check player fork opportunities
    for i in range(1, 10):
        if b[i] == ' ' and test_fork(b, player1, i):
            print "Choosing space ", i
            sleep(1)
            return i
    # Play center
    if b[5] == ' ':
        print "Choosing space 5"
        sleep(1)
        return 5

    # Play a corner
    for i in [1, 3, 7, 9]:
        if b[i] == ' ':
            print "Choosing space ", i
            sleep(1)
            return i
    #Play a side
    for i in [4, 2, 8, 6]:
        if b[i] == ' ':
            print "Choosing space ", i
            sleep(1)
            return i



  print "Human, would you like to go first or second? (1/2)"
  first_or_second = raw_input()
  if first_or_second == "1":
    print "Would you like to be X or O?"
    player1, player2 = players()

    while playing:
      os.system("clear")

      print "\n"
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)
      print "Human"
      choice = int(raw_input("What is your number 1-9?"))
      if player1 == "X":
        while not check_full_x(b,choice):
            choice = int(raw_input("Please choose an empty space for X. "))

      else:
        while not check_full_o(b,choice):
          choice = int(raw_input("Please choose an empty space for O. "))

      os.system("clear")
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)

      #X's win
      if win(b, player1):
        os.system("clear")
        print game_board(b)
        print "%s won the game! Too bad %s." % (player1, player2)
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
        choice = computer_turn(b,"X")
        while not check_full_x(b,choice):
            choice = computer_turn(b,"X")
        print choice
      else:
        choice = computer_turn(b,"O")
        while not check_full_o(b,choice):
          choice = computer_turn(b,"O")
        print choice

      if win(b, player2):
          os.system("clear")
          print game_board(b)
          print "%s wins! Congratulations! Sorry %s." % (player2, player1)
          play_again()
          print "GAME OVER."
          play_again()

  if first_or_second == "2":

    print "Would you like to be X or O?"
    player1, player2 = players()
    while playing:
      os.system("clear")

      print "\n"
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)

      print "Computer's turn."
      computer = player2
      if computer == "X":
        choice = computer_turn(b,"X")
        while not check_full_x(b,choice):
            choice = computer_turn(b,"X")
        print choice
      else:
        choice = computer_turn(b,"O")
        while not check_full_o(b,choice):
          choice = computer_turn(b,"O")
        print choice

      if win(b, player2):
          os.system("clear")
          print game_board(b)
          print "%s wins! Congratulations! Sorry %s." % (player2, player1)
          play_again()
          print "GAME OVER."
          play_again()

      os.system("clear")
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)

      choice = int(raw_input("What is your number 1-9?"))
      if player1 == "X":
        while not check_full_x(b,choice):
            choice = int(raw_input("Please choose an empty space for X. "))
      else:
        while not check_full_o(b,choice):
          choice = int(raw_input("Please choose an empty space for O. "))

      #X's win
      if win(b, player1):
        os.system("clear")
        print game_board(b)
        print "%s won the game! Too bad %s." % (player1, player2)
        print play_again()
      # If there is a tie
      full = True
      if " " in b:
        full = False

      if full:
          print "Both of you lost -_-"
          play_again()
          break
  else:
    print "Not option"
    comp_vs_human()

def computer_vs_computer():
    playing = True
    board = [""," "," "," "," "," "," "," "," "," "]
    b = board
    print "Computer1 versus Computer2"
    print "Computer1 will be X"
    print "Computer2 will be O"
    sleep(1)
    os.system("clear")
    print "\n"
    print "Let the battle begin"
    sleep(1)
    computer1 = "X"
    computer2 = "O"


    def computer_moves(b,p):
      #check computer win move
      for v in range(1,10):
           if b[v] == " " and test_win(b, play1, v):
              print "Choosing space ", v
              sleep(1)
              return v

      # Check computer1 win moves
      for i in range(1,10):
          if b[i] == ' ' and test_win(b,play2, i):
              print "Choosing space ", i
              sleep(1)
              return i
      # Check computer fork opportunities
      for i in range(1, 10):
          if b[i] == ' ' and test_fork(b, play1, i):
              print "Choosing space ", i
              sleep(1)
              return

      #  Check computer fork opportunities
      for i in range(1, 10):
          if b[i] == ' ' and test_fork(b, play2, i):
              print "Choosing space ", i
              sleep(1)
              return i
      # Play center
      if b[5] == ' ':
          print "Choosing space 5"
          sleep(1)
          return 5

      # Play a corner
      for i in [1, 3, 7, 9]:
          if b[i] == ' ':
              print "Choosing space ", i
              sleep(1)
              return i
      #Play a side
      for i in [4, 2, 8, 6]:
          if b[i] == ' ':
              print "Choosing space ", i
              sleep(1)
              return i


    while playing:
      os.system("clear")

      print "\n"
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)
      print "Computer 1"
      play2 = computer1
      play1 = computer2
      choice = computer_moves(b,"X")
      while not check_full_x(b,choice):
        choice = computer_moves(b,"X")

      os.system("clear")
      print example_board()
      print "The numbers above represent the spaces you want your letters to be."
      print game_board(b)

      #X's win
      if win(b, computer1):
        os.system("clear")
        print game_board(b)
        print "%s won the game! Too bad %s." % (computer1, computer2)
        exit()
      # If there is a tie
      full = True
      if " " in b:
        full = False

      if full:
          print "Both of you lost -_-"
          exit()

      print "Computer 2's turn."
      play1 = computer1
      play2 = computer2
      choice = computer_moves(b,"O")
      while not check_full_o(b,choice):
        choice = computer_moves(b,"O")

      if win(b, computer2):
          os.system("clear")
          print game_board(b)
          print "%s wins! Congratulations! Sorry %s." % (computer2, computer1)
          print "GAME OVER."
          exit()

if __name__ == "__main__":
    game_type()

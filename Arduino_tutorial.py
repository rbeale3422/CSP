try:
  from pyfirmata import Arduino, util
except:
  import pip
  pip.main(['install','pyfirmata'])
  from pyfirmata import Arduino, util
import time

#create an Arduino object
board = Arduino('COM4')

#start the board listening for commands
iterator = util.Iterator(board)
iterator.start()

#get reference to the two led lights set at digital 12(green) and 13(red)
LED1 = board.get_pin('d:13:o')
LED2 = board.get_pin('d:12:o')
# LED3 = board.get_pin('d:11:o')
# LED4 = board.get_pin('d:10:o')

#delay while connecting to board
time.sleep(1.0)

while True:
  LED1.write(1.0)
  time.sleep(1.0)
  LED2.write(1.0)
  time.sleep(1.0)
  # LED3.write(1.0)
  # time.sleep(1.0)
  # LED4.write(1.0)
  # time.sleep(1.0)
  LED1.write(0.0)
  time.sleep(1.0)
  LED2.write(0.0)
  time.sleep(1.0)
  # LED3.write(0.0)
  # time.sleep(1.0)
  # LED4.write(0.0)
  # time.sleep(1.0)
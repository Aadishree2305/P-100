class Atm(object):
  """
    blueprint for atm
  """

  def __init__(self, company, amount ,pinNumber):
    self.pinNumber=pinNumber
    self.amount=amount
    self.company = company

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def insert_card(self):
    print("Insert the Card")
    "Processing...."

  def enter_pin(self, gear_type):
    print("Enter the pin")
    "Processing...."


bank = Atm("icici",2000,123456)

print(bank.start())

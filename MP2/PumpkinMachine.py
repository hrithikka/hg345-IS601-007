from enum import Enum
import sys


from PumpkinMachineExceptions import (
    ExceededRemainingChoicesException,
    InvalidChoiceException,
    InvalidStageException,
    NeedsCleaningException,
    OutOfStockException,
    InvalidPaymentException,
)

class Usable:
    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if self.quantity < 0:
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self):
        return self.name

class Pumpkin(Usable):
    pass

class FaceStencil(Usable):
    pass

class Extra(Usable):
    pass

class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4

class PumpkinMachine:
    USES_UNTIL_CLEANING = 15
    MAX_STENCILS = 3
    MAX_EXTRAS = 3

    def __init__(self):
        
        self.pumpkins = [
            Pumpkin(name="Mini Pumpkin", cost=1),
            Pumpkin(name="Small Pumpkin", cost=2),
            Pumpkin(name="Medium Pumpkin", cost=2.5),
            Pumpkin(name="Large Pumpkin", cost=3),
        ]
        self.face_stencils = [
            FaceStencil(name="Happy Face", quantity=10, cost=1),
            FaceStencil(name="Scream Face", quantity=10, cost=1),
            FaceStencil(name="Toothy Face", quantity=10, cost=1),
            FaceStencil(name="Spooky Face", quantity=10, cost=1),
        ]
        self.extras = [
            Extra(name="Small Candle", quantity=10, cost=0.25),
            Extra(name="LED Candle", quantity=10, cost=0.25),
            Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
            Extra(name="Sticker Pack", quantity=10, cost=1.00),
            Extra(name="Paint Kit", quantity=10, cost=3),
            Extra(name="Dry Ice", quantity=10, cost=0.25),
            Extra(name="Googly Eyes", quantity=10, cost=0.25),
            Extra(name="Glitter", quantity=10, cost=0.25),
        ]

        
        self.remaining_uses = self.USES_UNTIL_CLEANING
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.total_sales = 0
        self.total_products = 0
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def pick_pumpkin(self, choice):
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException
        for c in self.pumpkins:
            if c.name.lower() == choice.lower() and c.in_stock():
                c.use()
                self.inprogress_pumpkin.append(c)
                return
        raise InvalidChoiceException  

    def pick_face_stencil(self, choice):
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException  
        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException 
        for f in self.face_stencils:
            if f.name.lower() == choice.lower() and f.in_stock():
                f.use()
                self.inprogress_pumpkin.append(f)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException  
    def pick_extras(self, choice):
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException
        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException 
        for t in self.extras:
            if t.name.lower() == choice.lower() and t.in_stock():
                t.use()
                self.inprogress_pumpkin.append(t)
                self.remaining_extras -= 1
                return
        raise InvalidChoiceException 

    def reset(self):
        
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
       
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_pumpkin_choice(self, pumpkin):
      
        self.pick_pumpkin(pumpkin)
        self.currently_selecting = STAGE.FaceStencil

    def handle_face_stencil_choice(self, face_stencil):
        if face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        else:
        # Check if the selected face stencil is in stock
            for stencil in self.face_stencils:
                if stencil.name == face_stencil:
                    if stencil.quantity == 0:
                        raise OutOfStockException("The selected face stencil is out of stock.")
                    else:
                        self.pick_face_stencil(face_stencil)
                        stencil.quantity <= 1
                        break


    def handle_extra_choice(self, extra):
        if extra == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_extras(extra)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
            self.total_products += 1
            self.total_sales += expected
            self.reset()
        else:
            raise InvalidPaymentException 

    def print_current_pumpkin(self):
       
        print(f"Current Pumpkin: {', '.join([x.name for x in self.inprogress_pumpkin])}")

    def calculate_cost(self):
    # Calculate the total cost of the in-progress pumpkin customization.
    # This method calculates the proper value of the inprogress_pumpkin array.
    # UCID: hg345 Date: 10/23/2023
        total_cost = sum(item.cost for item in self.inprogress_pumpkin)
        return total_cost

    def run(self):
        try:
            if self.currently_selecting == STAGE.Pumpkin:
                pumpkin = input(
                    f"What type of pumpkin would you like {', '.join([c.name.lower() for c in self.pumpkins if c.in_stock()])}?\n")
                self.handle_pumpkin_choice(pumpkin)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.FaceStencil:
                stencil = input(
                    f"What type of face stencil would you like {', '.join([f.name.lower() for f in self.face_stencils if f.in_stock()])}? Or type next.\n")
                self.handle_face_stencil_choice(stencil)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Extra:
                extra = input(
                    f"What extras would you like {', '.join([t.name.lower() for t in self.extras if t.in_stock()])}? Or type done.\n")
                self.handle_extra_choice(extra)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                expected_formatted = "${:.2f}".format(expected)  # Format the expected value as currency
                #input() message should properly display the value in currency format 
                total = input(f"Your total is {expected_formatted}, please enter the exact value.\n")
                # UCID: hg345 DATE: 10/23/2023
                self.handle_pay(expected, total)

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    print("Quitting the pumpkin machine")
                    return 1
        except KeyboardInterrupt:
            print("Quitting the pumpkin machine")
            sys.exit()
        #UCID:hg345 DATE:10/23/2023
        # Handling OutOfStockException and indicating the current stage/category
        except OutOfStockException as e:
            print(f"{self.currently_selecting} is out of stock.") 
        # Handling NeedsCleaningException
        except NeedsCleaningException as e:
            while True:
                user_input = input("Type clean to clear the machine before using") 
                if user_input.lower() == "clean":
                    self.clean_machine()
                    print("Machine has been cleaned.")
                    break
                else:
                    continue
        # Handling InvalidChoiceException and indicating the current stage/category
        except InvalidChoiceException as e:
            print(f"{self.currently_selecting} has an invalid choice.") 
        # Handling ExceededRemainingChoicesException and indicating the current stage/category     
        except ExceededRemainingChoicesException as e:
            print(f"{self.currently_selecting} has exceeded remaining choices.") 
        # Handling InvalidPaymentException
        except InvalidPaymentException as e:
            print("Invalid payment.")
        
        except Exception as e:
            print(f"Something went wrong and I didn't handle it: {e}")

        self.run()

    def start(self):
        self.run()

if __name__ == "__main__":
    pm = PumpkinMachine()
    pm.start()

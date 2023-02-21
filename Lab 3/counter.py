class Countdown:
    def __init__(self,start,step= 1) -> None:
        self.current = start
        self.step = step
        
    def down(self) -> None:
        self.current -= self.step
    
    @property
    def complete(self):
        if self.current <=0:
            return True
        else:
            return False
    
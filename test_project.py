from main import *

def test_updateScore():
    ship = Ship()
    score = 10
    ship.level = 10
    assert score * ship.level == 100

def test_updateRock():
    column = random.randint(0, 1200)
    assert column in range(0, 1200)
    
def test_endTitle():
    assert endTitle(0) == False



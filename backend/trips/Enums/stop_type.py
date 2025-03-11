class StopType:
    REST = 'rest'
    FUEL = 'fuel'
    FOOD = 'food'
    OVERNIGHT = 'overnight'
    
    CHOICES = [
        (REST, 'Rest Stop'),
        (FUEL, 'Fuel Stop'),
        (FOOD, 'Food Stop'),
        (OVERNIGHT, 'Overnight Stop')
    ]
class LogStatus:
    OFF_DUTY = 'off_duty'
    SLEEPER_BERTH = 'sleeper_berth'
    DRIVING = 'driving'
    ON_DUTY = 'on_duty'
    
    CHOICES = [
        (OFF_DUTY, 'Off Duty'),
        (SLEEPER_BERTH, 'Sleeper Berth'),
        (DRIVING, 'Driving'),
        (ON_DUTY, 'On Duty Not Driving')
    ]
try:
    from lib import checks
except:
    import checks

class Utils:
    
    def __init__(self):
        print("utilself")
        self.checks = checks.Checks()

    def animate(self):
        print("animation")

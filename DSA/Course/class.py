class Cookie:
    def __init__(self, color):   # 'self' keyword indicates that the method belongs to a class
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie1 = Cookie('green')
cookie2 = Cookie('blue')

print(f'Cookie 1 is {cookie1.get_color()}')
print(f'Cookie 2 is {cookie2.get_color()}')

cookie1.set_color('yellow')

print(f'\nCookie 1 is now {cookie1.get_color()}')
print(f'Cookie 2 is still {cookie2.get_color()}')
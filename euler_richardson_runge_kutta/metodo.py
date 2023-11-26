
class Metodo: 
    def __init__(self, x0, y0, h):
        self.x0 = x0 
        self.y0 = y0 
        self.x = x0 
        self.y = y0
        self.h = h

    def next_step(self):
        pass 

    def range_respostas(self, xn):
        pass

    def reset_method(self):
        self.x = self.x0 
        self.y = self.y0



class Euler(Metodo):
    def __init__(self, x0, y0, h, f):
        super().__init__(x0, y0, h)
        self.f = f

    def next_step(self):
        self.y += self.h * self.f(self.x, self.y)
        self.x = round(self.x + self.h, 2)

        return (self.x, self.y)
    

    def range_respostas(self, xn):
        x0 = self.x0 
        y0 = self.y0 

        xList = [x0]
        yList = [y0]

        n = int((xn / self.h))
        
        for i in range(n):
            x0 = round(x0 + self.h, 2)
            y0 += self.h * self.f(x0, y0)

            xList.append(x0)
            yList.append(y0)

        return xList, yList
    

class Richardson(Metodo):
    def __init__(self, x0, y0, h, f):
        super().__init__(x0, y0, h)
        self.f = f
        self.euler = Euler(x0, y0, h, f)  

        self.h = h/2
        self.y2 = y0

    def next_step(self):
        self.euler.next_step()

        self.y2 += self.h * self.f(self.x, self.y2)
        self.x = round(self.x + self.h, 2) 

        self.y2 += self.h * self.f(self.x, self.y2)
        self.x = round(self.x + self.h, 2) 

        self.y = 2*self.y2 - self.euler.y
        
        return self.x, self.y
        

    def range_respostas(self, xn):
        self.euler.reset_method()
        self.reset_method()

        xList = [self.x0]
        yList = [self.y0]

        n = int((xn / (self.h*2)))
        
        for i in range(n):
            x, y = self.next_step()
            xList.append(x)
            yList.append(y)

        return xList, yList
    

class RungeKutta(Metodo):
    def __init__(self, x0, y0, h, f):
        super().__init__(x0, y0, h)
        self.f = f 
    
    def next_step(self):
        k1 = self.f(self.x, self.y)
        k2 = self.f(self.x + self.h/2, self.y + self.h/2 * k1)
        k3 = self.f(self.x + self.h/2, self.y + self.h/2 * k2)
        k4 = self.f(self.x + self.h, self.y + self.h*k3) 

        self.y += self.h * (1/6) * (k1 + 2*k2 + 2*k3 + k4) 
        
        self.x = round(self.x+self.h,2)

        return self.x, self.y

    def range_respostas(self, xn):
        x0 = self.x0 
        y0 = self.y0 

        xList = [x0]
        yList = [y0]

        n = int((xn / self.h))
        
        for i in range(n):
            x, y = self.next_step()
            xList.append(x)
            yList.append(y)
            # x0 = round(x0 + self.h, 2)

            # k1 = self.f(x0, y0)
            # k2 = self.f(x0 + self.h/2, y0 + self.h/2 * k1)
            # k3 = self.f(x0 + self.h/2, y0 + self.h/2 * k2)
            # k4 = self.f(x0 + self.h, y0 + self.h*k3) 

            # y0 += self.h * (1/6) * (k1 + 2*k2 + 2*k3 + k4)         

            # xList.append(x0)
            # yList.append(y0)

        return xList, yList


if __name__ == '__main__':
    pass
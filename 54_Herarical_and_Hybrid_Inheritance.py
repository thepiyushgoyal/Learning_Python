import os
os.system('cls')
# Herarical
class Base:
    def show(self):
        print('base')
class D1(Base):
    def show(self):
        super().show()
        print('derived 1')
class D2(Base):
    def show(self):
        super().show()
        print('derived 2\n')
# Hybrid
class HybBase:
    def show(self):
        print('base')
class HybD1(HybBase):
    def show(self):
        print('Executed D1')
        super().show()
        print('derived 1')
class HybD2(HybBase):
    def show(self):
        print('Executed D2')
        super().show()
        print('derived 2')
class HybD3(HybD2,HybD1):
    def show(self):
        super().show()
        # HybD2.show(self)
        print('derived 3\n')

# Herarical
# d1 = D1()
# d1.show()
# d2 = D2()
# d2.show()

# Hybrid
d3 = HybD3()
d3.show()
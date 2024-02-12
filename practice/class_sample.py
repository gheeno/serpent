class Computer():
    '''
    Super class.
    '''
    def __init__(self, cpu, ram, gpu, ssd):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.ssd = ssd

    # GET AND SET is a form of abstraction.
        
    def get_cpu(self):
        return self.cpu
    
    def get_ram(self):
        return self.ram
    
    def get_gpu(self):
        return self.gpu
    
    def get_ssd(self):
        return self.ssd
    
    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_ram(self, ram):
        self.ram = ram

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_ssd(self, ssd):
        self.ssd = ssd

class Macbook(Computer):
    
    def __init__(self, cpu, ram, gpu, ssd, os, trackpad):
        # initialize the superclass.
        super().__init__(cpu, ram, gpu, ssd)
        # 
        self.os = os
        self.trackpad = trackpad

    
class MacbookPro(Macbook):
    
    def __init__(self, cpu, ram, gpu, ssd, os, trackpad, touch_bar=True, thunderbolt_ports=4):
        # Call the constructor of the superclass (Macbook)
        super().__init__(cpu, ram, gpu, ssd, os, trackpad)
        # Additional attributes specific to MacbookPro
        self.touch_bar = touch_bar
        self.thunderbolt_ports = thunderbolt_ports

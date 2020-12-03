import os

class Intcode():
    def __init__(self, data):
        
        self.data        = [each for each in data]

        self.ptr         = 0
        self.opcode_args = {1: 3,
                            2: 3,
                            3: 1,
                            4: 1,
                            5: 2,
                            6: 2,
                            7: 3,
                            8: 3,
                            99: 0}

    def __repr__(self):
        result = [self.opcode] + self.param_mode
        return "|".join([str(each) for each in result])
    
    def get_arg(self, mode, arg, data):
        if mode == 0:
            return int(data[arg])
        elif mode == 1:
            return arg

    def get_num_args(self):
        return self.opcode_args[self.opcode]

    def update_inst(self):
        opcode          = str(self.data[self.ptr])
        self.opcode     = int(opcode[-2:])
        self.param_mode = [0, 0, 0]
        if len(opcode) > 2:
            index = 0
            for each in opcode[-3:-6:-1]:
                self.param_mode[index] = int(each)
                index += 1        
            
    def run(self, ID):
        self.ID = ID
        self.update_inst()
        while self.opcode != 99:

            num   = self.get_num_args()
            args  = [int(each) for each in self.data[self.ptr+1:self.ptr+1+num]]
            msg   = ', '.join([str(x) for x in args])

            print(f"Opcode: [{self.opcode}] Args: [{msg}]")
            
            if self.opcode == 1:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                self.data[args[2]] = str(val1 + val2)

            elif self.opcode == 2:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                self.data[args[2]] = str(val1 * val2)

            elif self.opcode == 3:
                self.data[args[0]] = str(self.ID)

            elif self.opcode == 4:
                self.ID = int(self.data[args[0]])

            elif self.opcode == 5:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 > 0:
                    self.ptr = val2
                    self.update_inst()
                    continue

            elif self.opcode == 6:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 == 0:
                    self.ptr = val2
                    self.update_inst()
                    continue

            elif self.opcode == 7:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 < val2:
                    self.data[args[2]] = '1'
                else:
                    self.data[args[2]] = '0'

            elif self.opcode == 8:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 == val2:
                    self.data[args[2]] = '1'
                else:
                    self.data[args[2]] = '0'

            self.ptr += num + 1
            self.update_inst()

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), 'input\day_2.txt')
    with open(path, 'r') as f:
        lines = f.readlines()
    data = lines[0].strip().split(',')
    
    for noun in range(len(data)):
        for verb in range(len(data)):
            program = Intcode(data)
            program.data[1] = noun
            program.data[2] = verb
            program.run(None)
            if int(program.data[0]) == 19690720:
                print(100 * noun + verb)
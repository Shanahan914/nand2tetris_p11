class VMWriter:
    def __init__(self, outfile):
        self.out_file = outfile

        try:
            self.file = open(outfile, 'a')
        except Exception as e:
            raise Exception("failed to read file ({file}) due to: {e}")

    def write_pop(self, segment, index):
        pass

    def write_push(self, segment, index):
        if segment in ('CONST','ARG', 'LOCAL','STATIC', 'THIS','THAT', 'POINTER','TEMP'):
            self.file.write(f"push {segment.lower()} {index} \n")

    def write_arithmetic(self, command):
        if command in ('ADD','SUB', 'NEG', 'EQ', 'GT','LT', 'AND', 'OR', 'NOT'):
            self.file.write(f"{command.lower()} \n")
        return

    def write_label(self, label):
        pass

    def write_goto(self, label):
        pass

    def write_if(self, label):
        pass

    def write_call(self, name, nArgs):
        pass

    def write_function(self, name, nArgs):
        pass

    def write_return(self):
        pass

    def close(self):
        pass
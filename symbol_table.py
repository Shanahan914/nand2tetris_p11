class SymbolTable:

    def __init__(self):
        self.class_table = {}
        self.subroutine_table = {}
        self.STATIC_next_index = 0
        self.FIELD_next_index = 0
        self.ARG_next_index = 0
        self.VAR_next_index = 0

    
    def define(self, name, type_var, kind):
        if kind in ('STATIC', 'FIELD', 'static', 'field'):
            self.class_table[name] = {'type': type_var, 'kind': kind, 'index': self.var_count(kind)}
        elif kind in ('ARG', 'VAR', 'arg', 'var'):
            self.subroutine_table[name] = {'type': type_var, 'kind': kind, 'index': self.var_count(kind)}
        else:
            raise Exception(f'Key did not match the list of acceptable values: {kind}')
        # increment if no exception
        self._increment_index(kind)

        print(self.class_table)
        print(self.subroutine_table)

        return


    def var_count(self, kind):
        return getattr(self, f"{kind.upper()}_next_index")

    def kind_of(self, name):
        try:
            return self._get_data(name, 'kind')
        except KeyError:
            return None

    def type_of(self, name):
        return self._get_data(name, 'type')

    def index_of(self, name):
        print('name', name)
        return self._get_data(name, 'index')


    def _get_data(self, key, var):
        if key in self.class_table:
            return self.class_table[key][var] 
        elif key in self.subroutine_table:
            return self.subroutine_table[key][var]
        else:
            raise KeyError(f'Did not find given key {key} in the symbol table') 
        
    def _increment_index(self, kind):
        var_count = getattr(self, f"{kind.upper()}_next_index")
        var_count += 1 
        # Update the attribute with the new value
        setattr(self, f"{kind.upper()}_next_index", var_count)


    



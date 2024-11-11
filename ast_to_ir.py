class IRGenerator:
    def generate_ir(self, ast):
        """Generates the Intermediate Representation (IR) from the AST."""
        if ast['type'] == 'CreateTable':
            return self.generate_create_table_ir(ast)
        elif ast['type'] == 'InsertInto':
            return self.generate_insert_into_ir(ast)
        elif ast['type'] == 'Select':
            return self.generate_select_ir(ast)

    def generate_create_table_ir(self, ast):
        table_name = ast['table_name']
        columns = ast['columns']
        column_ir = [f"{col['name']} {col['datatype']}({col['length']})" if col['length'] else f"{col['name']} {col['datatype']}" for col in columns]
        return f"CREATE_TABLE({table_name}, [{', '.join(column_ir)}])"

    def generate_insert_into_ir(self, ast):
        table_name = ast['table_name']
        columns = ', '.join(ast['columns'])
        values = ', '.join(ast['values'])
        return f"INSERT_INTO({table_name}, [{columns}], [{values}])"

    def generate_select_ir(self, ast):
        columns = ', '.join(ast['columns'])
        table_name = ast['table_name']
        return f"SELECT({columns}) FROM {table_name}"

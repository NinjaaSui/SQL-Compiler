class ASTBuilder:
    def build_ast(self, parsed_data):
        """Builds an Abstract Syntax Tree from the parsed data."""
        if parsed_data['type'] == 'CreateTable':
            return {
                'type': 'CreateTable',
                'table_name': parsed_data['table_name'],
                'columns': [self.build_column_ast(col) for col in parsed_data['columns']]
            }
        elif parsed_data['type'] == 'InsertInto':
            return {
                'type': 'InsertInto',
                'table_name': parsed_data['table_name'],
                'columns': parsed_data['columns'],
                'values': parsed_data['values']
            }
        elif parsed_data['type'] == 'Select':
            return {
                'type': 'Select',
                'columns': parsed_data['columns'],
                'table_name': parsed_data['table_name']
            }

    def build_column_ast(self, column_data):
        """Build the AST for column definition."""
        return {
            'name': column_data['name'],
            'datatype': column_data['type'],
            'length': column_data['length']
        }

class SemanticAnalyzer:
    def analyze(self, ast):
        """Perform semantic analysis."""
        if ast['type'] == 'CreateTable':
            for column in ast['columns']:
                if column['datatype'] not in ['int', 'varchar']:
                    raise TypeError(f"Invalid datatype '{column['datatype']}' for column '{column['name']}'")
        elif ast['type'] == 'InsertInto':
            # Example check: Ensure column and value counts match
            if len(ast['columns']) != len(ast['values']):
                raise ValueError("Column count doesn't match value count in INSERT statement.")
        elif ast['type'] == 'Select':
            # Example check: Ensure columns are specified in SELECT statement
            if not ast['columns']:
                raise ValueError("No columns specified in SELECT statement.")

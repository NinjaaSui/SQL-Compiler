class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def consume(self):
        """Consume the current token and move to the next"""
        self.position += 1

    def current_token(self):
        """Return the current token"""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def match(self, token_type):
        """Check if the current token matches the expected type and consume it"""
        token = self.current_token()
        if token and token[0] == token_type:
            self.consume()
            return token[1]
        return None

    def parse(self):
        """Determine which statement to parse based on the first token."""
        if self.current_token()[0] == 'CREATE':
            return self.parse_create_table()
        elif self.current_token()[0] == 'INSERT':
            return self.parse_insert_into()
        elif self.current_token()[0] == 'SELECT':
            return self.parse_select()
        else:
            raise SyntaxError("Unsupported SQL statement.")

    def parse_create_table(self):
        """Parse the CREATE TABLE statement"""
        if self.match('CREATE') and self.match('TABLE'):
            table_name = self.match('IDENTIFIER')
            columns = []
            if not self.match('L_PAREN'):
                raise SyntaxError("Expected '(' after table name")

            while True:  # Loop to process column definitions
                column_name = self.match('IDENTIFIER')
                column_type = self.match('TYPE')

                # Optional length for varchar types
                length = None
                if column_type == 'varchar' and self.current_token()[0] == 'L_PAREN':
                    self.match('L_PAREN')
                    length = int(self.match('NUMBER'))
                    if not self.match('R_PAREN'):
                        raise SyntaxError("Expected ')' after varchar length")

                if column_name and column_type:
                    columns.append({'name': column_name, 'type': column_type, 'length': length})
                else:
                    raise SyntaxError("Invalid column definition")

                if not self.match('COMMA'):
                    break

            if not self.match('R_PAREN'):
                raise SyntaxError("Expected ')' at the end of column definitions")

            if not self.match('SEMICOLON'):
                raise SyntaxError("Expected ';' at the end of CREATE TABLE statement")

            return {'type': 'CreateTable', 'table_name': table_name, 'columns': columns}
        else:
            raise SyntaxError("Expected CREATE TABLE statement.")

    def parse_insert_into(self):
        """Parse the INSERT INTO statement."""
        if self.match('INSERT') and self.match('INTO'):
            table_name = self.match('IDENTIFIER')
            if not self.match('L_PAREN'):
                raise SyntaxError("Expected '(' after table name in INSERT statement")

            # Parse column names
            columns = []
            while True:
                column = self.match('IDENTIFIER')
                if column:
                    columns.append(column)
                if not self.match('COMMA'):
                    break

            if not self.match('R_PAREN'):
                raise SyntaxError("Expected ')' after column names")

            if not self.match('VALUES'):
                raise SyntaxError("Expected VALUES keyword in INSERT statement")

            if not self.match('L_PAREN'):
                raise SyntaxError("Expected '(' before values")

            # Parse values
            values = []
            while True:
                value = self.match('STRING') or self.match('NUMBER')
                if value:
                    values.append(value.strip("'"))  # Remove quotes from string literals
                if not self.match('COMMA'):
                    break

            if not self.match('R_PAREN'):
                raise SyntaxError("Expected ')' after values")

            if not self.match('SEMICOLON'):
                raise SyntaxError("Expected ';' at the end of INSERT statement")

            return {
                'type': 'InsertInto',
                'table_name': table_name,
                'columns': columns,
                'values': values
            }

    def parse_select(self):
        """Parse the SELECT statement."""
        if self.match('SELECT'):
            columns = []
            while True:
                column = self.match('IDENTIFIER')
                if column:
                    columns.append(column)
                if not self.match('COMMA'):
                    break

            if not self.match('FROM'):
                raise SyntaxError("Expected FROM in SELECT statement")

            table_name = self.match('IDENTIFIER')

            if not self.match('SEMICOLON'):
                raise SyntaxError("Expected ';' at the end of SELECT statement")

            return {
                'type': 'Select',
                'columns': columns,
                'table_name': table_name
            }

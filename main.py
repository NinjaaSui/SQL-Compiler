from compiler import compile_sql

# Example SQL query
sql_create_table = """
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
"""

sql_insert = """
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES (1, 'Doe', 'John', '123 Street', 'City');
"""

sql_select = """
SELECT PersonID, LastName FROM Persons;
"""

# Run the compiler on each query
print("CREATE TABLE Query:")
ast, ir = compile_sql(sql_create_table)
print("AST:", ast)
print("IR:", ir)

print("\nINSERT INTO Query:")
ast, ir = compile_sql(sql_insert)
print("AST:", ast)
print("IR:", ir)

print("\nSELECT Query:")
ast, ir = compile_sql(sql_select)
print("AST:", ast)
print("IR:", ir)

from lexing import *
from parsing import *
from ast_build import *
from semantic import *
from ast_to_ir import *

def compile_sql(sql_code):
    # Scanning Phase
    tokens = lexer(sql_code)
    print("Tokens:", tokens)

    # Syntax Phase
    parser = Parser(tokens)
    parsed_data = parser.parse()
    print("Parsed Data:", parsed_data)

    # AST Building
    ast_builder = ASTBuilder()
    ast = ast_builder.build_ast(parsed_data)
    print("AST:", ast)

    # Semantic Phase
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze(ast)

    # IR Generation Phase
    ir_generator = IRGenerator()
    ir = ir_generator.generate_ir(ast)
    print("IR:", ir)

    return ast, ir

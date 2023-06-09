"""
This file covers statements that don't already a colon like return
statements
"""

from src.util import components as comp
from src.util.output import StatementOutput


def transpiler_variable_declaration(transpiler,
                                    current: comp.VariableDeclaration):
    out = StatementOutput(transpiler)

    # Example of type hinting:
    # eighty_six: int
    out.add_output(transpiler.traverse(current.identifier))
    
    # Padding
    out.add_output(out.COLON)
    out.add_output(out.SPACE)

    # Add that variable type
    out.add_output(transpiler.traverse(current.variable_type))

    return out.get_output()


def transpiler_variable_initialization(transpiler,
                                       current: comp.VariableInitialization):
    out = StatementOutput(transpiler)

    # Pretty straightforward here
    out.add_output(transpiler.traverse(current.key_identifier))
    out.add_output(out.EQUALS_SIGN)
    out.add_output(transpiler.traverse(current.expression))

    return out.get_output()


def transpiler_return_statement(transpiler,
                                current: comp.ReturnStatement):
    out = StatementOutput(transpiler)

    out.add_output(out.RETURN_KW, out.SPACE)
    out.add_output(transpiler.traverse(current.expression))

    # Newline isn't needed here. If there are problems with \n
    # just know that it is not here

    return out.get_output()


def transpiler_variable_increment(transpiler,
                                  current: comp.VariableIncrement):
    out = StatementOutput(transpiler)

    out.add_output(transpiler.traverse(current.identifier))

    # Add the operators
    out.add_output(out.PLUS_SIGN)
    out.add_output(out.EQUALS_SIGN)

    # Check if the amount is the default
    if isinstance(current.amount, str):
        out.add_output(current.amount)
    else:
        out.add_output(transpiler.traverse(current.amount))

    return out.get_output()

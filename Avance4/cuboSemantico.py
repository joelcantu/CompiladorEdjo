class CuboSemantico():
    def __init__(self):
        self.cube = {
            "int" : {
                "int" : {
                    "+" : "int",
                    "-" : "int",
                    "*" : "int",
                    "/" : "int",
                    "=" : "int",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                },
                "decimal" : {
                    "+" : "decimal",
                    "-" : "decimal",
                    "*" : "decimal",
                    "/" : "decimal",
                    "=" : "decimal",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                }
            },
            "decimal" : {
                "int" : {
                    "+" : "decimal",
                    "-" : "decimal",
                    "*" : "decimal",
                    "/" : "decimal",
                    "=" : "decimal",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                },
                "decimal" : {
                    "+" : "decimal",
                    "-" : "decimal",
                    "*" : "decimal",
                    "/" : "decimal",
                    "=" : "decimal",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                }
            },
            "bool" : {
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                },
                "decimal" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "bool",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                }
            },
            "string": {
                "int": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                },
                "decimal": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                },
                "bool": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                },
                "string": {
                    "+": "string",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "string",
                    "==": "bool",
                    "!=": "bool",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                }
            }
        }

    def get_semantic_type(self, left_type, right_type, operator):
        return self.cube[left_type][right_type][operator]

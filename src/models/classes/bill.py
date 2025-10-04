class bill:

    def __init__(name, value, debtor, due_day, statements, actual_statement, statement_value=None, remaining=None, type=None):
        
        debtor : str = debtor
        name : str = name
        value : float = value
        due_day : int = due_day
        statements : int = statements
        actual_statement : int = actual_statement
        statement_value : int = statement_value
        remaining : float = remaining
        type : str = type

class User:

    def __init__(id, fullname, email, password_hash, salary, salary_day, debtors=None, to_pay=None):

        id : str = id
        
        fullname : str = fullname
        firstname : str = fullname.split(" ")[0]
        lastname :str = fullname.split(" ")[-1]
        email : str = email
        password_hash : str = password_hash

        salary : float = salary
        salary_day : int = salary_day

        debtors : list = debtors
        to_pay : float = to_pay


    



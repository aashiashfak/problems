def calculate_parenthesis_count(s):
    """
    Calculate the number of opening and closing parentheses in a string.
    """
    opening_count_p = s.count('(')
    closing_count_P = s.count(')')
    
    if  opening_count_p != closing_count_P:
        return ValueError("Unbalanced parentheses")
    
    opening_count_s = s.count('[')
    closing_count_S = s.count(']')
    
    if   opening_count_s != closing_count_S:
        return ValueError("Unbalanced square brackets")
    
    opening_count_c =  s.count('{')
    closing_count_c = s.count('}')
    
    if opening_count_c !=  closing_count_c:
        return("Unbalanced curly brackets")
    
    return " Balanced Brackets"

       
s_1 = "()(]){}["
print(calculate_parenthesis_count(s_1))




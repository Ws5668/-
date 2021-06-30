
import money




salary_money = 1000

def select_money():
    if money.get_money == True:
        print(f"现在存款为{money.saved_money+salary_money}")
    else:
        print(f"现在存款为{money.saved_money}")
select_money()


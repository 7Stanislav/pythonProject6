def my_func():
    work_h = int(input("Введите выработку в часах"))
    bid = int(input("Введите ставку в час"))
    prem = int(input("Введите размер премии"))
    sal = work_h * bid + prem
    print(f'З/п сотрудника = {sal}')


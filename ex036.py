print("=-=" * 20)
print("\033[34mHousing Loan Simulator\033[m")
print("=-=" * 20)
print("\nEnter the desired loan terms:\n")

amount = float(input("Loan amount: "))
tenure = float(input("Loan term: "))
salary = float(input("Monthly income: "))

mt = amount // (tenure * 12)

if mt <= (salary * 0.30):
    print("\n\033[32mLoan approved!\033[m")
else:
    print("\n\033[31mLoan reproved.\033[m")

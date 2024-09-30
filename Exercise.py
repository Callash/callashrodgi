from datetime import datetime

def calculate_fine(due_date, return_date):
    overdue_days = (return_date - due_date).days
    
    if overdue_days <= 0:
        return 0
    elif 1 <= overdue_days <= 7:
        return overdue_days * 20
    elif 8 <= overdue_days <= 14:
        return overdue_days * 50
    else:
        return overdue_days * 100

def main():

    booking_date_str = input("Enter booking date (YYYY-MM-DD): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    return_date_str = input("Enter return date (YYYY-MM-DD): ")

    
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    return_date = datetime.strptime(return_date_str, '%Y-%m-%d')

    # Calculate fine
    fine = calculate_fine(due_date, return_date)
    
    if fine > 0:
        print(f"The fine for overdue books is Ksh {fine}.")
    else:
        print("No fine, the book is returned on time.")

if __name__ == "__main__":
    main()

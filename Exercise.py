from datetime import datetime

def calculate_fine(due_date, return_date):
    overdue_days = (return_date - due_date).days
    
    if overdue_days <= 0:
        return 0, 0  # No fine if returned on or before the due date
    elif 1 <= overdue_days <= 7:
        fine_rate = 20
        fine_amount = overdue_days * fine_rate
    elif 8 <= overdue_days <= 14:
        fine_rate = 50
        fine_amount = overdue_days * fine_rate
    else:  # 15 days or more
        fine_rate = 100
        fine_amount = overdue_days * fine_rate
    
    return overdue_days, fine_rate, fine_amount

def main():
    # User input for Book ID, Due Date, and Return Date
    book_id = input("Enter Book ID: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    return_date_str = input("Enter return date (YYYY-MM-DD): ")

    # Convert input strings to datetime objects
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    return_date = datetime.strptime(return_date_str, '%Y-%m-%d')

    # Calculate fine details
    days_overdue, fine_rate, fine_amount = calculate_fine(due_date, return_date)

    # Display the result
    print("\n--- Fine Details ---")
    print(f"Book ID: {book_id}")
    print(f"Due Date: {due_date.date()}")
    print(f"Return Date: {return_date.date()}")
    print(f"Days Overdue: {days_overdue}")
    print(f"Fine Rate: Ksh {fine_rate} per day")
    print(f"Fine Amount: Ksh {fine_amount}")

if __name__ == "__main__":
    main()

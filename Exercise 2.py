def is_palindrome(s: str) -> bool:
    normalized_str = ''.join(s.split()).lower()
    return normalized_str == normalized_str[::-1]

def filter_even_numbers(numbers: list) -> list:
    
    return [num for num in numbers if num % 2 == 0]

print(is_palindrome("A man a plan a canal Panama"))  

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  

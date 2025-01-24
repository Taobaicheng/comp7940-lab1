def find_factors(num_list):
    for num in num_list:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        
        print("Factors of", num, "are:", factors)


l = [52633, 8137, 1024, 999]
find_factors(l)
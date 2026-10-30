# WAF to print the length of a list (list the parameter )
# cities = ["delhi", "pune", "noida", "gurgaon"]
# heroes = ["thor", "ironman","captain america","shaktiman"]
# def print_len(lens):
#     print(len(lens))

# print_len(cities)
# print_len(heroes)



#WAF to convert USD to INR. 
 
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =",inr_val, "INR")

# converter (1)

# a =int(input("Enter a number"))

# def fun (a):
#     if a%2 == 0 :
#         print("Even")
#     else :
#         print("odd")

# fun(a)

# def show(n):
#     if (n == 0):
#         return

#     print(n)
#     show(n-1)

# show(5)

def calc_sum(n):
    if(n ==0):
        return
    print(n)
    calc_sum(n-1)
 

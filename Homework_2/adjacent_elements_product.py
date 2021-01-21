sequence = input("Enter a sequence of numbers: ")
seq_int = [int(i) for i in sequence.split()]
product_list = [seq_int[i] * seq_int[i + 1] for i in range(len(seq_int) - 1)]
print(max(product_list))

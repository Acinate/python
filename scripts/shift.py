# Swaps adjacent characters in a string to produce a type of encryption

message = list("eTllm  ebauo toyruf varoti eub.gy yb2agawtte6v6p@ferbdlaolnoesucirytc.mo")

for i in range(len(message) - 1, 0, -2):
    swap = message[i - 1]
    message[i - 1] = message[i]
    message[i] = swap

print("".join(message))

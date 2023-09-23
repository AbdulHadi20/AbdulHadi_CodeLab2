# consider a loop that counts form 1 to 10, but prints only odd numbers

count = 0

while True:
    if count <= 10 and count % 2 == 1:
        count += 1
        print(count)

    else:
        break

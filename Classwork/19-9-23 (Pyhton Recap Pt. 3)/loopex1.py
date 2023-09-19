# consider a loop that counts form 1 to 10, but prints only odd numbers

count = 1

while count <= 10:
    count += 1
    if count % 2 == 0:

        continue

    else:
        print(count)

        break

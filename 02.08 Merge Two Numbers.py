x = int(input('Enter First 2 Digit Number: '));
y = int(input('Enter Second 2 Digit Number: '));

z = int(x / 10);

z = z * 10 + int(y / 10);

z = z * 10 + x % 10;

z = z * 10 + y % 10;

print("Merge Number: {}".format(z))

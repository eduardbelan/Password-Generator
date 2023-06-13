# Password Generator

This is a password generator program. It lets you choose:
+ length, 
+ composition, 
    + num of letters
    + num of symbols
    + num of numbers
+ additional secret words.

There is an overview of the password composition and a password strength check after the program terminates.

## Requirements

- Python

## Getting Started

1. Clone this repository.
2. Ensure you have Python installed on your machine.
3. Open a terminal and navigate to the directory where the `pw-generator.py` file is located.
```bash
cd C:\Users\username\Downloads\repo
```
4. Run the script using the following command:

```bash
python pw-generator.py

# or enter the path directly
python C:\Users\username\Downloads\repo\pw-generator.py
```

## Example
```bash
How many letters would you like? 3

How many symbols would you like? 3

How many numbers would you like? 3

How many secret words would you like? 2
Enter the 1st secret word: hi
Enter the 2nd secret word: hej

Order not randomised.
Your Password: NKV)++002hihej

Order randomised.
Your Password: 2hi++)V0K0Nhej

Your Password contains:
        3 letters: N, K, V
        3 symbols: ), +, +
        3 numbers: 0, 0, 2
It also contains 2 secret words: hi, hej

Password is safe.
```

## License
Password-Generator is released under the [MIT License](https://opensource.org/licenses/MIT).

**Note:** This program is provided as-is without any warranty. Use it at your own risk.

## Contributions
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue on the GitHub repository.

Leave the days of 'password' or 'password12345' in the past with this Password Generator, which can still create a password like that if you really wanted to.<br>
But let's aim for something stronger and more secure, shall we?
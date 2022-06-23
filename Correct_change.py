total = float(input("What is the total: "))
costomer_amount = float(input("What did the costomer hand you: "))

#Take total and subtract the costomer_amount

change = total - costomer_amount

hundred = change / 100
hundred_r = change % 100
fifty = hundred_r / 50
fifty_r = hundred_r % 50
twenty = fifty_r / 20
twenty_r = fifty_r % 20
tens = twenty_r / 10
tens_r = twenty_r % 10
fives = tens_r / 5
fives_r = tens_r % 5
ones = fives_r / 1
ones_r = fives_r % 1
quarter = ones_r / .25
quarter_r = ones_r % .25
dimes = quarter_r / .10
dimes_r = quarter_r % .10
nickel = dimes_r / .05
nickel_r = dimes_r % .05
pennys = nickel_r / .01

print (f""""
$100 - {int(hundred)}
$50 - {int(fifty)}
$20 - {int(twenty)}
$10 - {int(tens)}
$5 - {int(fives)}
$1 - {int(ones)}
$.25 - {int(quarter)}
$.10 - {int(dimes)}
$.05 - {int(nickel)}
$.01 - {int(pennys)}
""")

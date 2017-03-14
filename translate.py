# Assignment: Turn your user into a l33t h4x0r


user_input = input("Enter some text: ")
user_input = user_input.lower()

leetspeak = user_input.replace('a','4')
leetspeak = leetspeak.replace('b','8')
leetspeak = leetspeak.replace('e','3')
leetspeak = leetspeak.replace('l','1')
leetspeak = leetspeak.replace('o','0')
leetspeak = leetspeak.replace('s','5')
leetspeak = leetspeak.replace('t','7')


print(leetspeak)

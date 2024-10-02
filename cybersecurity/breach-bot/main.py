#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What's your name? \n")
print("\nNice to meet you, " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("\nWow! That means it has been " + str(timePassed) + " years since the Facebook breach took place!")

#Introduces breach
print("\nWould you like to about the Facebook breach of 2019?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization' response, (c) I would like to hear your response")
  topic = input()

  if topic.lower() == "a":
    print("\nMalicious actors hacked into Facebook and retrieved phone numbers, full names, locations, some email addresses, and other details from user profiles by exploiting a vulnerability in a now-defunct feature on the platform that allowed users to find each other by phone number.")

  elif topic.lower() == "b":
    print("\nFacebook claimed that it found and fixed the issue; the company believed that affected users were not in a position to fix the issue themselves.")

  elif topic.lower() == "c":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take??")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print( "\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) whether or not you agree with the organization's response, (b) my reaction, (c) my advice, or (d) none")
  topic = input()

  if topic.lower() == "a":
    print("\nThe breach relates to confidentiality because users’ personal data that was supposed to be private was accessed by malicious actors.")

  elif topic.lower() == "b":
    print("\nI disagree with the organization's response because the affected individuals were not notified and the data was not recovered. This lack of transparency would limit the affected party’s awareness and their ability to protect themselves.")

  elif topic.lower() == "c":
    print("\nMy advice would be to create a strong password and be wary while using public networks.")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")

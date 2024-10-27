import time

print("========= Welcome to Kaun Banega Crorepati =========")
user_name = input('Enter your name, please: ')

print(f'Hello {user_name}, the game contains 5 questions and you will be rewarded after each correct answer.')
print('Let\'s Begin the Game\n')

# Questions and their correct answers
qa_list = [
    ('What is the Currency of Pakistan?', ['A: Pakistani Rupee', 'B: Pakistani Dollar', 'C: Pakistani Riyal', 'D: Pakistani Pound'], 'A'),
    ('What is the National Animal of Pakistan?', ['A: Deer', 'B: Markhor', 'C: Peacock', 'D: Tiger'], 'B'),
    ('What is the name of Founder of Pakistan?', ['A: Liaqat', 'B: Iqbal', 'C: Jinnah', 'D: Nehru'], 'C'),
    ('Who is the National Poet of Pakistan?', ['A: Liaqat', 'B: Azad', 'C: Jinnah', 'D: Iqbal'], 'D'),
    ('What is the National Drink of Pakistan?', ['A: Lassi', 'B: Rooh Afza', 'C: Thadhal', 'D: Sugarcane Juice'], 'D')
]

prize_money = [100000, 1000000, 2000000, 3000000, 3900000]
total_prize = 0

# Loop through questions
for i, (question, options, correct_answer) in enumerate(qa_list):
    print(f"Question {i+1}: {question}")
    for option in options:
        print(option)
    
    # Take the user's answer
    user_answer = input("Your answer (A, B, C, D): ").upper()
    
    if user_answer == correct_answer:
        total_prize += prize_money[i]
        print(f'Correct Answer! You now have {total_prize} PKR.\n')
    else:
        print(f'Wrong Answer. You won {total_prize} PKR. Better luck next time!')
        quit()

    # Adding a short delay to make the experience smoother
    
    time.sleep(3)

print(f'Congratulations {user_name}! You Won {total_prize} PKR (1 CRORE)!')

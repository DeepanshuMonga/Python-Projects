import time
import threading
from inputimeout import inputimeout, TimeoutOccurred 
questions_list=["1. Who wrote Sherlock Holmes?","2. In Harry Potter, what position does Harry play in Quidditch?","3. What is the first book in The Lord of the Rings series?","4. What classic novel features the character Jay Gatsby?","5. Who is the author of 'A Song of Ice and Fire', the book series that inspired Game of Thrones?","6. What does HTML stand for?","7. In Python, what data structure is immutable: list or tuple?","8. What is the time complexity of a binary search algorithm?","9. Which programming language is known for having 'write once, run anywhere' capability?","10. What does the term 'recursion' mean in programming?","11. What is the name of Iron Man’s AI assistant before FRIDAY?","12. What was the first MCU film to cross $2 billion at the box office?","13. Which movie won the Oscar for Best Picture in 2023?","14. What is the highest-grossing animated movie of all time?","15. Who is the main villain in Doctor Strange in the Multiverse of Madness?","16. What is the rarest blood type in humans?","17. Who was the first person to step on the moon?","18. What is the speed of light in vacuum (in km/s)?","19. What is the national sport of Japan?","20. What is the formula of the complex cisplatin, a chemotherapy drug?"]
options_list=["1. J.R.R. Tolkien\n2. Agatha Christie\n3. J.K. Rowling\n4. Arthur Conan Doyle","1. Beater\n2. Seeker\n3. Chaser\n4. Keeper","1. The Fellowship of the Ring\n2. The Two Towers\n3. The Return of the King\n4. The Hobbit","1. To Kill a Mockingbird\n2. The Great Gatsby\n3. Moby-Dick\n4. The Catcher in the Rye","1. J.R.R. Tolkien\n2. George R.R. Martin\n3. J.K. Rowling\n4. Suzanne Collins","1. HyperText Markup Language\n2. High Text Markup Language\n3. Hyper Transfer Markup Language\n4. HyperText Management Language","1. List\n2. Tuple\n3. String\n4. Dictionary","1. O(n)\n2. O(log n)\n3. O(n log n)\n4. O(1)","1. C\n2. Java\n3. Python\n4. Ruby","1. Repeating a block of code until a condition is met\n2. Calling a function within itself\n3. Running code in parallel\n4. Running code in a loop","1. JARVIS\n2. VISION\n3. ULTRON\n4. PEPPER","1. Avengers: Infinity War\n2. Avengers: Endgame\n3. Black Panther\n4. Spider-Man: No Way Home","1. Everything Everywhere All at Once\n2. The Fabelmans\n3. Top Gun: Maverick\n4. Avatar: The Way of Water","1. The Lion King\n2. Frozen II\n3. Toy Story 4\n4. Frozen","1. Kang the Conqueror\n2. Scarlet Witch\n3. Loki\n4. Ultron","1. A+\n2. O-\n3. AB-\n4. B+","1. Buzz Aldrin\n2. Neil Armstrong\n3. John Glenn\n4. Alan Shepard","1. 300,000 km/s\n2. 150,000 km/s\n3. 186,000 km/s\n4. 200,000 km/s",'1. Baseball\n2. Sumo\n3. Karate\n4. Judo',"1. [Pt(NH₃)₂Cl₂]\n2. [Co(NH₃)₆]³⁺\n3. [Fe(CN)₆]⁴⁻\n4. [Ag(NH₃)₂]⁺"]
solutions_tuple=(4,2,1,2,2,1,2,2,2,2,1,2,1,2,2,3,2,1,2,1)
time.sleep(1.8)
print('\nWelcome to "The Geeky Gauntlet Quiz: Code, Movies & More!" 💻🎬📚')
time.sleep(1.9)
print("The rules of this Quiz are : ")
time.sleep(1.7)
print("1. There are 20 questions in all.")
time.sleep(1.7)
print("2. You will be given 15 seconds time limit for each question.")
time.sleep(1.7)
print("3. Each question carries 1 Mark.")
time.sleep(1.7)
print("4. There is no negative marking.")
time.sleep(1.7)
print("Let's start our Quiz - ")
total_ques=len(questions_list)
correct_ques=0
missed_ques=0
incorrect_ques=0
for i in range(0,total_ques):
    time.sleep(1)
    print("\n")
    print(questions_list[i])
    time.sleep(2)
    print(options_list[i])
    try:
        user_choice=int(inputimeout(prompt="Enter your option(1-4) : ",timeout=15))
    except TimeoutOccurred:
        print("\nTime is over! Moving forward to the next question.")
        missed_ques+=1
        user_choice = None
    if(user_choice==solutions_tuple[i]):
        correct_ques+=1
print("\nQuiz is over. Let's calculate your result : ")
time.sleep(2)
print("\n... Calculating ...\n")
time.sleep(2)
print("You got : ")
time.sleep(1.5)
incorrect_ques=total_ques-correct_ques-missed_ques
print("Correct Answers :",correct_ques)
time.sleep(1.7)
print("Incorrect Answers :",incorrect_ques)
time.sleep(1.7)
print("Missed Questions :",missed_ques)
time.sleep(1.8)
print("Thanks for Playing!\nHope you enjoyed the Quiz!\nHave a Good Day ahead!")
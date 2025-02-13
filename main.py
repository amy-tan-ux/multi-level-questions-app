import tkinter as tk
import time
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.attributes('-fullscreen', True)  # Make the window full screen
        self.root.configure(bg="dark red")  # Set the background color to dark red
        self.custom_font = ("Myriad", 16, "bold")

        self.finalScore = 0
        self.level = 0
        self.depleted = []
        self.remainingCounter = 0
        # Questions to ask when all categories are depleted
        self.qremaining = ["What is something you are looking forward to recently?", "What is your best advice in life?", "What is your best advice in relationships?", "What is your top 5 favourite advice?", "What is your least favourite advice?", "List 5 of your favourite books?", "List 5 of your favourite songs?", "List 5 of your favourite things?", "What is your top 5 greatest fear in life?", "What is something you've always wanted but never had?", "What is something you own that you will never give away?", "Where is your secret escape?", "What is your go-to excuse you always use?", "What is the philosophy you follow in life?"]
        # List of questions split into different categories
        self.qlist = {
            0: ["What is your favourite colour?", 
            "What is your favourite quote?",
            "What is your favourite song?",
            "What is your favourite city?",
            "What is your favourite utensil?",
            "What is your favourite appliance?",
            "What is your favourite piece of clothing garment?",
            "What is your favourite artist?",
            "What is your favourite animal"],
            1: ["If you were a season what would you be?",
            "If you were an animal what would you be?",
            "If you were a plant what would you be?",
            "If you were an inanimate object, what would you be?",
            "If you were a superhero who would you be?",
            "If you were a supervillan who would you be?",
            "If you were a tool, what would you be?",
            "If you were bread, what would you be?"],
            2: ["ocean or montains?", "flowers or trees?", "coffee or tea?",
             "night or evening?", "pencil or pen?", "phone or laptop?", "Omelette or quiche?", "spegetti or ramen?",
             "coissant or buns?", "muffins or cupcakes?", "chocolate or chips?"  ],
            3: ["If you could bend time would you visit the future or the past?",
            "If you have to be stuck in time would you choose to be stuck in the future or the past?",
            "do you spend more time thinking about the future or the past?"],
            4: ["If you have all the time in the world, what is something you would learn",
            "If you have all the time in the world, what do you see yourself doing",
            "What is something you wish you could do that breaks the law of physics?",
            "What is something you wish you could do more of?",
            "What is the last thing you've done for the first time?",
            "If you could magically pick up a new skill in an instant, what skill would you choose?"],
            5: ["Whats your favourite song or soundtrack for doing focused work?", 
            "What would be your entrance sound/ song every time you enter a room?",
            "You're cooking for the whole team, what is your signiture dish?",
            "If you could safely eat an inedible object, what would it be?",
            "What song best describes how your week has been?",
            "What food dish best describes how your week has been?",
            "What book or passage best describe how your week has been?", "Do you have a non-work goal you’re working toward right now? What is it?",
            "What trait do you admire the most in others?",
            "What trait do you admire the most in others?",
            "What is your favourite trait about yourself?",
            "What  makes someone a good team member?"]
        }
        self.askedQuestions = {0:[], 1: [], 2:[], 3:[], 4:[], 5:[]}
        self.clist = ["Picking Favourites!","Hypothetically...", "Choose ONE", "Time Traveller", "Wishing Well", "Tell Me About Yourself!"]
        self.current_question = 0
        self.start_time = None
        
        self.main_frame = tk.Frame(root, bg="dark red")
        self.main_frame.pack(expand=True)
        
        self.start_button = tk.Button(self.main_frame, text="Start", command=self.start_quiz, font=self.custom_font, bg="dark red", fg="white")
        self.start_button.pack(pady=20)
        
        self.question_category = tk.Label(self.main_frame, text="", wraplength=300, font=self.custom_font, bg="dark red", fg="white")
        self.question_category.pack(pady=20)
        
        self.question_label = tk.Label(self.main_frame, text="", wraplength=300, font=self.custom_font, bg="dark red", fg="white")
        self.question_label.pack(pady=20)
        
        
        self.submit_button = tk.Button(self.main_frame, text="Next Question", command=self.submit_answer, font=self.custom_font, bg="dark red", fg="white")
        self.submit_button.pack(pady=10)
        
        self.timer_label = tk.Label(self.main_frame, text="Time left: 60 seconds", bg="dark red")
        self.timer_label.pack(pady=10)
        
        self.restart_button = tk.Button(self.main_frame, text="Restart", command=self.start_quiz, font=self.custom_font, bg="dark red", fg="white")
        
    def start_quiz(self):
         # Show restart button
        self.question_label.config(text = "")
        self.finalScore = 0
        self.remainingCounter = 0
        self.level = 0
        self.askedQuestions = {0:[], 1: [], 2:[], 3:[], 4:[], 5:[]}
        self.depleted = []
        self.restart_button.pack(pady=20)
        self.start_button.pack_forget()
        self.start_time = time.time()
        self.current_question = 0
        self.show_question()
        self.update_timer()
        self.root.after(60000, self.end_quiz)  # End quiz after 1 minute

    def find_unasked_question(self, askedQuestion, askedQuestionList, modSize):
        print(askedQuestionList)
        while askedQuestion in askedQuestionList:
            return self.find_unasked_question((askedQuestion + 1) % modSize, askedQuestionList, modSize)
        
        return askedQuestion


    def show_question(self):

        if self.remainingCounter == len(self.qremaining)-1:
            self.question_category.config(text="")
            self.question_label.config(text="No More Questions to Display")

        elif len(self.depleted) == 6:
            self.finalScore +=1
            self.remainingCounter += 1
            self.question_category.config(text="Final Questions")
            self.question_label.config(text=self.qremaining[self.remainingCounter -1])
        
        elif self.level % 6 in self.depleted:
            self.level += 1
            self.show_question()

        # case where all questions are asked
        elif len(self.askedQuestions.get(self.level % 6)) == len(self.qlist.get(self.level % 6)):
            self.depleted.append(self.level % 6)
            self.level += 1
            self.show_question()

        else:
            self.finalScore +=1
            questionModSize = len(self.qlist.get(self.level % 6))
            randomIndex = random.randint(0,len(self.qlist.get(self.level % 6))-1)
            print(randomIndex)
            questionIdex = self.find_unasked_question(randomIndex, self.askedQuestions.get(self.level % 6), questionModSize )
            self.askedQuestions[self.level % 6] += [questionIdex]
            print(self.askedQuestions)
            self.question_category.config(text=self.clist[self.level % 6])
            self.question_label.config(text=self.qlist.get(self.level % 6)[questionIdex])            
            self.level += 1
        
    def submit_answer(self):
        if time.time() - self.start_time < 60:
            self.current_question += 1
            self.show_question()
        else:
            self.end_quiz()
    
    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = int(60 - elapsed_time)
        
        # Calculate color gradient from orange to dark red
        red_value = int(255 * (1 - remaining_time / 60))
        green_value = int(165 * (remaining_time / 60))
        color = f'#{red_value:02x}{green_value:02x}00'
        
        if remaining_time > 0:
            self.timer_label.config(text=f"Time left: {remaining_time} seconds", font=self.custom_font, fg=color)
            self.root.after(1000, self.update_timer)
    
    def end_quiz(self):
        self.question_label.config(text="Thank you for playing!! Your Final Score is: " + str(self.finalScore))
        self.question_category.config(text="")
        self.timer_label.config(text="Time left: 60 seconds")
        

    def restart_quiz(self):
        # Hide restart button and show start button
        self.restart_button.pack_forget()
        self.start_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    
    # Add a close button to end the app
    close_button = tk.Button(app.main_frame, text="Close", command=root.destroy, bg="dark red", fg="white")
    close_button.pack(pady=10)

    root.mainloop()

### Psuedo-Code for Triva project 
### initiate Trivia as Class
### def ___init___(self, question,answer ,player = 0 score = 0, question_amount = 0):
###### self.question = question
###### self.answer = answer
###### self.score = 0
###### self.player = 0
###### self.qnumb = 0
###### self.question_amount = 0
### def player_numb(self, player_amount):
##### intialize player_amount as integer input "How many players will be playing"
##### multi_play = player_amount is greater than 1 and less than 5
###### while multi_play is false and does not equal 0
###### play_name = input("Enter player name")
######## if player_amount is equal to 1:
########## print (play name)
#########elif player_amount is greater than 1:
######### multi_play becomes true
##########for i in range of player_ amount:
############
########## return multi_play
### def create_question(self, questions):
###### questions =[]
######with open file 'popculturequestions' as file:
###### for i in file:
############print(i)
### def give_answer(self):
###### intialize answer as input "Enter Answer: "
###### if answer is not equal to question:
####### except ValueError "Wrong! The answer is ", answer
## def next_question(self):
##### if self.question is less than the length of self.questions_amount
####### return self.question
class Trivia:
    def ___init___(self, question,answer,score = 0, question_amount = 0):
        self.question = question
        self.answer = answer
        self.score = score
        self.qnumb = 0
        self.question_amount = question_amount
    def player_numb(self, player_amount = 0):
            player_amount = int(input("How many player will be playing?: "))
            multi_play = player_amount > 1 and player_amount < 5
            while multi_play == False :
                play_name = input("Enter player name")
                if self.player == 1:
                    print(play_name)
                elif self.player < 1:
                     multi_play = True 
                     self.player += player_amount
                     print(play_name)
    
    def create_question(self,questions): # handles the creation and storage of each questions
        questions = []
        with open('easymodeqs.py') as file:
            emrip = file.strip('\n')
            for i in file:
                questions.append(i)
    
    def give_answer(self, i_answer,c_answer,score): # handles the organization of each answer corrilated to its question
        self.score += score
        i_answer = input("Enter Your Answer: ")
        if i_answer == c_answer:
            print("Correct!," play_name,"You earned a point")
            self.score += score
        else: 
            return "Incorrect!"
        # while answer!= "quit":
        #     try:
        #         self.answer = input("Enter Your Answer: ")
        #         for question_c in self.questions:
        #             question_c = answer

        #     except ValueError:
        #         print("Wrong! The answer is ", answer)
    def next_question(self):
        if self.qnumb > len(self.question_amount):
            return self.question



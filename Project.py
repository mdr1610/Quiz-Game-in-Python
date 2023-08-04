

from ast import Name
import getpass
import random
from string import ascii_lowercase

def play():
 print("Welcome Dear user")
 mid=input("What is your Name: ")
 print(mid)
 print("Lets Begin")
 NUM_QUESTIONS_PER_QUIZ = 10
 QUESTIONS ={
      "Number of primitive data types in Java are?": [
        "8",
        "6",
        "4",
        "3",
    ],
      "(Java)Find the output of the following code:\n"
       "String str = “Hellow”;\n"
       "System.out.println(str.indexOf(‘t))" :[
        "-1",
        "0",
        "1",
        "true",
    ],
      "Which of these are selection statements in Java?": [
        " if()",
        " for", 
        " break", 
        "continue",
   ],
      "Which environment variable is used to set the java path?":[
       "JAVA_HOME",
       "Maven_Path",
       "Java",
       "Java Path",
   ],
      "What is the numerical range of a char data type in Java?":[
       "0 to 65535",
       "0 to 32767",
       " -128 to 127",
       " 0 to 256",
   ],
      "Which of these keywords is used to define interfaces in Java?":[
       " interface",
       "Interface",
       "-intf",
       "Intf",
   ],
     "(Java) Which one of the following is not an access modifier?":[
       "Void",
       "Private",
       "Public",
       "Protected",
   ],
      "(Java) Which of these class is superclass of String and StringBuffer class?":[
       "java.lang",
       "java.util",
       "ArrayList",
       "None of the mentoined",
   ],
      "Arrays in java are-?":[
       "object",
       "object references",
       "Primitive data types",
       "None of the mentoined",
   ],
    "(Java) When an array is passed to a method, what does the method receive??":[
       "The reference of the array",
       "A copy of the array",
       "length of the array",
       "copy of first element",
   ],
     "(Python) What will be the datatype of the var in the below code snippet?\n var=10\n print(type(var))\n var = ''Hello''\n Print (type(var))": [
        "int and str",
        "int and int",
        "str and int",
        "str and str",
    ],
    "What is the maximum length of a Python identifier?": [
        "No fixed length",
        "32",
        "16",
        "None of these",
    ],
     "Which of the following concepts is not a part of Python?": [
        " Pointers", 
        " Loops", 
        " Dynamic Testing", 
        "None of These",
   ],
    "What do we use to define a block of code in Python language?":[
       "Indentation",
       "Key",
       "Brackets",
       "None of these",
   ],
    "Which of the following is not a keyword in Python language?":[
       "val",
       "raise",
       "try",
       "width",
   ],
    "(Python) import math abs(math.sqrt(36)),What will be the output of this code?":[
       "6.0",
       "6",
       "-6",
       "Error",
   ],
    "(Python) Which of the following declarations is incorrect?":[
       "None of these",
       "_x=2",
       "__x=3",
       "__xyz_=5",
   ],
    "What is the method inside the class in python language?":[
       "Function",
       "Object",
       "Attribute",
       "Argument",
   ],
    "(Python) What will be the type of the variable sorted_numbers in the below code snippet?\n numbers = (4, 7, 19, 2, 89, 45, 72, 22)\n sorted_numbers = sorted(numbers)\n print(sorted_numbers)":[
       "List",
       "Tuple",
       "String",
       "Int",
   ],
    "Which of the following functions converts date to corresponding time in Python?":[
       "strptime()",
       "strftime()",
       "Both of the these",
       "None of these",
   ],
  "HTML stands for": [
        "Hyper Text Markup Language",
        "High Text Machine Language",
        "Hypertext and links Markup Language",
        "None of these",
    ],
    "(HTML) Which charecter is used to represent the closing of a tag" :[
        "/",
        "{}",
        "!",
        "..",
    ],
     "(HTML)How to create an ordered list": [
        "<ol>",
        "<ul>", 
        "<li>", 
        "<i>",
   ],   
      "Which Html tag is used to display the power in expression i.e(X^2-Y^2)?":[
       "<sup>",
       "<sub>",
       " <p>",
       "None of the mentoined ",
   ],
    "(HTML) Which of the following is used to create a combo box(or drop down box)":[
       "<select>",
       "<list>",
       "<input type=''dropdown''> ",
       "<ul>",
   ],
   
    " Which of the following is the correct way to send mail in HTML":[
       "<a href=''Mohan:abc@gmail.com''>",
       "a href=''abc@gmail.com''",
       "<mail>abc@gmail.com</mail>",
       "None of the mentoined",
   ],
    " Which HTML element is used for YouTube videos?":[
       "<iframe> ",
       "<frame>",
       "<small>",
       "<samp>",
   ],
    "HTML is a subset of":[
       "SGML",
       "SGMT",
       "SGME",
       "XHTML",
   ],
    "Which of the following tag is used to create a text area in HTML Form?":[
       "<textarea></textarea> ",
       "<text></text>",
       "<input type=”text” />",
       "<input type=”textarea” />",
   ],
    "(HTML) Which works similar to <b> element?":[
       "<strong>",
       "<blockquote>",
       "<em>",
       "<i>",
   ],
     "PHP stands for ": [
       "Hypertext Preprocessor",
       "Pretext Hypertext Preprocessor",
       "Personal Home Processor",
       "None of these",
    ],
      "Variable name in PHP starts with" :[
        "$ (Dollar)",
        "& (Ampersand)",
        "! (Exclamation)",
        "..",
    ],
      "Which of the following is not a variable scope in PHP?": [
        "Extern",
        "Local", 
        "Static", 
        "Global",
   ],
    "Which of the following PHP function is used to generate unique id?":[
      "uniqueid()",
      "id()",
      "mdid()<p>",
      "None of the mentoined ",
   ],
    " Which of the following is the correct way of defining a variable in PHP?":[
       "$variable_name = value;",
       "$variable name = value;",
       "$variable_name = value",
       "$variable name as value;",
   ],
    " What is the use of sprintf() function in PHP?":[
      "The sprintf() function is used to send output to variable",
      "The sprintf() function is used to print the output of program",
      "Both of the above",
      "None of the mentoined",
   ],
    "Which of the following function is used to find files in PHP?":[
       "glob()",
       "fold()",
       "file()",
       "None of the mentoined",
   ],
    "What does SPL stands for in PHP?":[
       "Standard PHP Library",
       "Simple PHP Library",
       "Simple PHP List",
       "None of the above",
   ],
    "Which of the following function is used to get the ASCII value of a character in PHP?":[
       "chr() ",
       "ascii()",
       "val()",
       "asc()",
   ],
    "Which PHP function is capable to read specific number of characters from a file?":[
       "fgets()",
       "fget()",
       "fileget()",
       "None of the above",
   ],
  }
 num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
 questions = random.sample(list(QUESTIONS.items()), k=num_questions)

 num_correct = 0
 for num, (question, alternatives) in enumerate(questions, start=1):
     print(f"\nQuestion {num}:")
     print(f"{question}?")
     correct_answer = alternatives[0]
     labeled_alternatives = dict(
            zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
     for label, alternative in labeled_alternatives.items():
          print(f"  {label}) {alternative}")

     while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
          print(f"Please answer one of {', '.join(labeled_alternatives)}")

     answer = labeled_alternatives[answer_label]
     if answer == correct_answer:
           num_correct += 1
           print("⭐ Correct! ⭐")
     else:
           print(f"The answer is {correct_answer!r}, not {answer!r}")

 print(mid,f"You got {num_correct} correct out of {num} questions") 
        
def rules():
 print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
3. This Quiz will contain questions From Computer technologies from Java,Python,Php and Html.
4. Each Question Will have Time Limit Of 60 sec.If you are not able to answer the Question in time,then user will be automatically redirected to 
next Question.  ''')

def about():
 print('''\n==========ABOUT US==========
Developed By Mainak Duttaroy''')

if __name__ == "__main__":
        choice = 1
        while choice != 4:
                 print('\n=========WELCOME TO QUIZ SYSTEM==========')
                 print('--------------------------')
                 print('1. PLAY QUIZ')
                 print('2.SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
                 print('3.ABOUT US')
                 print('4.Exit')
                 choice = int(input('ENTER YOUR CHOICE: '))
                 if choice == 1:
                        play()
                 elif choice == 2:
                        rules()
                 elif choice == 3:
                        about()
                 elif choice == 4:
                        break
                 else:
                        print('WRONG INPUT. ENTER THE CHOICE AGAIN')

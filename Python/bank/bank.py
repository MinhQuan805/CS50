def main():
     greeting = input('Greeting: ').strip().lower()
     result = greet(greeting)
     print(result)
def greet(string):
       if string.startswith("hello"):
            return "$0"
       elif string.startswith('h'):
            return "$20"
       else:
           return "$100"

main()

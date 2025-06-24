# this is the simple chat bot chat

def  get_response(use_input):
  use_input = use_input.lower()
  if "hello" in use_input or "hi" use_input:
    return "hi how are you"
  elif "how are you" in use_input:
    return "i am fine and you"
  else:
    " I AM NOt sure what can i do"

def chatbot():
  print ("hello i am a chatbot")
    while True:
      use_input = input("you" ).lower()
    if "exit" in use_input:
      print("goodbye")
    break
    response = get_response(use_input)
    print(f"chatbot: {response}")


if __name__ == "__main__":
chatbot()

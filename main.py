from modules.speak import speak
from modules.speech import listen
from modules.brain import ask_ai
from modules.web_search import web_search
speak("Nexa is online")
while True:
  text=listen()
  if not text:
    continue
  if"hello nexa" in text or "nexa"in text:
    print("NEXA: Yes Praveen,I am listening")
    speak("Yes Praveen,I am listening")
    continue
  if "exit" in text or "goodbye" in text or "stop" in text:
    speak("Goodbye Praveen")
    break
  if "search" in text:
    query=text.replace("search","").strip()
    answer=web_search(query)
  else:
    answer=ask_ai(text)
  print("\nNEXA:",answer)
  speak(answer)


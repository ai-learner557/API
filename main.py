import requests
def get_random_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)

    if response.status_code==200:
        print(f"Full JSON response: {response.json()}")
        joke_data=response.json()
        return f"{joke_data['setup']} \n{joke_data['punchline']}"
    else:
        return "Failed to fetch a joke.Please try again later"
def min():
    print("Welcome to the random Joke Generator!")
    while True:
        user_input=input("Press Enter to get a random joke or 'q'to quit: ")
        if user_input.lower()=='q':
         break
        joke=get_random_joke()
        print("\nRandom Joke:")
        print(joke)
if __name__=="__main__":
    min()
import time

# module
def countdown(user_input):
    while user_input >= 0:
        minutes, seconds = divmod(user_input, 60)
        timer = f'{minutes:02d}:{seconds:02d}'
        print(timer, end='\r')
        time.sleep(1)
        user_input -= 1
    print('Time is up')

if __name__ == '__main__':
    user_input = int(input('Enter the time in seconds : '))
    countdown(user_input)
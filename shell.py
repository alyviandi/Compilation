import pytjawa

while True:
    text = input('pytjawa > ')
    result, error = pytjawa.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number!')
    except KeyboardInterrupt:
        print('\nNo input taken')
        break # don't forget to add break statement
    finally:
        print('\nAttempted Input\n')
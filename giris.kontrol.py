email = 'Eyupkilic1901@gmail.com'
password = 'eyupk'


entry_email = input('emaili girin: ')
entry_password = input('şifrenizi girin: ')


if (email == entry_email):
    if (password == entry_password):
        print('giriş başarılı yönlendiriliyorsunuz')

    else:
        print('şifreniz yanlış tekrar deneyin')

else:
    print('emailiniz yanlış lütfen tekrar deneyin')

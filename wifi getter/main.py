from profiles import *

def main():
    getter = ProfileGetter()
    passwords_profiles = PasswordGetter(getter.extract_profiles())
    for item in passwords_profiles.get_profiles_passwords():
        print(item)


if __name__ == '__main__':
    main()
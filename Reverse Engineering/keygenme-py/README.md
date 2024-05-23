# PicoCTF2021 - keygenme-py

## Description
[keygenme-trial.py](./keygenme-trial.py)

## Solution
1. Inspected source code of ```keygeme-trial.py```

2. Analysed the source code finding:

    1. ```enter_license()``` calls ```check_key(user_key, bUsername_trial)``` and supposedly decrypts ```full_version``` 
    2. In ```check_key(user_key, bUsername_trial)``` function, you need to craft a key such that it passses the check:
    ```
        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False
    ```
    3. Key has the format: ```picoCTF{1n_7h3_|<3y_of_xxxxxxxx}```, whereby the ```xxxxxxxx``` needs to be forged to pass the checks
    4. ```username_trial``` has value ```MORTON``` as in SHA256 encoded, where the key value must match the hash for the indexes in order of: \[4, 5, 3, 6, 2, 7, 1, 8\]
3. Created ```script.py``` to generate the license key which is also the flag

## Flag
```picoCTF{1n_7h3_|<3y_of_75fc1081}```
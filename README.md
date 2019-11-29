# PyPassword - Manager // Simple and Crypted

+ How to use:

        python3 main.py

        There's a easy to use CLI. In the interface you can Write, Read and Delete entrys from the Database.

        At first start, PyPassword generates a default database named [passmandb] but you can change this name at startup. After that PyPassword prompted to input a username.

        Every entry, except the Service name (e.g. Google.de),  is aes encrypted. For the AES Module, your username is used as the Key. This username is sha256 hashed and saved to the database. You can only use the generated database with the right username, saved at the time of generating. One username per database!

+ What are the requirements:

        pip3 install zxcvbn && pip3 install pycrypto

+ Info:

        There's currently a additional GUI file in the repo.
        Don't use it! That file was just for testing some stuff for a GUI
        version i will upload later.

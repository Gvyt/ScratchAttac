from flask import Flask
from threading import Thread
import backend_code
Thread(target=backend_code.run).start()

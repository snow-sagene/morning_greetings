#from morning_greetings.contact import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message
from morning_greetings.contact_manager import ContactsManager


manager = ContactsManager()
friends_list = manager.get_contacts()

try:
        
    for i in friends_list:
        message = generate_message(i['name'])
        send_message(i['email'], message)
        log_message(i, message)
except:
    print("Error detected")
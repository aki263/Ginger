from .Model import db, Person, Address, Email, PhoneNumber, Group, PersonGroup
import logging



class PersonOperation:
    """
    This is the main class for person manupilation it has multiple fuction to create and link multiple persons
    """


    def create_person(self, first_name, last_name):
        """

        :param first_name: This is the param that is for the first name of the person
        :param last_name: this is the last name of the person
        :return: it returns true so you know what happened, else check logs
        """
        try:
            self.user,created = Person.get_or_create(first_name=first_name, last_name=last_name)
            if self.user:
                logging.info('Data Inserted')
                return True
        except Exception as ex:
            logging.error('Error in Data Creation'+str(ex))
        return False

    def add_phone_for_user(self, phone_list=list()):
        """

        :param phone_list: this takes in list of phone number and links it to person
        :return True
        """
        try:
            for phone in phone_list:
                if len(phone) != 10 and phone is not None:
                    if PhoneNumber.create(PersonModel=self.user, phone=phone):
                        logging.info('Phone number Inserted for User')
                        return True
                else:
                    logging.error("Phone number must be of 10 digits")
        except Exception as ex:
            logging.error("Error in phone number insertion")
        return  False

    def add_user_to_group(self, group_name):
        """
        This links the person to a given group, if group doesnt exits, it creates the group
        :param group_name: name of the group
        :return: true or false
        """
        try:
            grp, created =Group.get_or_create(group_name=group_name)
            if PersonGroup.create(PersonModel=self.user, GroupModel=grp):
                return True
        except Exception as ex:
            logging.error("Error in user insertion in Group " + str(ex))
        return False
    def add_address_for_user(self, address):
        """
        This addes the address to the user
        :param address: address as string
        :return: true or false
        """
        try:
            if address is not None or address is not '':
                if Address.get_or_create(PersonModel=self.user, address=address):
                    logging.info("Addess added for person")
                    return True
            else:
                logging.error("Address is empty or none")
        except Exception as ex:
            logging.error("Address creation error " + str(ex))
        return False

    def add_email_for_user(self, email):
        """
        Links email with the user
        :param email: takes in the email
        :return: true or false
        """
        try:
            if email is not None or email is not '':
                if Email.get_or_create(PersonModel=self.user, email=email):
                    logging.info("Email added for person")
                    return True
            else:
                logging.error("Email is empty or none")
        except Exception as ex:
            logging.error("Email creation error " + str(ex))
        return False

    def get_person_groups(self):
        """
        THis get all the group of a given person
        :return list of group with the total in touple like (6, ['111111', '111111', '111111', '111111', '111111', '111111'])
        """
        try:
            temp=[usr.group_name for usr in self.user.find_user_group()]
            return (len(temp),temp)
        except Exception as ex:
            logging.error("Error in getting person groups " + str(ex))

    def get_person_emails(self):
        """
        this return all the user email
        :return: (6, ['xyz@xyz.com', 'xyz@xyz.com', 'xyz@xyz.com', 'xyz@xyz.com', 'xyz@xyz.com', 'xyz@xyz.com'])
        """
        try:
            temp=[emaill.email for emaill in self.user.find_user_email()]
            return (len(temp),temp)
        except Exception as ex:
            logging.error("Error in getting person emails " + str(ex))

    def get_person_phonenumbers(self):
        """
        this returns all the phone number of the user
        :return: (6, ['111111', '111111', '111111', '111111', '111111', '111111'])
        """
        try:
            temp = [emaill.phone for emaill in self.user.find_user_phone()]
            return (len(temp), temp)

        except Exception as ex:
            logging.error("Error in getting person phone numbers " + str(ex))

    def find_person(self, name=None):
        """
    This takes name and searches in db
        :param name: should have space to search in indivdually in fname and lname
        :return: list of names
        """
        try:
            if name != '' or name != ' ':
                fname = lname = ''
                if ' ' in name:
                    fname = name.split(' ')[0]
                    lname = name.split(' ')[1]
                else:
                    fname = lname = name
                return (x.first_name for x in
                        self.user.select().where(Person.last_name.contains(lname) & Person.first_name.contains(fname)))
        except Exception as ex:
            logging.error("Error in searching Person" + str(ex))

    def find_person_by_email(self, email=None):
        """
        this will finf person with email
        :param email: you can supply either the exact string or a prefix string, ie. both "alexander@company.com" and "alex" should work
        :return: person
        """
        try:
            if email is not None or email is not '':
                temp = [emai.id for emai in
                        Email.select().where((Email.email == email) | (Email.email.startswith(email)))]
                return len(temp), [x.first_name for x in Person.select().where(Person.id << temp)]
        except Exception as ex:
            logging.error("Error in fiding by email")

    def find_person_by_email_design(self, email=None):
        """
        this will seach email
        you can supply any substring, ie. "comp" should work assuming "alexander@company.com" is an email address in the address book
        :param email:
        :return: person
        """
        try:
            if email is not None or email is not '':
                temp = [emai.id for emai in Email.select().where((Email.email.contains(email)))]
                return len(temp), [x.first_name for x in Person.select().where(Person.id << temp)]
        except Exception as ex:
            logging.error("Error in fiding by email")

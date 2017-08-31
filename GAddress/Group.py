from . import Model
import logging


class Group:
    def __init__(self):
        self.group =''

    def create_group(self, group_name):
        """
        this is for creating group
        :param group_name: name of the group
        :return: instance of group
        """
        try:
            return Group.get_or_create(group_name=group_name)
        except Exception as ex:
            logging.error("Error in creating group " + str(ex))

    def get_group_member(self, group_name):
        """
        this will give the names of all the member of a group
        :param group_name:name of the group
        :return: list og all the people in the group
        """
        try:
            self.group=Group.get(group_name==group_name)
            temp = self.group.find_group_member()
            return len(temp), [person.first_name + ' ' + person.last_name for person in temp]
        except Exception as ex:
            logging.error("Error in getting total member of group")

# Adapter is a structural design pattern

# Adapters design pattern is used when we have a class (Client) expecting some
# type of object and we have an object (Adaptee) offering the same features
# but exposing a different interface.

# One example is as follows: Consider a 3rd party library that requires data in
# JSON format, but we only have XML data. In this can we have to create an
# "adapter" object, which is a special object that converts the interface of
# one object so that another object can understand it.

# Commonly used when legacy code is to be used with modern classes.


# Assume that we have a library accepting JSON data
# JSONData is target class type.
class JSONData:
    def get_json(self):
        return {
            "uname": "Jack",
            "password": "Kcaj"
        }


# XML needs to be converted into JSON inorder to use
# library. So this class is adaptee.
class XMLData:
    def get_xml(self):
        return '''
        <data>
            <uname> Jack </uname>
            <password> Kcaj </password>
        </data>
        '''


class Adapter(XMLData):
    def get_json(self):
        xml = self.get_xml()
        # Convert XML to JSON here.
        # ...
        return {
            "uname": "Jack",
            "password": "Kcaj"
        }

def library(strictly_json):
    """
    Library function strictly accepting JSON as input.
    """
    print(strictly_json.get_json())


if __name__ == "__main__":

    # This works well.
    library(JSONData())

    # But to use our XML data with this "library" function,
    # We first need to convet it into JSON.
    adapter = Adapter()
    library(adapter)


# OUTPUT:
# {'uname': 'Jack', 'password': 'Kcaj'}
# {'uname': 'Jack', 'password': 'Kcaj'}

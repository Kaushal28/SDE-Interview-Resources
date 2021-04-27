# Proxy is structured design pattern

# Proxy pattern provides an object that acts as a substitute for a real
# service object used by a client. A proxy receives client requests,
# does some work (access control, caching, etc.) and then passes the
# request to a service object.

# Proxy objects are used in place of resource heavy objects to make sure
# they are initialized only when required. Also, using proxy, we get chance
# to execute some code before/after the actual initialization.

# Example: https://stackoverflow.com/a/28054029/5353128


# Real subject, which will be abstracted using proxy
class Image:
    def __init__(self, filename):
        self.filename = filename
    
    def load_image(self):
        print(f"Loading file from disk: {self.filename}")
    

class Proxy:
    def __init__(self, subject):
        self.subject = subject


class ProxyImage(Proxy):

    # This method should be same as real subject to provide
    # same experience as the real subject.
    def load_image(self):
        if self._have_access():
            self.subject.load_image()
            print("Image loaded!")
    
    def _have_access(self):
        """Some extra functionality here."""
        return True


if __name__ == "__main__":

    image = ProxyImage(Image("my_image.png"))
    image.load_image()


# OUTPUT:
# Loading file from disk: my_image.png
# Image loaded!
